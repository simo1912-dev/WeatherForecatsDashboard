import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for te next Days")
place = st.text_input("Place:")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"Forecast of {option} for the next {days} days in  {place}")

d, t = get_data(place, days, option)


figure = px.line(x=dates, y=temperatures, labels=dict(x="Date", y="Temperature"))
st.plotly_chart(figure)