#!/usr/bin/env python3
"""
UK Investment Strategy Dashboard Launcher

This script launches the comprehensive UK investment evaluation dashboard
that analyzes geopolitical risks, supply chain dynamics, and capital flows.
"""

import subprocess
import sys
import os

def main():
    """Launch the UK Investment Strategy Dashboard"""
    
    print("🇬🇧 UK Investment Strategy Dashboard")
    print("=" * 50)
    print("Launching comprehensive UK investment analysis...")
    print("This dashboard includes:")
    print("• Geopolitical risk assessment")
    print("• Supply chain dynamics analysis") 
    print("• International capital flows evaluation")
    print("• Sector-specific investment recommendations")
    print("• Risk mitigation strategies")
    print("=" * 50)
    
    try:
        # Check if required packages are installed
        import streamlit
        import yfinance
        import pandas
        import numpy
        import plotly
        
        # Launch the dashboard
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            "uk_investment_strategy.py",
            "--server.port", "8501",
            "--server.headless", "true"
        ])
        
    except ImportError as e:
        print(f"❌ Missing required package: {e}")
        print("Please install required packages using:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error launching dashboard: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
