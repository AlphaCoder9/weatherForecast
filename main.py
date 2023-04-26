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

if place:

    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperature = [dict['main']['temp'] for dict in filtered_data]
        dates = [dict['dt_txt'] for dict in filtered_data]
        figure = px.line(x=dates, y=temperature, labels={"x": "Date",
                                   "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky view":
        images = {"Clear": "images/clear.png",
                  "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png",
                  "Snow": "images/snow.png"}
        sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
        images_paths = [images[condition] for condition in sky_conditions]
        print(sky_conditions)
        st.image(images_paths, width=115)

