import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

# Sample dataset 
data = pd.DataFrame({
    'Feature1': [1.0, 2.0, 3.0, 4.0, 5.0],
    'Feature2': [2.0, 3.0, 4.0, 5.0, 6.0],
    'Feature3': [3.0, 4.0, 5.0, 6.0, 7.0],
    'Biocompatible': [0, 0, 1, 1, 0]  #0 for not biocompatible, 1 for biocompatible
})

features = data[['Feature1', 'Feature2', 'Feature3']]
labels = data['Biocompatible']

X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(features, labels)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy*100}%")

model_path = os.path.abspath('C:\\Users\\Rahul Patnaik\\Desktop\\biocompatibility\\biocompatibility_model.pkl')

try:
    joblib.dump(model, model_path)
    print("Model saved successfully!")
except Exception as e:
    print("Error while saving the model:", e)




print("Current Working Directory:", os.getcwd())
