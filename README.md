Heart Disease Prediction Web App
================================

This is a Flask-based web application that predicts the presence of heart disease in a patient using a machine learning model. The model is trained on the heart disease dataset and uses 13 clinical parameters as input features.

Features
--------
- Predicts heart disease risk based on patient input.
- Takes into account 13 health indicators (like cholesterol, chest pain type, etc.).
- Displays prediction results along with confidence probabilities.
- Generates a report with patient details and explanations of input features.

Project Structure
-----------------
app.py                # Main Flask app
model.pkl             # Trained ML model (Pickle format)
heart-disease.csv     # Dataset used for training
templates/
  ├── index.html      # Input form page
  └── report.html     # Result page

How to Run
----------
1. Clone the repository:
   git clone https://github.com/your-username/heart-disease-predictor.git
   cd heart-disease-predictor

2. Install dependencies:
   pip install flask numpy pickle-mixin

3. Make sure you have `model.pkl` and the `templates/` folder ready.

4. Run the Flask app:
   python app.py

5. Open your browser and go to:
   http://127.0.0.1:5000/

Input Features
--------------
- Age: Age in years
- Gender: 0 = Female, 1 = Male
- Chest Pain Type: 0 = Typical Angina, 1 = Atypical, 2 = Non-anginal, 3 = Asymptomatic
- Resting Blood Pressure (mm Hg)
- Serum Cholesterol (mg/dl)
- Fasting Blood Sugar: 1 if > 120 mg/dl, else 0
- Resting ECG: 0 = Normal, 1 = ST-T wave abnormality, 2 = Left ventricular hypertrophy
- Max Heart Rate Achieved
- Exercise-Induced Angina: 1 = Yes, 0 = No
- ST Depression
- Slope of Peak ST Segment: 1 = Upsloping, 2 = Flat, 3 = Downsloping
- Number of Major Vessels (0–3)
- Thalassemia: 1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect

Dataset
-------
The dataset used (`heart-disease.csv`) includes labeled data indicating the presence or absence of heart disease based on medical attributes.

Disclaimer
----------
This app is for educational purposes only. It is not intended for real medical diagnosis. Please consult a professional healthcare provider for actual medical advice.

License
-------
MIT License

Author: Ashi Mittal
GitHub: https://github.com/ashimittal5
