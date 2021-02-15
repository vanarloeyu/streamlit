import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""

# Simple Stock Price App

Shown are the stock closing price and volume of Tesla Inc!


""")

tickerSymbol = 'TSLA'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='id', start='2010-5-31', end='2020-5-31')

st.write("""
## Closing Prices
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
