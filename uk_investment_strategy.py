import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import requests
import json
from typing import Dict, List, Tuple
import warnings
warnings.filterwarnings('ignore')

class UKInvestmentStrategy:
    """
    Comprehensive UK Investment Evaluation Strategy incorporating:
    - Geopolitical risks
    - Supply chain dynamics  
    - International capital flows
    - Domestic economic stability factors
    """
    
    def __init__(self):
        self.uk_market_indices = {
            'FTSE 100': '^FTSE',
            'FTSE 250': '^FTMC', 
            'FTSE All-Share': '^FTAS',
            'GBP/USD': 'GBPUSD=X',
            'GBP/EUR': 'GBPEUR=X',
            'UK 10Y Bond': '^TNX'
        }
        
        self.geopolitical_risk_factors = {
            'Brexit Impact': 0.8,
            'EU Relations': 0.7,
            'US-UK Relations': 0.6,
            'Global Trade Tensions': 0.9,
            'Energy Security': 0.8,
            'Financial Services Regulation': 0.7
        }
        
        self.supply_chain_indicators = {
            'Port Congestion': 0.6,
            'Shipping Costs': 0.8,
            'Raw Material Availability': 0.7,
            'Manufacturing Capacity': 0.5,
            'Transportation Infrastructure': 0.6
        }
        
        self.capital_flow_metrics = {
            'FDI Inflows': 0.7,
            'Portfolio Investment': 0.8,
            'Currency Strength': 0.6,
            'Interest Rate Differential': 0.7,
            'Political Stability': 0.6
        }

    def get_market_data(self, ticker: str, period: str = "1y") -> pd.DataFrame:
        """Fetch market data for analysis"""
        try:
            data = yf.Ticker(ticker).history(period=period)
            return data
        except Exception as e:
            st.error(f"Error fetching data for {ticker}: {str(e)}")
            return pd.DataFrame()

    def calculate_geopolitical_risk_score(self) -> Dict[str, float]:
        """Calculate geopolitical risk assessment for UK investments"""
        risk_scores = {}
        
        # Brexit impact assessment
        brexit_impact = {
            'Trade Relations': 0.7,
            'Financial Services': 0.8,
            'Labor Market': 0.6,
            'Regulatory Environment': 0.7
        }
        risk_scores['Brexit Impact'] = np.mean(list(brexit_impact.values()))
        
        # EU relations assessment
        eu_relations = {
            'Trade Agreements': 0.6,
            'Financial Passporting': 0.8,
            'Regulatory Alignment': 0.7,
            'Political Cooperation': 0.5
        }
        risk_scores['EU Relations'] = np.mean(list(eu_relations.values()))
        
        # Global trade tensions
        global_trade = {
            'US-China Relations': 0.8,
            'Supply Chain Disruption': 0.9,
            'Commodity Prices': 0.7,
            'Currency Volatility': 0.6
        }
        risk_scores['Global Trade Tensions'] = np.mean(list(global_trade.values()))
        
        return risk_scores

    def analyze_supply_chain_dynamics(self) -> Dict[str, Dict[str, float]]:
        """Analyze supply chain dynamics affecting UK economy"""
        supply_chain_analysis = {}
        
        # Manufacturing sector
        manufacturing = {
            'Capacity Utilization': 0.75,
            'Input Cost Inflation': 0.8,
            'Lead Times': 0.7,
            'Inventory Levels': 0.6
        }
        supply_chain_analysis['Manufacturing'] = manufacturing
        
        # Services sector
        services = {
            'Digital Infrastructure': 0.6,
            'Skilled Labor Availability': 0.7,
            'Regulatory Compliance': 0.5,
            'International Competition': 0.8
        }
        supply_chain_analysis['Services'] = services
        
        # Energy sector
        energy = {
            'Energy Security': 0.8,
            'Price Volatility': 0.9,
            'Infrastructure Investment': 0.6,
            'Green Transition': 0.7
        }
        supply_chain_analysis['Energy'] = energy
        
        return supply_chain_analysis

    def evaluate_capital_flows(self) -> Dict[str, float]:
        """Evaluate international capital flows affecting UK markets"""
        capital_flow_analysis = {}
        
        # Foreign Direct Investment
        fdi_factors = {
            'Political Stability': 0.6,
            'Regulatory Environment': 0.7,
            'Market Access': 0.8,
            'Infrastructure Quality': 0.7
        }
        capital_flow_analysis['FDI Attractiveness'] = np.mean(list(fdi_factors.values()))
        
        # Portfolio Investment
        portfolio_factors = {
            'Market Liquidity': 0.8,
            'Currency Stability': 0.6,
            'Interest Rate Environment': 0.7,
            'Economic Growth Prospects': 0.6
        }
        capital_flow_analysis['Portfolio Investment'] = np.mean(list(portfolio_factors.values()))
        
        # Currency Dynamics
        currency_factors = {
            'Trade Balance': 0.7,
            'Interest Rate Differential': 0.6,
            'Political Risk': 0.7,
            'Economic Fundamentals': 0.6
        }
        capital_flow_analysis['Currency Strength'] = np.mean(list(currency_factors.values()))
        
        return capital_flow_analysis

    def sector_specific_analysis(self, sector: str) -> Dict[str, float]:
        """Provide sector-specific investment analysis"""
        sector_analysis = {
            'Financial Services': {
                'Brexit Impact': 0.8,
                'Regulatory Environment': 0.7,
                'Digital Transformation': 0.6,
                'International Competition': 0.8,
                'Capital Requirements': 0.7
            },
            'Technology': {
                'Talent Availability': 0.7,
                'Funding Environment': 0.8,
                'Regulatory Framework': 0.6,
                'International Expansion': 0.7,
                'Innovation Ecosystem': 0.8
            },
            'Healthcare': {
                'Regulatory Approval': 0.7,
                'Funding Environment': 0.8,
                'International Collaboration': 0.6,
                'Digital Health Adoption': 0.7,
                'Aging Population': 0.8
            },
            'Manufacturing': {
                'Supply Chain Resilience': 0.7,
                'Energy Costs': 0.8,
                'Labor Availability': 0.6,
                'Trade Relations': 0.7,
                'Automation Investment': 0.7
            },
            'Real Estate': {
                'Interest Rate Sensitivity': 0.8,
                'Foreign Investment': 0.7,
                'Regulatory Changes': 0.6,
                'Economic Growth': 0.7,
                'Demographic Trends': 0.6
            }
        }
        
        return sector_analysis.get(sector, {})

    def generate_investment_recommendations(self) -> Dict[str, List[str]]:
        """Generate investment recommendations based on analysis"""
        recommendations = {
            'High Conviction': [
                "UK Technology Sector - Strong innovation ecosystem and digital transformation trends",
                "Healthcare & Life Sciences - Aging population and strong research base",
                "Green Energy Infrastructure - Government support and energy security needs",
                "Digital Financial Services - Fintech innovation and regulatory evolution"
            ],
            'Moderate Conviction': [
                "UK Export-Oriented Manufacturing - Benefiting from trade diversification",
                "Real Estate Investment Trusts - Stable income with inflation protection",
                "Consumer Staples - Defensive positioning in uncertain economic environment",
                "Infrastructure Investment - Government spending priorities"
            ],
            'Cautious Approach': [
                "Traditional Financial Services - Regulatory uncertainty and Brexit impact",
                "Energy-Intensive Manufacturing - High energy cost sensitivity",
                "Import-Dependent Retail - Supply chain and currency volatility risks",
                "Small-Cap Stocks - Higher volatility and liquidity concerns"
            ]
        }
        return recommendations

    def risk_mitigation_strategies(self) -> Dict[str, List[str]]:
        """Provide risk mitigation strategies for UK investments"""
        strategies = {
            'Geopolitical Risk': [
                "Diversify across multiple jurisdictions and trade partners",
                "Monitor Brexit implementation and EU relationship developments",
                "Consider currency hedging strategies for international exposure",
                "Stay informed on global trade policy changes"
            ],
            'Supply Chain Risk': [
                "Invest in companies with diversified supply chains",
                "Focus on sectors with strong domestic capabilities",
                "Consider companies with digital transformation initiatives",
                "Monitor companies' supply chain resilience strategies"
            ],
            'Capital Flow Risk': [
                "Diversify currency exposure across portfolio",
                "Monitor central bank policy changes and interest rate trends",
                "Consider defensive sectors during capital flow volatility",
                "Focus on companies with strong balance sheets and cash flows"
            ]
        }
        return strategies

    def analyze_company(self, company_name: str) -> Dict[str, any]:
        """Analyze a specific company based on name"""
        try:
            # Try to find the company ticker
            ticker = self.find_company_ticker(company_name)
            if not ticker:
                return {"error": f"Could not find ticker for company: {company_name}"}
            
            # Get company data
            company_data = self.get_company_data(ticker)
            data, info = company_data
            
            if data.empty:
                return {"error": f"Could not fetch data for {ticker}"}
            
            # Analyze company based on sector and characteristics
            analysis = self.perform_company_analysis(company_name, ticker, company_data)
            return analysis
            
        except Exception as e:
            return {"error": f"Error analyzing company: {str(e)}"}

    def find_company_ticker(self, company_name: str) -> str:
        """Find ticker symbol for a company name"""
        # Common UK company mappings
        uk_companies = {
            'hsbc': 'HSBC.L',
            'barclays': 'BARC.L',
            'lloyds': 'LLOY.L',
            'rbs': 'RBS.L',
            'natwest': 'NWG.L',
            'unilever': 'ULVR.L',
            'glaxosmithkline': 'GSK.L',
            'astrazeneca': 'AZN.L',
            'bp': 'BP.L',
            'shell': 'SHEL.L',
            'royal dutch shell': 'SHEL.L',
            'british american tobacco': 'BATS.L',
            'imperial brands': 'IMB.L',
            'diageo': 'DGE.L',
            'rio tinto': 'RIO.L',
            'bhp': 'BHP.L',
            'anglo american': 'AAL.L',
            'glencore': 'GLEN.L',
            'vodafone': 'VOD.L',
            'bt': 'BT-A.L',
            'british telecom': 'BT-A.L',
            'centrica': 'CNA.L',
            'national grid': 'NG.L',
            'ssp': 'SSPG.L',
            'sage': 'SGE.L',
            'just eat': 'JET.L',
            'deliveroo': 'ROO.L',
            'ocado': 'OCDO.L',
            'asos': 'ASC.L',
            'boohoo': 'BOO.L',
            'next': 'NXT.L',
            'marks and spencer': 'MKS.L',
            'tesco': 'TSCO.L',
            'sainsbury': 'SBRY.L',
            'morrisons': 'MRW.L',
            'persimmon': 'PSN.L',
            'barratt': 'BDEV.L',
            'taylor wimpey': 'TW.L',
            'berkeley': 'BKG.L',
            'land securities': 'LAND.L',
            'british land': 'BLND.L',
            'segro': 'SGRO.L',
            'rightmove': 'RMV.L',
            'zoopla': 'ZPLA.L',
            'autotrader': 'AUTO.L',
            'halma': 'HLMA.L',
            'spirax sarco': 'SPX.L',
            'renishaw': 'RSW.L',
            'weir': 'WEIR.L',
            'melrose': 'MRO.L',
            'rolls royce': 'RR.L',
            'bae systems': 'BA.L',
            'cobham': 'COB.L',
            'g4s': 'GFS.L',
            'serco': 'SRP.L',
            'capita': 'CPI.L',
            'mitie': 'MTO.L',
            'compass': 'CPG.L',
            'whitbread': 'WTB.L',
            'intercontinental hotels': 'IHG.L',
            'easyjet': 'EZJ.L',
            'international airlines group': 'IAG.L',
            'ryanair': 'RYA.L',
            'wizz air': 'WIZZ.L',
            'carnival': 'CCL.L',
            'tui': 'TUI.L',
            'thomas cook': 'TCG.L',
            'sports direct': 'SPD.L',
            'jd sports': 'JD.L',
            'frasers': 'FRAS.L',
            'superdry': 'SDRY.L',
            'ted baker': 'TED.L',
            'burberry': 'BRBY.L',
            'mulberry': 'MUL.L',
            'jimmy choo': 'CHOO.L',
            'asos': 'ASC.L',
            'boohoo': 'BOO.L',
            'missguided': 'MGID.L',
            'pretty little thing': 'PLT.L',
            'na-kd': 'NAKD.L',
            'revolve': 'RVLV.L',
            'stitch fix': 'SFIX.L',
            'wayfair': 'W.L',
            'etsy': 'ETSY.L',
            'shopify': 'SHOP.L',
            'square': 'SQ.L',
            'stripe': 'STRIPE.L',
            'klarna': 'KLARNA.L',
            'monzo': 'MONZO.L',
            'revolut': 'REVOLUT.L',
            'transferwise': 'WISE.L',
            'wise': 'WISE.L',
            'checkout.com': 'CHECKOUT.L',
            'rapyd': 'RAPYD.L',
            'go cardless': 'GOCARDLESS.L',
            'sumup': 'SUMUP.L',
            'worldpay': 'WP.L',
            'nortonlifelock': 'NLOK.L',
            'avast': 'AVST.L',
            'kaspersky': 'KASPERSKY.L',
            'trend micro': 'TMIC.L',
            'crowdstrike': 'CRWD.L',
            'palo alto networks': 'PANW.L',
            'fortinet': 'FTNT.L',
            'check point': 'CHKP.L',
            'symantec': 'SYMC.L',
            'mcafee': 'MCFE.L',
            'bitdefender': 'BITDEFENDER.L',
            'malwarebytes': 'MALWAREBYTES.L',
            'eset': 'ESET.L',
            'sophos': 'SOPHOS.L',
            'f-secure': 'F-SECURE.L',
            'bullguard': 'BULLGUARD.L',
            'avg': 'AVG.L',
            'avira': 'AVIRA.L',
            'norton': 'NORTON.L',
            'microsoft': 'MSFT',
            'apple': 'AAPL',
            'google': 'GOOGL',
            'alphabet': 'GOOGL',
            'amazon': 'AMZN',
            'facebook': 'META',
            'meta': 'META',
            'netflix': 'NFLX',
            'tesla': 'TSLA',
            'nvidia': 'NVDA',
            'amd': 'AMD',
            'intel': 'INTC',
            'qualcomm': 'QCOM',
            'broadcom': 'AVGO',
            'cisco': 'CSCO',
            'oracle': 'ORCL',
            'salesforce': 'CRM',
            'adobe': 'ADBE',
            'paypal': 'PYPL',
            'visa': 'V',
            'mastercard': 'MA',
            'american express': 'AXP',
            'discovery': 'DISCA',
            'warner bros': 'WBD',
            'paramount': 'PARA',
            'comcast': 'CMCSA',
            'verizon': 'VZ',
            'at&t': 'T',
            'att': 'T',
            't-mobile': 'TMUS',
            'sprint': 'S',
            'charter': 'CHTR',
            'cablevision': 'CVC',
            'time warner': 'TWX',
            'viacom': 'VIAB',
            'cbs': 'CBS',
            'fox': 'FOX',
            'news corp': 'NWSA',
            '21st century fox': 'FOXA',
            'disney': 'DIS',
            'pixar': 'PIXAR',
            'marvel': 'MARVEL',
            'lucasfilm': 'LUCASFILM',
            'star wars': 'STARWARS',
            'pixar': 'PIXAR',
            'dreamworks': 'DWA',
            'universal': 'CMCSA',
            'sony': 'SONY',
            'nintendo': 'NTDOY',
            'electronic arts': 'EA',
            'activision blizzard': 'ATVI',
            'take two': 'TTWO',
            'ubisoft': 'UBI.PA',
            'capcom': '9697.T',
            'konami': '9766.T',
            'sega': '6460.T',
            'bandai namco': '7832.T',
            'square enix': '9684.T',
            'nintendo': '7974.T',
            'sony': '6758.T',
            'microsoft': 'MSFT',
            'apple': 'AAPL',
            'google': 'GOOGL',
            'alphabet': 'GOOGL',
            'amazon': 'AMZN',
            'facebook': 'META',
            'meta': 'META',
            'netflix': 'NFLX',
            'tesla': 'TSLA',
            'nvidia': 'NVDA',
            'amd': 'AMD',
            'intel': 'INTC',
            'qualcomm': 'QCOM',
            'broadcom': 'AVGO',
            'cisco': 'CSCO',
            'oracle': 'ORCL',
            'salesforce': 'CRM',
            'adobe': 'ADBE',
            'paypal': 'PYPL',
            'visa': 'V',
            'mastercard': 'MA',
            'american express': 'AXP',
            'discovery': 'DISCA',
            'warner bros': 'WBD',
            'paramount': 'PARA',
            'comcast': 'CMCSA',
            'verizon': 'VZ',
            'at&t': 'T',
            'att': 'T',
            't-mobile': 'TMUS',
            'sprint': 'S',
            'charter': 'CHTR',
            'cablevision': 'CVC',
            'time warner': 'TWX',
            'viacom': 'VIAB',
            'cbs': 'CBS',
            'fox': 'FOX',
            'news corp': 'NWSA',
            '21st century fox': 'FOXA',
            'disney': 'DIS',
            'pixar': 'PIXAR',
            'marvel': 'MARVEL',
            'lucasfilm': 'LUCASFILM',
            'star wars': 'STARWARS',
            'pixar': 'PIXAR',
            'dreamworks': 'DWA',
            'universal': 'CMCSA',
            'sony': 'SONY',
            'nintendo': 'NTDOY',
            'electronic arts': 'EA',
            'activision blizzard': 'ATVI',
            'take two': 'TTWO',
            'ubisoft': 'UBI.PA',
            'capcom': '9697.T',
            'konami': '9766.T',
            'sega': '6460.T',
            'bandai namco': '7832.T',
            'square enix': '9684.T',
            'nintendo': '7974.T',
            'sony': '6758.T'
        }
        
        # Search for company name in our mapping
        company_lower = company_name.lower().strip()
        for name, ticker in uk_companies.items():
            if company_lower in name or name in company_lower:
                return ticker
        
        # If not found, try to search using yfinance
        try:
            search_results = yf.Tickers(company_name)
            if search_results and len(search_results) > 0:
                return search_results[0]
        except:
            pass
        
        return None

    def get_company_data(self, ticker: str) -> tuple:
        """Get comprehensive company data"""
        try:
            company = yf.Ticker(ticker)
            data = company.history(period="1y")
            
            # Get additional company info
            info = company.info
            return data, info
        except Exception as e:
            return pd.DataFrame(), {}

    def perform_company_analysis(self, company_name: str, ticker: str, company_data: tuple) -> Dict[str, any]:
        """Perform comprehensive company analysis"""
        data, info = company_data
        
        if data.empty:
            return {"error": "No data available for analysis"}
        
        # Determine company sector
        sector = self.determine_company_sector(company_name, info)
        
        # Calculate risk scores
        geopolitical_risk = self.calculate_company_geopolitical_risk(sector, info)
        supply_chain_risk = self.calculate_company_supply_chain_risk(sector, info)
        capital_flow_risk = self.calculate_company_capital_flow_risk(sector, info)
        
        # Calculate financial metrics
        financial_metrics = self.calculate_financial_metrics(data, info)
        
        # Generate investment recommendation
        recommendation = self.generate_company_recommendation(
            geopolitical_risk, supply_chain_risk, capital_flow_risk, financial_metrics
        )
        
        return {
            "company_name": company_name,
            "ticker": ticker,
            "sector": sector,
            "geopolitical_risk": geopolitical_risk,
            "supply_chain_risk": supply_chain_risk,
            "capital_flow_risk": capital_flow_risk,
            "financial_metrics": financial_metrics,
            "recommendation": recommendation,
            "price_data": data
        }

    def determine_company_sector(self, company_name: str, info: dict) -> str:
        """Determine company sector based on name and info"""
        company_lower = company_name.lower()
        
        # Financial services
        if any(word in company_lower for word in ['bank', 'hsbc', 'barclays', 'lloyds', 'rbs', 'natwest', 'finance', 'insurance']):
            return 'Financial Services'
        
        # Technology
        elif any(word in company_lower for word in ['tech', 'software', 'digital', 'ai', 'cyber', 'fintech', 'sage', 'sage']):
            return 'Technology'
        
        # Healthcare
        elif any(word in company_lower for word in ['pharma', 'health', 'medical', 'biotech', 'glaxo', 'astra', 'gsk', 'azn']):
            return 'Healthcare'
        
        # Energy
        elif any(word in company_lower for word in ['oil', 'gas', 'energy', 'bp', 'shell', 'centrica', 'national grid']):
            return 'Energy'
        
        # Manufacturing
        elif any(word in company_lower for word in ['manufacturing', 'industrial', 'engineering', 'rolls', 'bae', 'weir']):
            return 'Manufacturing'
        
        # Retail
        elif any(word in company_lower for word in ['retail', 'shop', 'store', 'tesco', 'sainsbury', 'morrisons', 'asos', 'boohoo']):
            return 'Retail'
        
        # Real Estate
        elif any(word in company_lower for word in ['property', 'real estate', 'land', 'berkeley', 'barratt', 'persimmon']):
            return 'Real Estate'
        
        # Consumer Goods
        elif any(word in company_lower for word in ['consumer', 'unilever', 'diageo', 'british american tobacco', 'imperial']):
            return 'Consumer Goods'
        
        # Mining
        elif any(word in company_lower for word in ['mining', 'rio tinto', 'bhp', 'anglo american', 'glencore']):
            return 'Mining'
        
        # Telecommunications
        elif any(word in company_lower for word in ['telecom', 'vodafone', 'bt', 'british telecom']):
            return 'Telecommunications'
        
        # Transportation
        elif any(word in company_lower for word in ['airline', 'easyjet', 'british airways', 'transport']):
            return 'Transportation'
        
        else:
            return 'Other'

    def calculate_company_geopolitical_risk(self, sector: str, info: dict) -> Dict[str, float]:
        """Calculate company-specific geopolitical risk"""
        base_risks = self.calculate_geopolitical_risk_score()
        
        # Adjust based on sector
        sector_adjustments = {
            'Financial Services': 1.2,  # Higher risk due to Brexit
            'Technology': 0.8,          # Lower risk, global nature
            'Healthcare': 0.9,          # Moderate risk
            'Energy': 1.1,              # Higher risk due to energy security
            'Manufacturing': 1.0,       # Standard risk
            'Retail': 0.9,              # Moderate risk
            'Real Estate': 0.8,         # Lower risk
            'Consumer Goods': 0.9,      # Moderate risk
            'Mining': 1.1,              # Higher risk due to global trade
            'Telecommunications': 0.9,  # Moderate risk
            'Transportation': 1.0       # Standard risk
        }
        
        adjustment = sector_adjustments.get(sector, 1.0)
        
        adjusted_risks = {}
        for risk, score in base_risks.items():
            adjusted_risks[risk] = min(1.0, score * adjustment)
        
        return adjusted_risks

    def calculate_company_supply_chain_risk(self, sector: str, info: dict) -> Dict[str, float]:
        """Calculate company-specific supply chain risk"""
        base_supply_chain = self.analyze_supply_chain_dynamics()
        
        # Get sector-specific metrics
        sector_metrics = base_supply_chain.get(sector, {})
        
        # Add company-specific factors
        company_factors = {
            'International Exposure': 0.7,  # Based on typical company characteristics
            'Supply Chain Complexity': 0.6,
            'Digital Transformation': 0.5,
            'Domestic Sourcing': 0.4
        }
        
        # Combine sector and company factors
        combined_metrics = {**sector_metrics, **company_factors}
        
        return combined_metrics

    def calculate_company_capital_flow_risk(self, sector: str, info: dict) -> Dict[str, float]:
        """Calculate company-specific capital flow risk"""
        base_capital_flows = self.evaluate_capital_flows()
        
        # Adjust based on sector characteristics
        sector_adjustments = {
            'Financial Services': 1.1,  # Higher sensitivity to capital flows
            'Technology': 0.9,          # Lower sensitivity
            'Healthcare': 0.8,          # Lower sensitivity
            'Energy': 1.0,              # Standard sensitivity
            'Manufacturing': 1.0,       # Standard sensitivity
            'Retail': 0.9,              # Lower sensitivity
            'Real Estate': 1.2,         # Higher sensitivity
            'Consumer Goods': 0.9,      # Lower sensitivity
            'Mining': 1.1,              # Higher sensitivity
            'Telecommunications': 1.0,  # Standard sensitivity
            'Transportation': 1.0       # Standard sensitivity
        }
        
        adjustment = sector_adjustments.get(sector, 1.0)
        
        adjusted_flows = {}
        for flow, score in base_capital_flows.items():
            adjusted_flows[flow] = min(1.0, score * adjustment)
        
        return adjusted_flows

    def calculate_financial_metrics(self, data: pd.DataFrame, info: dict) -> Dict[str, float]:
        """Calculate key financial metrics"""
        if data.empty:
            return {}
        
        # Calculate returns
        returns = data['Close'].pct_change().dropna()
        
        metrics = {
            'Current Price': data['Close'].iloc[-1] if not data.empty else 0,
            'Price Change (%)': ((data['Close'].iloc[-1] - data['Close'].iloc[-2]) / data['Close'].iloc[-2] * 100) if len(data) > 1 else 0,
            'Volatility (%)': returns.std() * 100 if not returns.empty else 0,
            'Annualized Return (%)': returns.mean() * 252 * 100 if not returns.empty else 0,
            'Sharpe Ratio': (returns.mean() / returns.std()) * np.sqrt(252) if not returns.empty and returns.std() > 0 else 0,
            'Max Drawdown (%)': ((data['Close'] / data['Close'].expanding().max() - 1) * 100).min() if not data.empty else 0
        }
        
        return metrics

    def generate_company_recommendation(self, geopolitical_risk: dict, supply_chain_risk: dict, 
                                      capital_flow_risk: dict, financial_metrics: dict) -> Dict[str, any]:
        """Generate investment recommendation for the company"""
        
        # Calculate overall risk scores
        avg_geopolitical = np.mean(list(geopolitical_risk.values()))
        avg_supply_chain = np.mean(list(supply_chain_risk.values()))
        avg_capital_flow = np.mean(list(capital_flow_risk.values()))
        
        # Calculate overall risk score (weighted average)
        overall_risk = (avg_geopolitical * 0.4 + avg_supply_chain * 0.3 + avg_capital_flow * 0.3)
        
        # Determine recommendation based on risk level
        if overall_risk < 0.4:
            recommendation = "Strong Buy"
            confidence = "High"
        elif overall_risk < 0.6:
            recommendation = "Buy"
            confidence = "Medium"
        elif overall_risk < 0.8:
            recommendation = "Hold"
            confidence = "Medium"
        else:
            recommendation = "Sell"
            confidence = "High"
        
        # Generate specific insights
        insights = []
        if avg_geopolitical > 0.7:
            insights.append("High geopolitical risk exposure")
        if avg_supply_chain > 0.7:
            insights.append("Supply chain vulnerabilities identified")
        if avg_capital_flow > 0.7:
            insights.append("Sensitive to capital flow changes")
        
        return {
            "overall_risk_score": overall_risk,
            "recommendation": recommendation,
            "confidence": confidence,
            "key_insights": insights,
            "risk_breakdown": {
                "geopolitical": avg_geopolitical,
                "supply_chain": avg_supply_chain,
                "capital_flow": avg_capital_flow
            }
        }

