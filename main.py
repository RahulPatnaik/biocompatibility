import tkinter as tk
from tkinter import filedialog
import pandas as pd
import joblib
import openpyxl
import os

print(os.getcwd())

current_directory = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(current_directory, 'biocompatibility_model.pkl')
model = joblib.load(model_path)


def load_data(file_path):
    try:
        excel_data = openpyxl.load_workbook(file_path)
        sheet = excel_data['Sheet1']

        data = pd.DataFrame(sheet.values)

        data.columns = data.iloc[0]
        data = data[1:]

        data['Feature1'] = data['Feature1'].astype(float)
        data['Feature2'] = data['Feature2'].astype(float)
        data['Feature3'] = data['Feature3'].astype(float)
        data['Biocompatible'] = data['Biocompatible'].astype(int)

        return data

    except Exception as e:
        return None

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

app = tk.Tk()
app.title("Biocompatibility Checker")
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

app.geometry(f"{screen_width}x{screen_height}")

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

predict_button = tk.Button(app, text="Predict Biocompatibility", height=5, width= 50, command=handle_prediction)
predict_button.place(x=20, y=300)

result_label = tk.Label(app, text="", font=("Helvetica", 30))
result_label.pack()

app.mainloop()
