import streamlit as st
import pandas as pd
import pickle

# Load model
with open("swiggy_delivery_time_rf.pkl", "rb") as f:
    model = pickle.load(f)

# Load feature list
with open("final_features.pkl", "rb") as f:
    final_features = pickle.load(f)

st.set_page_config(page_title="Swiggy Delivery Time Prediction", layout="centered")

st.title("🚴 Swiggy Delivery Time Prediction")
st.write("Predict delivery time (in minutes) using a trained Random Forest model.")

st.header("Enter Order Details")

# User Inputs (MATCH FINAL FEATURES)
age = st.number_input("Rider Age", min_value=18, max_value=60, value=25)
ratings = st.slider("Rider Rating", 1.0, 5.0, 4.5)
vehicle_condition = st.selectbox("Vehicle Condition (0=Poor,1=Avg,2=Good)", [0,1,2])
multiple_deliveries = st.number_input("Multiple Deliveries", min_value=0, max_value=5, value=1)
distance = st.number_input("Distance (km)", min_value=0.5, max_value=50.0, value=5.0)
traffic = st.selectbox("Traffic Level (0=Low,1=Medium,2=High,3=Jam)", [0,1,2,3])
festival_yes = st.selectbox("Festival Day?", [0,1])
order_time_hour = st.slider("Order Time Hour", 0, 23, 12)
order_time_of_day_morning = st.selectbox("Is Morning Order?", [0,1])
weather_sunny = st.selectbox("Is Weather Sunny?", [0,1])
city_type_urban = st.selectbox("Is Urban City?", [0,1])

# Create input dataframe
input_data = pd.DataFrame([[
    age,
    ratings,
    vehicle_condition,
    multiple_deliveries,
    distance,
    traffic,
    festival_yes,
    order_time_hour,
    order_time_of_day_morning,
    weather_sunny,
    city_type_urban
]], columns=final_features)

if st.button("Predict Delivery Time"):
    prediction = model.predict(input_data)[0]
    st.success(f"🕒 Estimated Delivery Time: **{round(prediction, 2)} minutes**")
