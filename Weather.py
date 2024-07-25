import streamlit as st
import pandas as pd
import pickle

st.image(r"C:\Users\reddy\OneDrive\Desktop\new logo.jpg")
## Loading the trained model
with open(r"model.pkl","rb") as file:
    model = pickle.load(file)

#Defining the Input fileds
st.title("WEATHER PREDICTION")

Temperature1 = st.number_input("Enter the temparature in CELCIUS)",min_value=2.5,max_value=32.5,step = 2.0)
Humidity = st.number_input("Enter the HUMIDITY(%)",min_value=20.0,max_value=109.0,step = 5.0)
Precipitation = st.number_input("Enter the PRECIPITATION(%)",min_value=0.0,max_value= 109.0,step = 5.0)
Cloud_Cover = st.radio("Enter the ColudCover",['partly cloudy', 'clear', 'overcast', 'cloudy'])
UV_Index = st.number_input("Enter the UV INDEX",min_value=0.0, max_value=14.0,step = 1.0)
Season = st.radio("Enter the SEASONS",['Winter', 'Spring', 'Summer', 'Autumn'])
Visibility = st.number_input("Enter the VISIBILITY(KM)",min_value=2.0,max_value= 8.0,step = 1.0)
Location = st.radio("Enter the LOCATION",['inland', 'mountain', 'coastal'])
Wind_Speed = st.number_input("Enter the WIND_SPEED",min_value=4.0,max_value=8.0)
Atmospheric_Pressure = st.number_input("Enter the ATMOSHERIC_PRESSURE",min_value=900.0,max_value=1020.0,step = 5.0)

# Creating The Data Frame from the input
input_data = pd.DataFrame({
    "Temperature":[Temperature1],
    "Humidity" :[Humidity],
    "Precipitation (%)":[Precipitation],
    "Cloud Cover":[Cloud_Cover],
    "UV Index":[UV_Index],
    "Season":[Season],
    "Visibility (km)":[Visibility],
    "Location":[Location],
    "Wind Speed":[Wind_Speed],
    "Atmospheric Pressure":[Atmospheric_Pressure]
    })


# Displaying the input Data
st.write("Input data:")
st.write(input_data)

# Making the prediction
if st.button("Predict Weather Type"):
    prediction = model.predict(input_data)
    st.write("Predicted Weather Type:",prediction[0])

    if True:
        if prediction[0]== "Rainy":
            st.image(r"C:\Users\reddy\OneDrive\Desktop\raining.jpg")
        elif prediction[0]=="Cloudy":
            st.image(r"C:\Users\reddy\OneDrive\Desktop\cloudy.png")
        elif prediction[0]=="Sunny":
            st.image(r"C:\Users\reddy\OneDrive\Desktop\sunny.jpg")
        else:
            st.image(r"C:\Users\reddy\OneDrive\Desktop\snowy.jpg")




