import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load the dataset
data = pd.read_csv("student_data.csv")

# Input features
X = data[[
    "study_hours",
    "attendance",
    "previous_marks",
    "assignment_score"
]]

# Target/output
y = data["performance"]

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create the machine learning model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Check accuracy
accuracy = model.score(X_test, y_test)

print("Model Accuracy:", accuracy)

# Save the trained model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained and saved successfully!")