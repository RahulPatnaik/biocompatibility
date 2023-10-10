import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Sample dataset (replace this with your own dataset)
data = pd.DataFrame({
    'Feature1': [1.0, 2.0, 3.0, 4.0, 5.0],
    'Feature2': [2.0, 3.0, 4.0, 5.0, 6.0],
    'Feature3': [3.0, 4.0, 5.0, 6.0, 7.0],
    'Biocompatible': [0, 0, 1, 1, 0]  # Example labels (0 for not biocompatible, 1 for biocompatible)
})

# Split the data into features and labels
features = data[['Feature1', 'Feature2', 'Feature3']]
labels = data['Biocompatible']

# Create and train a random forest classifier (replace this with your own dataset)
model = RandomForestClassifier()
model.fit(features, labels)

model_path = os.path.abspath('C:\\Users\\Rahul Patnaik\\Desktop\\biocompatibility\\biocompatibility_model.pkl')

try:
    # Attempt to save the model
    joblib.dump(model, model_path)
    print("Model saved successfully!")
except Exception as e:
    print("Error while saving the model:", e)




print("Current Working Directory:", os.getcwd())