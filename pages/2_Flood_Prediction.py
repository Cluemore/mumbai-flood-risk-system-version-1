import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.title("🌧 Area-Based Flood Risk Prediction")

# Load model
@st.cache_resource
def load_model():
    with open("flood_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# Load dataset
df = pd.read_excel("mumbai_flood_ml_dataset_final.xlsx")
df.columns = df.columns.str.strip()

areas = sorted(df["Area"].unique())
selected_area = st.selectbox("Select Area", areas)

if st.button("Predict Flood Risk"):

    area_data = df[df["Area"] == selected_area].iloc[0]

    features = area_data.drop(["ID", "Area", "Flood_Severity_Index_0to10"]).values.reshape(1, -1)

    prediction = model.predict(features)[0]
    prediction = round(min(max(prediction, 0), 10), 2)

    st.metric("Predicted Flood Severity (0-10)", prediction)

    if prediction < 3:
        st.success("🟢 Low Risk")
    elif prediction < 6:
        st.warning("🟡 Moderate Risk")
    elif prediction < 8:
        st.error("🟠 High Risk")
    else:
        st.error("🔴 Very High Risk")

    st.subheader("Area Parameters Used")
    st.dataframe(area_data)