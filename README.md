# Student Performance Predictor

A simple machine learning project that predicts student performance based on a few academic and study-related factors.

## About the Project

This project uses a Decision Tree Classifier to predict student performance using:

- Study hours per day
- Attendance percentage
- Previous marks
- Assignment score

A Streamlit interface is included so users can enter these details and get a performance prediction.

## Features

- Predicts student performance from academic inputs
- Simple and easy-to-use Streamlit interface
- Uses a Decision Tree Classifier
- Includes a sample dataset
- Trained model is saved and used for prediction

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

## Project Structure

```text
student-performance-predictor/
│
├── app.py
├── train_model.py
├── student_data.csv
├── model.pkl
├── requirements.txt
├── README.md
└── .gitignore
