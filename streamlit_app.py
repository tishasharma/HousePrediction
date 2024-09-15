import streamlit as st
import requests

# Title of the app
st.title("Bangalore Home Price Prediction")

# Input fields
location = st.text_input("Enter Location")
total_sqft = st.number_input("Enter Total Square Feet", min_value=500, max_value=10000, step=100)
bath = st.number_input("Enter Number of Bathrooms", min_value=1, max_value=10, step=1)
bhk = st.number_input("Enter Number of Bedrooms", min_value=1, max_value=10, step=1)

# When the user clicks 'Predict' button
if st.button("Predict Price"):
    # Prepare input data for the Flask API
    input_data = {
        'location': location,
        'total_sqft': total_sqft,
        'bath': bath,
        'bhk': bhk
    }
    
    # Send request to the Flask API
    url = 'http://127.0.0.1:5000/predict_home_price'
    response = requests.post(url, json=input_data)
    
    # Get the predicted price from the response
    if response.ok:
        prediction = response.json()['predicted_price']
        st.write(f"The predicted price of the house is ₹ {prediction:.2f} lakh")
    else:
        st.write("Error: Could not fetch prediction. Please try again.")

# Run this Streamlit app with: streamlit run app.py
