import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Financial Returns Analyzer",
    page_icon="📈",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .ticker-input {
        margin-bottom: 2rem;
    }
</style>
""", unsafe_allow_html=True)

def get_stock_data(ticker, period="3mo"):
    """Fetch stock data from Yahoo Finance"""
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period)
        return data
    except Exception as e:
        st.error(f"Error fetching data for {ticker}: {str(e)}")
        return None

def calculate_daily_returns(data):
    """Calculate daily returns"""
    if data is None or data.empty:
        return None
    returns = data['Close'].pct_change().dropna()
    return returns

def calculate_statistics(returns):
    """Calculate financial statistics"""
    if returns is None or returns.empty:
        return None
    
    stats = {
        'Mean Daily Return (%)': returns.mean() * 100,
        'Standard Deviation (%)': returns.std() * 100,
        'Annualized Return (%)': returns.mean() * 252 * 100,
        'Annualized Volatility (%)': returns.std() * np.sqrt(252) * 100,
        'Sharpe Ratio': (returns.mean() / returns.std()) * np.sqrt(252),
        'Min Daily Return (%)': returns.min() * 100,
        'Max Daily Return (%)': returns.max() * 100,
        'Total Return (%)': ((returns + 1).prod() - 1) * 100
    }
    return stats

def plot_returns(data, returns, ticker):
    """Create interactive plots"""
    if data is None or returns is None:
        return
    
    # Create figure with secondary y-axis
    fig = go.Figure()
    
    # Add price data
    fig.add_trace(go.Scatter(
        x=data.index,
        y=data['Close'],
        mode='lines',
        name='Stock Price',
        line=dict(color='#1f77b4', width=2),
        yaxis='y'
    ))
    
    # Add returns data
    fig.add_trace(go.Scatter(
        x=returns.index,
        y=returns * 100,
        mode='lines',
        name='Daily Returns (%)',
        line=dict(color='#ff7f0e', width=1),
        yaxis='y2'
    ))
    
    # Update layout
    fig.update_layout(
        title=f'{ticker.upper()} - Stock Price and Daily Returns (Last 3 Months)',
        xaxis_title='Date',
        yaxis=dict(title='Stock Price ($)', side='left'),
        yaxis2=dict(title='Daily Returns (%)', side='right', overlaying='y'),
        hovermode='x unified',
        height=500,
        showlegend=True
    )
    
    return fig

def plot_returns_distribution(returns, ticker):
    """Plot returns distribution"""
    if returns is None:
        return
    
    fig = px.histogram(
        x=returns * 100,
        nbins=30,
        title=f'{ticker.upper()} - Daily Returns Distribution',
        labels={'x': 'Daily Returns (%)', 'y': 'Frequency'},
        color_discrete_sequence=['#1f77b4']
    )
    
    fig.add_vline(x=returns.mean() * 100, line_dash="dash", line_color="red", 
                  annotation_text=f"Mean: {returns.mean() * 100:.2f}%")
    
    return fig

def main():
    # Header
    st.markdown('<h1 class="main-header">📈 Financial Returns Analyzer</h1>', unsafe_allow_html=True)
    
    # Sidebar for input
    st.sidebar.header("📊 Data Input")
    
    # Ticker input
    ticker_input = st.sidebar.text_input(
        "Enter Stock Ticker or Company Name:",
        placeholder="e.g., AAPL, MSFT, GOOGL",
        help="Enter a valid stock ticker symbol"
    )
    
    # Period selection
    period = st.sidebar.selectbox(
        "Data Period:",
        ["3mo", "6mo", "1y"],
        index=0,
        help="Select the time period for analysis"
    )
    
    # Analysis button
    analyze_button = st.sidebar.button("🚀 Analyze", type="primary")
    
    if analyze_button and ticker_input:
        with st.spinner(f"Fetching data for {ticker_input.upper()}..."):
            # Get data
            data = get_stock_data(ticker_input, period)
            
            if data is not None and not data.empty:
                # Calculate returns
                returns = calculate_daily_returns(data)
                
                if returns is not None:
                    # Display basic info
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric("Current Price", f"${data['Close'].iloc[-1]:.2f}")
                    
                    with col2:
                        price_change = data['Close'].iloc[-1] - data['Close'].iloc[-2]
                        price_change_pct = (price_change / data['Close'].iloc[-2]) * 100
                        st.metric("Daily Change", f"${price_change:.2f}", f"{price_change_pct:.2f}%")
                    
                    with col3:
                        st.metric("Data Points", len(returns))
                    
                    # Create tabs for different views
                    tab1, tab2, tab3 = st.tabs(["📈 Price & Returns", "📊 Statistics", "📋 Distribution"])
                    
                    with tab1:
                        st.plotly_chart(plot_returns(data, returns, ticker_input), use_container_width=True)
                    
                    with tab2:
                        # Calculate and display statistics
                        stats = calculate_statistics(returns)
                        
                        if stats:
                            col1, col2 = st.columns(2)
                            
                            with col1:
                                st.markdown("### 📊 Key Statistics")
                                for key, value in list(stats.items())[:4]:
                                    if 'Sharpe' in key:
                                        st.metric(key, f"{value:.3f}")
                                    else:
                                        st.metric(key, f"{value:.2f}%")
                            
                            with col2:
                                st.markdown("### 📈 Additional Metrics")
                                for key, value in list(stats.items())[4:]:
                                    if 'Sharpe' in key:
                                        st.metric(key, f"{value:.3f}")
                                    else:
                                        st.metric(key, f"{value:.2f}%")
                    
                    with tab3:
                        st.plotly_chart(plot_returns_distribution(returns, ticker_input), use_container_width=True)
                        
                        # Additional insights
                        st.markdown("### 💡 Insights")
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            positive_days = (returns > 0).sum()
                            total_days = len(returns)
                            win_rate = (positive_days / total_days) * 100
                            st.metric("Win Rate", f"{win_rate:.1f}%")
                        
                        with col2:
                            volatility = returns.std() * 100
                            if volatility < 2:
                                risk_level = "Low"
                            elif volatility < 4:
                                risk_level = "Medium"
                            else:
                                risk_level = "High"
                            st.metric("Risk Level", risk_level)
                
                else:
                    st.error("Unable to calculate returns. Please check the ticker symbol.")
            else:
                st.error(f"No data found for {ticker_input}. Please check the ticker symbol.")
    
    elif not ticker_input and analyze_button:
        st.warning("Please enter a stock ticker to analyze.")
    
    # Instructions
    if not analyze_button:
        st.markdown("""
        ### 🎯 How to Use This App
        
        1. **Enter a Stock Ticker**: Use the sidebar to input a valid stock ticker (e.g., AAPL, MSFT, GOOGL)
        2. **Select Time Period**: Choose how much historical data to analyze (3 months, 6 months, or 1 year)
        3. **Click Analyze**: Press the "Analyze" button to fetch data and generate insights
        4. **Explore Results**: View price charts, returns distribution, and key statistics
        
        ### 📊 What You'll Get
        
        - **Price & Returns Chart**: Interactive plot showing stock price and daily returns
        - **Key Statistics**: Mean, standard deviation, Sharpe ratio, and more
        - **Returns Distribution**: Histogram showing the distribution of daily returns
        - **Risk Analysis**: Win rate and risk level assessment
        
        ### 💡 Popular Tickers to Try
        
        - **Tech**: AAPL, MSFT, GOOGL, AMZN, TSLA
        - **Finance**: JPM, BAC, WFC, GS
        - **Healthcare**: JNJ, PFE, UNH, ABBV
        """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        📈 Financial Returns Analyzer | Powered by Yahoo Finance API
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 