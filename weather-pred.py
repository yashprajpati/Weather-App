import numpy as np
import pickle
import streamlit as st

# Load trained model
loaded_model = pickle.load(open('D:/Internship/Weather APP/weather.sav', 'rb'))

def weather_prediction(input_data):
    input_data_as_array = np.asarray(input_data, dtype=float)
    input_data_reshaped = input_data_as_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 1:
        return 'Rainy'
    elif prediction[0] == 0:
        return 'Cloudy'
    elif prediction[0] == 3:
        return 'Sunny'
    else:
        return 'Snowy'

def main():
    st.title("Weather Data Prediction App")

    temperature = st.text_input("Temperature (°C)")
    humidity = st.text_input("Humidity (%)")
    wind_speed = st.text_input("Wind Speed (km/h)")
    precipitation = st.text_input("Precipitation (%)")
    cloud_cover = st.text_input("Cloud Cover (0=overcast, 1=partly cloudy, 2=clear, 3=cloudy)")
    pressure = st.text_input("Atmospheric Pressure (hPa)")
    uv_index = st.text_input("UV Index")
    season_val = st.text_input("Season (0=Winter, 1=Spring, 2=Autumn, 3=Summer)")
    visibility = st.text_input("Visibility (km)")
    location_val = st.text_input("Location (0=inland, 1=mountain, 2=coastal)")

    if st.button("Result of Weather Prediction"):
        try:
            input_list = [
                float(temperature),
                float(humidity),
                float(wind_speed),
                float(precipitation),
                float(cloud_cover),
                float(pressure),
                float(uv_index),
                float(season_val),
                float(visibility),
                float(location_val),
            ]


            prediction = weather_prediction(input_list)
            st.success(f"Weather prediction result: {prediction}")

        except ValueError:
            st.error("❗ Please enter valid numeric values in all fields.")

if __name__== "__main__":
    main()