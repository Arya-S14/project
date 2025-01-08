import streamlit as st # type: ignore
from getrequest import get_weather_data

st.title("API Calling")
city=st.text_input("Enter  city")
weather_data=get_weather_data(city=city)

if(weather_data):
    st.subheader("Weather Description")
    st.write(weather_data['weather'][0]['description'])
    st.write(weather_data['main']['temp'])
