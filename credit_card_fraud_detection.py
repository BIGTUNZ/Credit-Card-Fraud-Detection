

# Import necessary libraries
import streamlit as st
import pandas as pd
import joblib


# Title for the web app
st.title('Credit Card Fraud Detection')

# Load the trained model
model = joblib.load("credit_card_model.pkl")  

# Input features from the user
st.header('Input Features')

# Feature sliders with appropriate ranges based on your dataset
v11 = st.slider('V11', min_value=-20.0, max_value=20.0, value=0.0, step=0.1)
v4 = st.slider('V4', min_value=-20.0, max_value=20.0, value=0.0, step=0.1)
v2 = st.slider('V2', min_value=-20.0, max_value=20.0, value=0.0, step=0.1)
v17 = st.slider('V17', min_value=-20.0, max_value=20.0, value=0.0, step=0.1)
v14 = st.slider('V14', min_value=-20.0, max_value=20.0, value=0.0, step=0.1)
v12 = st.slider('V12', min_value=-20.0, max_value=20.0, value=0.0, step=0.1)
v10 = st.slider('V10', min_value=-20.0, max_value=20.0, value=0.0, step=0.1)

# Create a dictionary for the model input
input_data = {
    'V11': [v11],
    'V4': [v4],
    'V3': [v3],
    'V17': [v17],
    'V14': [v14],
    'V12': [v12],
    'V10': [v10]
}


# Convert input data to dataframe
input_df = pd.DataFrame(input_data)

# Display the input data
st.subheader('Input Data')
st.write(input_df)

# Prediction
if st.button('Predict'):
    prediction = model.predict(input_df)
    prediction_prob = model.predict_proba(input_df)
    
if prediction[0] == 1: 
    st.success(f"The model predicts that this is a Fraud {prediction_prob[0][1] * 100:.2f}% probability.")
else:
    st.error(f"The model predicts that this is not a fraud {prediction_prob[0][0] * 100:.2f}% probability.")

