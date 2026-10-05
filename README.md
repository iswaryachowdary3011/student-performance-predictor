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
## Machine Learning Model

The project uses a **Decision Tree Classifier** from Scikit-learn.

The model is trained using the student dataset and saved as `model.pkl`. The Streamlit application loads this trained model to make predictions based on the user's inputs.

## Dataset

The dataset contains student-related information including:

- Study hours
- Attendance
- Previous marks
- Assignment score
- Performance

## Project Purpose

The purpose of this project is to understand the basic workflow of a machine learning project, from preparing data and training a model to using the trained model in a simple application.

## Future Improvements

- Add more relevant student data
- Try other machine learning algorithms
- Compare model performance
- Improve the user interface
- Deploy the application online

## Author

**Iswarya**

GitHub: https://github.com/iswaryachowdary3011
