from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd
import os

app = Flask(__name__)

# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")
model = joblib.load(MODEL_PATH)
# Features in the same order as training
feature_cols = [
    'age', 'education_level', 'department', 'job_role',
    'years_experience', 'training_hours', 'avg_monthly_hours',
    'satisfaction_level', 'last_performance_score',
    'absenteeism_days', 'promotion_last_5yrs'
]

# Home page
@app.route("/")
def home():
    return render_template("home.html")

# About page
@app.route("/about")
def about():
    return render_template("about.html")

# Predict page (form)
@app.route("/predict")
def predict_page():
    return render_template("predict.html")

# Submit page (handle form submission)
@app.route("/submit", methods=["POST"])
def submit():
    try:
        # Collect values from form
        data = {}
        for col in feature_cols:
            val = request.form.get(col)
            # Convert numeric fields
            if col in ['age', 'years_experience', 'training_hours', 'avg_monthly_hours',
                       'satisfaction_level', 'last_performance_score',
                       'absenteeism_days', 'promotion_last_5yrs']:
                if val is None or val.strip() == "":
                    data[col] = np.nan
                else:
                    data[col] = float(val)
            else:
                data[col] = val

        X = pd.DataFrame([data])
        prediction = model.predict(X)[0]

        # Probability (for classifiers)
        if hasattr(model, "predict_proba"):
            probability = round(float(model.predict_proba(X)[0].max()), 3)
        else:
            probability = None

        return render_template("submit.html", prediction=prediction, probability=probability)

    except Exception as e:
        return render_template("submit.html", error=str(e))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
