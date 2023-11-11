import streamlit as st
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Load the trained model
model = joblib.load("App Development\Best_random_forest_model.joblib")

def main():
    st.title("Customer Churn Prediction")

    # Input fields
    Age = st.number_input("Age", min_value=1, max_value=120, step=1)
    gender = st.selectbox("Gender", ["Male", "Female"])
    location = st.selectbox("Location", ["Houston", "Los Angeles", "Miami", "Chicago", "New York"])
    Subscription_Length_Months = st.number_input("Subscription Length (Months)", min_value=1, step=1)
    Monthly_Bill = st.number_input("Monthly Bill", min_value=0.0, step=10.0)
    Total_Usage_GB = st.number_input("Total Usage (GB)", min_value=0.0, step=1.0)

    # Convert categorical features to numerical using encoding
    Gender_Male = 1 if gender == "Male" else 0
    Location_Houston = Location_Los_Angeles	= Location_Miami = Location_New_York = 0

    if location == "Houston":
      Location_Houston = 1
    elif location == "Los Angeles":
      Location_Los_Angeles = 1
    elif location == "Miami":
      Location_Miami = 1
    elif location == "New York":
      Location_New_York = 1

    # Predict button
    if st.button("Predict"):      
        scaler = StandardScaler()    
        input_data = np.array([[Age, Subscription_Length_Months,	Monthly_Bill,	Total_Usage_GB,	Gender_Male,	Location_Houston,	Location_Los_Angeles,	Location_Miami,	Location_New_York]])
        scaled_data = scaler.fit_transform([input_data[0][1:4]])
        input_data[0][1:4] = scaled_data[0]
        print(input_data)
        prediction = model.predict(input_data)
        if prediction[0] == 0:
            st.write("Prediction: Customer will not churn!!")
        else:
            st.write("Prediction: Customer will churn!!")

if __name__ == "__main__":
    main()
