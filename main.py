import streamlit as st
import plotly.express as px
from backend import get_data


st.title("Weather Forcast for the next 5 days")
place = st.text_input("Enter any place: ")
days = st.slider("Forcast days", min_value=1,
                 max_value=5,
                 help='Select the number of forcasted days')
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky view"))
st.subheader(f"{option} for the next {days} days in {place}")

data = get_data(place, days, option)


d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "Date",
                                   "y": "Temperature (C)"})
st.plotly_chart(figure)