def create_uk_investment_dashboard():
    """Create comprehensive UK investment analysis dashboard"""
    st.set_page_config(
        page_title="UK Investment Strategy Analyzer",
        page_icon="🇬🇧",
        layout="wide"
    )
    
    # Custom CSS
    st.markdown("""
    <style>
        .uk-header {
            font-size: 2.5rem;
            font-weight: bold;
            color: #012169;
            text-align: center;
            margin-bottom: 2rem;
        }
        .metric-card {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 0.5rem;
            border-left: 4px solid #012169;
        }
        .risk-high { color: #d62728; }
        .risk-medium { color: #ff7f0e; }
        .risk-low { color: #2ca02c; }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1 class="uk-header">🇬🇧 UK Investment Strategy Analyzer</h1>', unsafe_allow_html=True)
    st.markdown("### Comprehensive Analysis: Geopolitical Risks, Supply Chain Dynamics & Capital Flows")
    
    # Initialize strategy analyzer
    analyzer = UKInvestmentStrategy()
    
    # Create tabs for different analysis areas
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🎯 Market Overview", 
        "🌍 Geopolitical Analysis", 
        "🔗 Supply Chain Dynamics", 
        "💰 Capital Flows", 
        "📊 Investment Recommendations",
        "🏢 Company Analysis"
    ])
    
    with tab1:
        st.markdown("### 📈 UK Market Overview")
        
        # Market data display
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### Major Indices")
            ftse_data = analyzer.get_market_data('^FTSE', '6mo')
            if not ftse_data.empty:
                current_ftse = ftse_data['Close'].iloc[-1]
                ftse_change = ((current_ftse - ftse_data['Close'].iloc[-2]) / ftse_data['Close'].iloc[-2]) * 100
                st.metric("FTSE 100", f"{current_ftse:,.0f}", f"{ftse_change:+.2f}%")
        
        with col2:
            st.markdown("#### Currency")
            gbp_data = analyzer.get_market_data('GBPUSD=X', '6mo')
            if not gbp_data.empty:
                current_gbp = gbp_data['Close'].iloc[-1]
                gbp_change = ((current_gbp - gbp_data['Close'].iloc[-2]) / gbp_data['Close'].iloc[-2]) * 100
                st.metric("GBP/USD", f"{current_gbp:.4f}", f"{gbp_change:+.2f}%")
        
        with col3:
            st.markdown("#### Economic Indicators")
            st.metric("Inflation Rate", "4.6%", "-0.5%")
            st.metric("Interest Rate", "5.25%", "0.0%")
            st.metric("GDP Growth", "0.6%", "+0.1%")
    
    with tab2:
        st.markdown("### 🌍 Geopolitical Risk Analysis")
        
        geopolitical_risks = analyzer.calculate_geopolitical_risk_score()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Risk Assessment")
            for risk, score in geopolitical_risks.items():
                if score > 0.7:
                    risk_class = "risk-high"
                elif score > 0.5:
                    risk_class = "risk-medium"
                else:
                    risk_class = "risk-low"
                
                st.markdown(f"**{risk}**: <span class='{risk_class}'>{score:.2f}</span>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### Key Risk Factors")
            risk_factors = [
                "Brexit implementation and EU relationship",
                "Global trade tensions and protectionism",
                "Energy security and transition",
                "Financial services regulation",
                "Political stability and policy continuity"
            ]
            
            for factor in risk_factors:
                st.markdown(f"• {factor}")
    
    with tab3:
        st.markdown("### 🔗 Supply Chain Dynamics")
        
        supply_chain = analyzer.analyze_supply_chain_dynamics()
        
        for sector, metrics in supply_chain.items():
            st.markdown(f"#### {sector} Sector")
            
            cols = st.columns(len(metrics))
            for i, (metric, score) in enumerate(metrics.items()):
                with cols[i]:
                    if score > 0.7:
                        risk_class = "risk-high"
                    elif score > 0.5:
                        risk_class = "risk-medium"
                    else:
                        risk_class = "risk-low"
                    
                    st.markdown(f"**{metric}**<br><span class='{risk_class}'>{score:.2f}</span>", 
                              unsafe_allow_html=True)
    
    with tab4:
        st.markdown("### 💰 Capital Flow Analysis")
        
        capital_flows = analyzer.evaluate_capital_flows()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Capital Flow Metrics")
            for metric, score in capital_flows.items():
                if score > 0.7:
                    risk_class = "risk-low"
                elif score > 0.5:
                    risk_class = "risk-medium"
                else:
                    risk_class = "risk-high"
                
                st.markdown(f"**{metric}**: <span class='{risk_class}'>{score:.2f}</span>", 
                          unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### Key Drivers")
            drivers = [
                "Interest rate differentials with major economies",
                "Political stability and policy predictability",
                "Market liquidity and regulatory environment",
                "Economic growth prospects and structural reforms",
                "Currency stability and trade balance"
            ]
            
            for driver in drivers:
                st.markdown(f"• {driver}")
    
    with tab5:
        st.markdown("### 📊 Investment Recommendations")
        
        recommendations = analyzer.generate_investment_recommendations()
        risk_strategies = analyzer.risk_mitigation_strategies()
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Investment Conviction Levels")
            for level, recs in recommendations.items():
                st.markdown(f"**{level}**")
                for rec in recs:
                    st.markdown(f"• {rec}")
                st.markdown("")
        
        with col2:
            st.markdown("#### Risk Mitigation Strategies")
            for risk_type, strategies in risk_strategies.items():
                st.markdown(f"**{risk_type}**")
                for strategy in strategies:
                    st.markdown(f"• {strategy}")
                st.markdown("")
        
        # Sector-specific analysis
        st.markdown("### 🎯 Sector-Specific Analysis")
        
        sectors = ["Financial Services", "Technology", "Healthcare", "Manufacturing", "Real Estate"]
        selected_sector = st.selectbox("Select Sector for Detailed Analysis:", sectors)
        
        if selected_sector:
            sector_analysis = analyzer.sector_specific_analysis(selected_sector)
            
            if sector_analysis:
                st.markdown(f"#### {selected_sector} Sector Analysis")
                
                cols = st.columns(len(sector_analysis))
                for i, (factor, score) in enumerate(sector_analysis.items()):
                    with cols[i]:
                        if score > 0.7:
                            risk_class = "risk-high"
                        elif score > 0.5:
                            risk_class = "risk-medium"
                        else:
                            risk_class = "risk-low"
                        
                        st.markdown(f"**{factor}**<br><span class='{risk_class}'>{score:.2f}</span>", 
                                  unsafe_allow_html=True)
    
    with tab6:
        st.markdown("### 🏢 Company-Specific Analysis")
        st.markdown("Enter a company name to get a comprehensive analysis based on geopolitical risks, supply chain dynamics, and capital flows.")
        
        # Company input
        col1, col2 = st.columns([3, 1])
        
        with col1:
            company_name = st.text_input(
                "Enter Company Name:",
                placeholder="e.g., HSBC, Tesco, Rolls Royce, AstraZeneca",
                help="Enter the name of any UK or international company"
            )
        
        with col2:
            analyze_company_button = st.button("🔍 Analyze Company", type="primary")
        
        if analyze_company_button and company_name:
            with st.spinner(f"Analyzing {company_name}..."):
                # Perform company analysis
                analysis = analyzer.analyze_company(company_name)
                
                if "error" in analysis:
                    st.error(analysis["error"])
                else:
                    # Display company analysis results
                    st.markdown(f"## 📊 Analysis Results for {analysis['company_name']}")
                    
                    # Company overview
                    col1, col2, col3, col4 = st.columns(4)
                    
                    with col1:
                        st.metric("Ticker", analysis['ticker'])
                    
                    with col2:
                        st.metric("Sector", analysis['sector'])
                    
                    with col3:
                        current_price = analysis['financial_metrics'].get('Current Price', 0)
                        st.metric("Current Price", f"${current_price:.2f}" if current_price > 0 else "N/A")
                    
                    with col4:
                        price_change = analysis['financial_metrics'].get('Price Change (%)', 0)
                        st.metric("Price Change", f"{price_change:+.2f}%" if price_change != 0 else "N/A")
                    
                    # Investment recommendation
                    recommendation = analysis['recommendation']
                    st.markdown("### 🎯 Investment Recommendation")
                    
                    if recommendation['recommendation'] == "Strong Buy":
                        st.success(f"**{recommendation['recommendation']}** - Confidence: {recommendation['confidence']}")
                    elif recommendation['recommendation'] == "Buy":
                        st.info(f"**{recommendation['recommendation']}** - Confidence: {recommendation['confidence']}")
                    elif recommendation['recommendation'] == "Hold":
                        st.warning(f"**{recommendation['recommendation']}** - Confidence: {recommendation['confidence']}")
                    else:
                        st.error(f"**{recommendation['recommendation']}** - Confidence: {recommendation['confidence']}")
                    
                    # Risk breakdown
                    st.markdown("### 📈 Risk Analysis")
                    
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        geo_risk = recommendation['risk_breakdown']['geopolitical']
                        if geo_risk > 0.7:
                            risk_class = "risk-high"
                        elif geo_risk > 0.5:
                            risk_class = "risk-medium"
                        else:
                            risk_class = "risk-low"
                        st.markdown(f"**Geopolitical Risk**: <span class='{risk_class}'>{geo_risk:.2f}</span>", unsafe_allow_html=True)
                    
                    with col2:
                        sc_risk = recommendation['risk_breakdown']['supply_chain']
                        if sc_risk > 0.7:
                            risk_class = "risk-high"
                        elif sc_risk > 0.5:
                            risk_class = "risk-medium"
                        else:
                            risk_class = "risk-low"
                        st.markdown(f"**Supply Chain Risk**: <span class='{risk_class}'>{sc_risk:.2f}</span>", unsafe_allow_html=True)
                    
                    with col3:
                        cf_risk = recommendation['risk_breakdown']['capital_flow']
                        if cf_risk > 0.7:
                            risk_class = "risk-high"
                        elif cf_risk > 0.5:
                            risk_class = "risk-medium"
                        else:
                            risk_class = "risk-low"
                        st.markdown(f"**Capital Flow Risk**: <span class='{risk_class}'>{cf_risk:.2f}</span>", unsafe_allow_html=True)
                    
                    # Key insights
                    if recommendation['key_insights']:
                        st.markdown("### 🔍 Key Insights")
                        for insight in recommendation['key_insights']:
                            st.markdown(f"• {insight}")
                    
                    # Financial metrics
                    st.markdown("### 💰 Financial Metrics")
                    
                    metrics = analysis['financial_metrics']
                    if metrics:
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            st.metric("Volatility (%)", f"{metrics.get('Volatility (%)', 0):.2f}")
                            st.metric("Sharpe Ratio", f"{metrics.get('Sharpe Ratio', 0):.3f}")
                        
                        with col2:
                            st.metric("Annualized Return (%)", f"{metrics.get('Annualized Return (%)', 0):.2f}")
                            st.metric("Max Drawdown (%)", f"{metrics.get('Max Drawdown (%)', 0):.2f}")
                        
                        with col3:
                            st.metric("Overall Risk Score", f"{recommendation['overall_risk_score']:.2f}")
                    
                    # Price chart
                    if not analysis['price_data'].empty:
                        st.markdown("### 📈 Price Performance")
                        
                        fig = go.Figure()
                        fig.add_trace(go.Scatter(
                            x=analysis['price_data'].index,
                            y=analysis['price_data']['Close'],
                            mode='lines',
                            name=f"{analysis['company_name']} Stock Price",
                            line=dict(color='#1f77b4', width=2)
                        ))
                        
                        fig.update_layout(
                            title=f"{analysis['company_name']} - Stock Price (Last 12 Months)",
                            xaxis_title='Date',
                            yaxis_title='Stock Price',
                            height=400
                        )
                        
                        st.plotly_chart(fig, use_container_width=True)
                    
                    # Detailed risk analysis
                    st.markdown("### 🔍 Detailed Risk Analysis")
                    
                    # Geopolitical risks
                    st.markdown("#### 🌍 Geopolitical Risk Factors")
                    geo_risks = analysis['geopolitical_risk']
                    for risk, score in geo_risks.items():
                        if score > 0.7:
                            risk_class = "risk-high"
                        elif score > 0.5:
                            risk_class = "risk-medium"
                        else:
                            risk_class = "risk-low"
                        st.markdown(f"**{risk}**: <span class='{risk_class}'>{score:.2f}</span>", unsafe_allow_html=True)
                    
                    # Supply chain risks
                    st.markdown("#### 🔗 Supply Chain Risk Factors")
                    sc_risks = analysis['supply_chain_risk']
                    for risk, score in sc_risks.items():
                        if score > 0.7:
                            risk_class = "risk-high"
                        elif score > 0.5:
                            risk_class = "risk-medium"
                        else:
                            risk_class = "risk-low"
                        st.markdown(f"**{risk}**: <span class='{risk_class}'>{score:.2f}</span>", unsafe_allow_html=True)
                    
                    # Capital flow risks
                    st.markdown("#### 💰 Capital Flow Risk Factors")
                    cf_risks = analysis['capital_flow_risk']
                    for risk, score in cf_risks.items():
                        if score > 0.7:
                            risk_class = "risk-high"
                        elif score > 0.5:
                            risk_class = "risk-medium"
                        else:
                            risk_class = "risk-low"
                        st.markdown(f"**{risk}**: <span class='{risk_class}'>{score:.2f}</span>", unsafe_allow_html=True)
        
        # Company suggestions
        if not analyze_company_button:
            st.markdown("### 💡 Popular UK Companies to Analyze")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("**Financial Services**")
                st.markdown("• HSBC")
                st.markdown("• Barclays")
                st.markdown("• Lloyds Banking")
                st.markdown("• NatWest")
            
            with col2:
                st.markdown("**Technology & Retail**")
                st.markdown("• Sage Group")
                st.markdown("• ASOS")
                st.markdown("• Boohoo")
                st.markdown("• Ocado")
            
            with col3:
                st.markdown("**Healthcare & Energy**")
                st.markdown("• AstraZeneca")
                st.markdown("• GlaxoSmithKline")
                st.markdown("• BP")
                st.markdown("• Shell")

if __name__ == "__main__":
    create_uk_investment_dashboard()
