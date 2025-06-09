import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

st.title("🏠 Property Price Prediction")

# Input fields
area = st.number_input("Area (in sqft)", min_value=200)
bhk = st.selectbox("Number of BHK", [1, 2, 3, 4, 5])
bathroom = st.selectbox("Number of Bathrooms", [1, 2, 3, 4])
parking = st.selectbox("Parking Slots", [0, 1, 2, 3])

status = st.selectbox("Status", ["Almost Ready", "Ready to Move"])
furnishing = st.selectbox("Furnishing", ["Furnished", "Semi-Furnished", "Unfurnished"])
transaction = st.selectbox("Transaction", ["New Property", "Resale"])
property_type = st.selectbox("Type", ["Apartment", "Builder Floor"])

# One-hot encoding for categories
status_list = [1, 0] if status == "Almost Ready" else [0, 1]
furnish_list = {
    "Furnished": [1, 0, 0],
    "Semi-Furnished": [0, 1, 0],
    "Unfurnished": [0, 0, 1]
}[furnishing]
transaction_list = [1, 0] if transaction == "New Property" else [0, 1]
type_list = [1, 0] if property_type == "Apartment" else [0, 1]

if st.button("Predict"):
    input_data = [[area, bhk, bathroom, parking] + status_list + furnish_list + transaction_list + type_list]
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Property Price: ₹{round(prediction):,}")
