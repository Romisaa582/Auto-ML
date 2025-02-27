import streamlit as st
import pandas as pd

st.title("🧠 Alzheimer's Disease Prediction")

# Sample dataset
sample_data = {
    "Age": [65, 70, 75, 80, 85],
    "BMI": [22.5, 24.3, 26.1, 27.8, 29.5],
    "PhysicalActivity": [3, 2, 1, 2, 0],
    "MemoryComplaints": [1, 2, 3, 4, 5],
    "Forgetfulness": [2, 3, 4, 5, 5],
    "Diagnosis": [0, 0, 1, 1, 1]
}

df = pd.DataFrame(sample_data)

st.write("### Sample Data Preview:")
st.dataframe(df)

# User input for prediction simulation
st.write("### Enter Patient Data for Prediction")
input_data = {}
cols = st.columns(len(df.columns) - 1)  # Create columns for input fields

for i, col in enumerate(df.columns[:-1]):  # Exclude Diagnosis
    col_mean = float(df[col].mean())
    with cols[i]:
        input_data[col] = st.number_input(f"{col}\n(Mean: {col_mean})", value=col_mean)

if st.button("Predict"):
    # Simple threshold-based prediction (placeholder)
    risk_score = sum(input_data.values()) / len(input_data)  # Average of inputs
    diagnosis = "Alzheimer" if risk_score > df['Diagnosis'].mean() else "No Alzheimer"
    st.write(f"## Prediction: {diagnosis}")
