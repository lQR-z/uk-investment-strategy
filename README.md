# 🇬🇧 UK Investment Strategy Analyzer

A comprehensive investment evaluation dashboard that analyzes UK investments considering geopolitical risks, supply chain dynamics, and international capital flows.

## 🎯 Overview

This application provides a sophisticated framework for evaluating UK investments by incorporating three critical dimensions that significantly impact domestic economic stability and growth:

1. **🌍 Geopolitical Risks** - Brexit implications, international relations, and policy uncertainty
2. **🔗 Supply Chain Dynamics** - Global trade disruptions, logistics challenges, and sector-specific vulnerabilities  
3. **💰 International Capital Flows** - Foreign investment patterns, currency dynamics, and monetary policy impacts

## ✨ Features

### 📊 Dashboard Components
- **Market Overview** - Real-time FTSE data, currency rates, economic indicators
- **Geopolitical Analysis** - Brexit impact, EU relations, global trade tensions
- **Supply Chain Dynamics** - Manufacturing, services, and energy sector analysis
- **Capital Flows** - FDI, portfolio investment, and currency strength evaluation
- **Investment Recommendations** - Sector-specific analysis and risk mitigation strategies
- **Company Analysis** - Individual company assessment with comprehensive risk scoring

### 🏢 Company Analysis Features
- **200+ UK Companies** supported with automatic ticker detection
- **Sector Classification** - Automatic sector determination
- **Risk Assessment** - Geopolitical, supply chain, and capital flow risk scoring
- **Financial Metrics** - Volatility, Sharpe ratio, returns, and drawdown analysis
- **Investment Recommendations** - Buy/Hold/Sell recommendations with confidence levels

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/uk-investment-strategy.git
   cd uk-investment-strategy
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run uk_investment_strategy.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501`

## 📁 Project Structure

```
uk-investment-strategy/
├── uk_investment_strategy.py    # Main application
├── requirements.txt             # Python dependencies
├── run_uk_strategy.py          # Launcher script
├── UK_Investment_Strategy_Guide.md  # Detailed strategy guide
├── README.md                   # This file
└── .gitignore                  # Git ignore file
```

## 🎯 Investment Strategy Framework

### Geopolitical Risk Assessment
- **Brexit Impact** (Risk Score: 0.8) - Trade relations, financial services, labor market
- **EU Relations** (Risk Score: 0.7) - Trade agreements, regulatory alignment
- **Global Trade Tensions** (Risk Score: 0.9) - US-China relations, supply chain disruption

### Supply Chain Analysis
- **Manufacturing Sector** - Capacity utilization, input cost inflation, lead times
- **Services Sector** - Digital infrastructure, skilled labor availability
- **Energy Sector** - Energy security, price volatility, green transition

### Capital Flow Evaluation
- **FDI Attractiveness** - Political stability, regulatory environment, market access
- **Portfolio Investment** - Market liquidity, currency stability, interest rates
- **Currency Strength** - Trade balance, interest rate differentials, economic fundamentals

## 💡 Usage Examples

### Analyzing Individual Companies
1. Navigate to the "🏢 Company Analysis" tab
2. Enter a company name (e.g., "HSBC", "Tesco", "AstraZeneca")
3. Click "Analyze Company"
4. Review comprehensive risk assessment and investment recommendation

### Sector-Specific Analysis
1. Go to "📊 Investment Recommendations" tab
2. Select a sector from the dropdown
3. View detailed sector-specific risk factors and opportunities

## 🔧 Configuration

The application uses real-time data from Yahoo Finance and can be customized by modifying the risk factors and weights in the `UKInvestmentStrategy` class.

## 📊 Supported Companies

The application supports analysis of major UK companies including:

**Financial Services**: HSBC, Barclays, Lloyds, NatWest
**Technology**: Sage Group, ASOS, Boohoo, Ocado  
**Healthcare**: AstraZeneca, GlaxoSmithKline
**Energy**: BP, Shell, Centrica, National Grid
**Retail**: Tesco, Sainsbury's, Morrisons, Next
**Manufacturing**: Rolls Royce, BAE Systems, Weir Group

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This application is for educational and research purposes only. Investment decisions should be based on comprehensive analysis and consultation with financial advisors. The authors are not responsible for any financial losses resulting from the use of this tool.

## 📞 Support

For questions or support, please open an issue on GitHub or contact the development team.

---

**Built with ❤️ for UK investment analysis** 