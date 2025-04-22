from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect patient information
    patient_name = request.form.get('patient_name')
    patient_age = int(request.form.get('age'))
    patient_gender = "Male" if request.form.get('gender') == "1" else "Female"

    # Extract model features
    features = [float(request.form.get(col)) for col in [
        'age', 'gender', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
        'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
    ]]
    
    # Prepare data for model prediction
    final_features = np.array([features]).reshape(1, -1)
    prediction = model.predict(final_features)[0]
    prediction_probability = model.predict_proba(final_features)[0][1]

    # Interpret the result with probability
    if prediction == 1:
        result = f"Heart Disease Detected (Probability: {prediction_probability:.2%})"
        result_class = "positive"
    else:
        result = f"No Heart Disease Detected (Probability: {(1-prediction_probability):.2%})"
        result_class = "negative"

    # Prepare report details
    patient_details = {
        "Name": patient_name,
        "Age": patient_age,
        "Gender": patient_gender
    }

    # Feature names for heart disease context
    feature_names = [
        "Age (Years)",
        "Gender (0=Female, 1=Male)",
        "Chest Pain Type",
        "Resting BP (mmHg)",
        "Cholesterol (mg/dl)",
        "Fasting Blood Sugar (>120 mg/dl)",
        "Resting ECG",
        "Max Heart Rate",
        "Exercise-Induced Angina (1=Yes, 0=No)",
        "ST Depression",
        "Slope of Peak ST",
        "No. of Major Vessels",
        "Thalassemia Type"
    ]

    # Feature descriptions for better understanding
    feature_descriptions = {
        "Age (Years)": "Patient's age in years",
        "Gender (0=Female, 1=Male)": "0 = Female, 1 = Male",
        "Chest Pain Type": "0 = Typical angina, 1 = Atypical angina, 2 = Non-anginal pain, 3 = Asymptomatic",
        "Resting BP (mmHg)": "Resting blood pressure in mmHg",
        "Cholesterol (mg/dl)": "Serum cholesterol in mg/dl",
        "Fasting Blood Sugar (>120 mg/dl)": "0 = ≤120 mg/dl, 1 = >120 mg/dl",
        "Resting ECG": "0 = Normal, 1 = ST-T wave abnormality, 2 = Left ventricular hypertrophy",
        "Max Heart Rate": "Maximum heart rate achieved",
        "Exercise-Induced Angina (1=Yes, 0=No)": "0 = No, 1 = Yes",
        "ST Depression": "ST depression induced by exercise relative to rest",
        "Slope of Peak ST": "1 = Upsloping, 2 = Flat, 3 = Downsloping",
        "No. of Major Vessels": "Number of major vessels colored by fluoroscopy (0-4)",
        "Thalassemia Type": "1 = Normal, 2 = Fixed defect, 3 = Reversable defect"
    }

    return render_template('report.html', 
                         result=result,
                         result_class=result_class,
                         patient=patient_details, 
                         features=features, 
                         feature_names=feature_names,
                         feature_descriptions=feature_descriptions)

if __name__ == '__main__':
    app.run(debug=True)
