import yfinance as yf
import streamlit as st
import pandas as pd

import plotly.graph_objects as go


st.write("""

# Simple TS Chart App


""")
df = pd.read_excel('dataset.xlsx')

color_dict = {}
for i, trt in enumerate(df['Treatment'].unique()):
	st.sidebar.header(trt)
	color_dict[i] = st.sidebar.color_picker('Pick A Color', '#00f900', key=i)
colors = [v for k,v in color_dict.items()]

fig = go.Figure(data=[go.Bar(
    x=df['Treatment'],
    y=df['Value'],
    marker_color=colors # marker color can be a single color value or an iterable
)])
fig.update_layout(xaxis={'categoryorder':'total descending'})
st.plotly_chart(fig)
st.write(df)
