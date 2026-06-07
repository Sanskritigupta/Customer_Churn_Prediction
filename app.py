import streamlit as st
import pandas as pd
import joblib

model = joblib.load("best_churn_pipeline.pkl")

st.title("Customer Churn Prediction")

credit_score = st.number_input("Credit Score", 300, 900, 650)
age = st.number_input("Age", 18, 100, 35)
tenure = st.number_input("Tenure", 0, 10, 5)
balance = st.number_input("Balance", 0.0, 300000.0, 50000.0)
products_number = st.number_input("Products Number", 1, 4, 1)
estimated_salary = st.number_input("Estimated Salary", 0.0, 300000.0, 50000.0)

country = st.selectbox("Country", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Male", "Female"])
credit_card = st.selectbox("Credit Card", [0, 1])
active_member = st.selectbox("Active Member", [0, 1])

balance_per_product = balance / max(products_number, 1)
salary_balance_ratio = estimated_salary / (balance + 1)

if age < 30:
    age_group = "Young"
elif age < 50:
    age_group = "Middle"
else:
    age_group = "Senior"

if tenure <= 3:
    tenure_bucket = "Low"
elif tenure <= 7:
    tenure_bucket = "Medium"
else:
    tenure_bucket = "High"

high_balance = "Yes" if balance > 100000 else "No"

data = pd.DataFrame({
    "credit_score": [credit_score],
    "age": [age],
    "tenure": [tenure],
    "balance": [balance],
    "products_number": [products_number],
    "estimated_salary": [estimated_salary],
    "balance_per_product": [balance_per_product],
    "salary_balance_ratio": [salary_balance_ratio],
    "country": [country],
    "gender": [gender],
    "credit_card": [credit_card],
    "active_member": [active_member],
    "age_group": [age_group],
    "tenure_bucket": [tenure_bucket],
    "high_balance": [high_balance]
})

if st.button("Predict"):
    prediction = model.predict(data)[0]

    if prediction == 1:
        st.error("Customer is likely to Churn")
    else:
        st.success("Customer is likely to Stay")
st.markdown("---")
st.caption("Created by Sanskriti Gupta")
