
import streamlit as st
import pickle
import pandas as pd

# Load the saved model and encoders
with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('item_encoder.pkl', 'rb') as f:
    item_encoder = pickle.load(f)

with open('area_encoder.pkl', 'rb') as f:
    area_encoder = pickle.load(f)

st.set_page_config(page_title="Crop Production Prediction", page_icon="🌾")
st.title("🌾 Crop Production Prediction App")
st.markdown("Predict the **total crop production (tons)** based on Crop, Region, Year, Area harvested, and Yield.")

# Input selections
item_list = list(item_encoder.classes_)
area_list = list(area_encoder.classes_)

selected_item = st.selectbox("Select Crop (Item):", item_list)
selected_area = st.selectbox("Select Region (Area):", area_list)
selected_year = st.number_input("Enter Year:", min_value=1960, max_value=2050, step=1, value=2020)
area_harvested = st.number_input("Enter Area Harvested (hectares):", min_value=0.0, value=10000.0)
yield_value = st.number_input("Enter Yield (kg/ha):", min_value=0.0, value=1500.0)

# Prediction button
if st.button("Predict Production"):
    # Encode categorical values
    encoded_item = item_encoder.transform([selected_item])[0]
    encoded_area = area_encoder.transform([selected_area])[0]

    # Prepare input
    input_data = pd.DataFrame({
        'Item_encoded': [encoded_item],
        'Area_encoded': [encoded_area],
        'Year': [selected_year],
        'Area harvested': [area_harvested],
        'Yield': [yield_value]
    })

    # Make prediction
    predicted_production = model.predict(input_data)[0]
    st.success(f"🌱 Predicted Production for **{selected_item}** in **{selected_area}** ({selected_year}): **{predicted_production:.2f} tons**")

st.sidebar.markdown("---")
st.sidebar.write("✅ Developed by Tanishq (Capstone Project)")
