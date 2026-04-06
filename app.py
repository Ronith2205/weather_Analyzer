import streamlit as st
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🌦️ Weather Prediction System")

# Inputs
temp_max = st.number_input("Max Temperature", value=20.0)
temp_min = st.number_input("Min Temperature", value=10.0)
precip = st.number_input("Precipitation", value=0.0)
wind = st.number_input("Wind Speed", value=5.0)

# Prediction
if st.button("Predict Weather"):
    result = model.predict([[precip, temp_max, temp_min, wind]])
    st.success(f"🌤️ Weather: {result[0]}")