import tkinter as tk
from tkinter import filedialog
import pandas as pd
import joblib
import openpyxl
import os

print(os.getcwd())

# Determine the full path to the directory 
current_directory = os.path.dirname(os.path.abspath(__file__))

# Load the trained machine learning model
model_path = os.path.join(current_directory, 'biocompatibility_model.pkl')
model = joblib.load(model_path)


# load and preprocess the data
def load_data(file_path):
    try:
        # Load the Excel file using openpyxl
        excel_data = openpyxl.load_workbook(file_path)
        # Specify the sheet
        sheet = excel_data['Sheet1']

        # Convert the sheet data to a DataFrame
        data = pd.DataFrame(sheet.values)

        # Assign column names based on the first row
        data.columns = data.iloc[0]
        data = data[1:]  # Remove the first row

        # Convert to float data types
        data['Feature1'] = data['Feature1'].astype(float)
        data['Feature2'] = data['Feature2'].astype(float)
        data['Feature3'] = data['Feature3'].astype(float)
        data['Biocompatible'] = data['Biocompatible'].astype(int)

        return data

    except Exception as e:
        return None

# handle user input and make predictions
def handle_prediction():
    user_input = {
        'Feature1': float(feature1_entry.get()),
        'Feature2': float(feature2_entry.get()),
        'Feature3': float(feature3_entry.get()),
    }

    user_data = pd.DataFrame([user_input])

    try:
        prediction = model.predict(user_data)
        if prediction[0] == 1:
            result_label.config(text="Biocompatible: Yes")
        else:
            result_label.config(text="Biocompatible: No")
    except Exception as e:
        result_label.config(text=f"Error: {e}")

# Create the main application window
app = tk.Tk()
app.title("Biocompatibility Checker")

# Get the screen width and height
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Set the window size to the screen size
app.geometry(f"{screen_width}x{screen_height}")

# Add input fields for user to enter features
feature1_label = tk.Label(app, text="Feature 1:", font=("Helvetica", 20))
feature1_label.place(x=20,y=10)
feature1_entry = tk.Entry(app, width= 30, font=("Helvetica", 20))
feature1_entry.place(x=20,y=50)

feature2_label = tk.Label(app, text="Feature 2:", font=("Helvetica", 20))
feature2_label.place(x=20, y=90)
feature2_entry = tk.Entry(app, width= 30, font=("Helvetica", 20))
feature2_entry.place(x=20, y=130)

feature3_label = tk.Label(app, text="Feature 3:", font=("Helvetica", 20))
feature3_label.place(x=20, y=170)
feature3_entry = tk.Entry(app, width= 30, font=("Helvetica", 20))
feature3_entry.place(x=20, y=210)

# Button to trigger prediction
predict_button = tk.Button(app, text="Predict Biocompatibility", height=5, width= 50, command=handle_prediction)
predict_button.place(x=20, y=300)

# Label to display the prediction result
result_label = tk.Label(app, text="", font=("Helvetica", 30))
result_label.pack()

# Start the Tkinter main loop
app.mainloop()
