# Employee Performance Prediction (Demo Project)

## 📌 Project Overview
This project demonstrates a Machine Learning approach to **Employee Performance Prediction**. 
It follows a workflow of data preprocessing, model training, evaluation, and deployment using Flask.

## 📂 Project Structure
```
Project_Demo/
│
├── Dataset/
│   └── employee_performance.csv
│
├── Training/
│   └── Employee_Prediction.ipynb
│
├── Flask/
│   ├── app.py
│   ├── model.pkl
│   └── templates/
│       └── index.html
│
└── README.md
```

## ⚙️ Steps to Run the Project

### 1. Setup Environment
```bash
pip install -r requirements.txt
```

Required libraries:
- pandas
- numpy
- scikit-learn
- flask
- joblib

### 2. Train the Model
- Open `Training/Employee_Prediction.ipynb`
- Run all cells to:
  - Load and preprocess dataset
  - Train model
  - Save trained model as `model.pkl`

### 3. Run Flask App
Navigate to the Flask folder and run:
```bash
python app.py
```

### 4. Access Web App
- Open your browser and go to:
```
http://127.0.0.1:5000/
```
- Enter input values to get employee performance prediction.

## ✅ Notes
- You can replace `Dataset/employee_performance.csv` with your own dataset.
- Retrain the model if dataset changes.
