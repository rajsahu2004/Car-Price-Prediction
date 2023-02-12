import numpy as np
import pickle
import streamlit as st

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

def predict_default(features):
    # Convert features to numpy array
    features = np.array(features).astype(np.float64).reshape(1, -1)
    # Predict
    prediction = model.predict(features)
    return prediction
# Car_Name,Year,Selling_Price,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner
def main():
    Car_Name = st.text_input("Car_Name")
    Year = st.number_input("Year")
    Selling_Price = st.number_input("Selling_Price")
    Present_Price = st.number_input("Present_Price")
    Kms_Driven = st.number_input("Kms_Driven")
    Fuel_Type = st.number_input("Fuel_Type")
    Seller_Type = st.number_input("Seller_Type")
    Transmission = st.number_input("Transmission")
    Owner = st.number_input("Owner")
    diagnosis = ''
    if st.button('Predict'):
        diagnosis = predict_default([Car_Name,Year,Selling_Price,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner])
    st.success(diagnosis)

if __name__ == '__main__':
    main()