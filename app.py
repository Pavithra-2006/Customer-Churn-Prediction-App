import streamlit as st
import pandas as pd
import joblib
import numpy as np

# -----------------------------
# Load pipeline and feature columns
# -----------------------------
pipeline = joblib.load("churn_pipeline.pkl")  # Your trained pipeline
feature_columns = joblib.load("feature_columns.pkl")  # Feature order saved during training

# -----------------------------
# Streamlit UI config
# -----------------------------
st.set_page_config(page_title="Customer Churn Predictor", layout="wide")
st.title("📉 Customer Churn Prediction App")
st.write("Predict whether a customer is likely to churn")

st.markdown("""
**Instructions:**  
- Binary fields: `0 = No`, `1 = Yes`  
- Numeric fields: Enter the actual values
""")

# -----------------------------
# Numeric Inputs Section
# -----------------------------
with st.expander("📊 Numeric Fields", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        AccountAge = st.number_input("Account Age (months)", min_value=0)
        TotalCharges = st.number_input("Total Charges", min_value=0.0)
        ViewingHoursPerWeek = st.number_input("Viewing Hours per Week", min_value=0.0)
        WatchlistSize = st.number_input("Watchlist Size", min_value=0)
        UserRating = st.number_input("User Rating (0-5)", min_value=0, max_value=5)
    with col2:
        MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0)
        AverageViewingDuration = st.number_input("Average Viewing Duration (minutes)", min_value=0.0)
        ContentDownloadsPerMonth = st.number_input("Content Downloads per Month", min_value=0)
        SupportTicketsPerMonth = st.number_input("Support Tickets per Month", min_value=0)
    with col3:
        # Add any additional numeric fields if needed
        pass

# -----------------------------
# Categorical / Binary Inputs Section
# -----------------------------
with st.expander("✅ Categorical / Binary Fields", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        SubscriptionType = st.selectbox("Month-to-month Subscription?", [0, 1])
        PaymentMethod = st.selectbox("Manual Payment?", [0, 1])
        PaperlessBilling = st.selectbox("Paperless Billing?", [0, 1])
        MultiDeviceAccess = st.selectbox("Multi Device Access?", [0, 1])
    with col2:
        ContentType = st.selectbox("Content Type: Movies?", [0, 1])
        DeviceRegistered = st.selectbox("Device Registered: Mobile?", [0, 1])
        GenrePreference = st.selectbox("Genre Preference: Action?", [0, 1])
        Gender = st.selectbox("Gender: Male?", [0, 1])
    with col3:
        ParentalControl = st.selectbox("Parental Control Enabled?", [0, 1])
        SubtitlesEnabled = st.selectbox("Subtitles Enabled?", [0, 1])

# -----------------------------
# Collect inputs into DataFrame
# -----------------------------
user_input = {
    "AccountAge": AccountAge,
    "MonthlyCharges": MonthlyCharges,
    "TotalCharges": TotalCharges,
    "SubscriptionType": SubscriptionType,
    "PaymentMethod": PaymentMethod,
    "PaperlessBilling": PaperlessBilling,
    "ContentType": ContentType,
    "MultiDeviceAccess": MultiDeviceAccess,
    "DeviceRegistered": DeviceRegistered,
    "ViewingHoursPerWeek": ViewingHoursPerWeek,
    "AverageViewingDuration": AverageViewingDuration,
    "ContentDownloadsPerMonth": ContentDownloadsPerMonth,
    "GenrePreference": GenrePreference,
    "UserRating": UserRating,
    "SupportTicketsPerMonth": SupportTicketsPerMonth,
    "Gender": Gender,
    "WatchlistSize": WatchlistSize,
    "ParentalControl": ParentalControl,
    "SubtitlesEnabled": SubtitlesEnabled,
}

input_data = pd.DataFrame([user_input])

# -----------------------------
# Fill missing columns
# -----------------------------
for col in feature_columns:
    if col not in input_data.columns:
        input_data[col] = 0  # Fill missing columns with 0

# Reorder columns to match training
input_data = input_data[feature_columns]

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict Churn", type="primary"):
    prediction = pipeline.predict(input_data)[0]
    probability = pipeline.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Customer likely to churn\nProbability: {probability:.2f}")
    else:
        st.success(f"✅ Customer likely to stay\nProbability: {probability:.2f}")
