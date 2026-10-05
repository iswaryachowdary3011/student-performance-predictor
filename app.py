import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Page title
st.title("🎓 Student Performance Predictor")
st.write("Enter the student's details to predict their performance.")

# User inputs
study_hours = st.number_input(
    "Study Hours per Day",
    min_value=0.0,
    max_value=12.0,
    value=4.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=75
)

previous_marks = st.number_input(
    "Previous Marks (%)",
    min_value=0,
    max_value=100,
    value=65
)

assignment_score = st.number_input(
    "Assignment Score (%)",
    min_value=0,
    max_value=100,
    value=70
)

# Prediction button
if st.button("Predict Performance"):

    input_data = pd.DataFrame({
        "study_hours": [study_hours],
        "attendance": [attendance],
        "previous_marks": [previous_marks],
        "assignment_score": [assignment_score]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Performance: **{prediction}**")