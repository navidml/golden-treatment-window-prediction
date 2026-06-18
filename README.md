# Sepsis Risk Prediction System

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-red?logo=streamlit)](https://sepsis-risk-predictor.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-orange.svg)](https://scikit-learn.org/)

## Overview

Sepsis Risk Prediction System is a machine learning-powered clinical decision support application designed to estimate the likelihood of sepsis using routinely collected physiological and laboratory measurements.

The project combines feature selection, ensemble learning techniques, and an interactive Streamlit interface to provide real-time sepsis risk assessment.

**Live Application:**  
https://sepsis-risk-predictor.streamlit.app/

---

## Project Objective

Sepsis is a life-threatening condition that requires early recognition and timely intervention.

The objective of this project is to:

- Identify patients at risk of developing sepsis
- Support early clinical decision-making
- Utilize interpretable clinical variables
- Deliver predictions through an easy-to-use web application

---

## Dataset

**Source:** Kaggle

**Target Variable**

```text
sepsis_label
```

**Classification Task**

```text
0 → No Sepsis
1 → Sepsis
```

---

## Selected Clinical Features

| Feature | Description |
|----------|-------------|
| lactate_mmol | Blood lactate level |
| apache_iv | APACHE IV severity score |
| ph_arterial | Arterial blood pH |
| creatinine | Kidney function indicator |
| spo2_mean | Mean oxygen saturation |
| sofa_score | SOFA score |
| fluids_ml_24h | Fluid administration within 24 hours |
| respiratory_rate_min | Minimum respiratory rate |
| bicarbonate | Serum bicarbonate level |
| sirs_criteria | Number of SIRS criteria met |
| temp_celsius_min | Minimum body temperature |

---

## Machine Learning Model

### Final Architecture

```text
AdaBoost Classifier
+
Random Forest Base Estimator
```

This ensemble architecture combines the adaptive learning capability of AdaBoost with the robustness of Random Forest classifiers to improve predictive performance and model stability.

---

## Model Development Pipeline

```text
Data Collection
        ↓
Data Cleaning
        ↓
Feature Selection
        ↓
Train/Test Split
        ↓
AdaBoost + Random Forest
        ↓
Grid Search Optimization
        ↓
Model Evaluation
        ↓
Deployment with Streamlit
```

---

## Performance Evaluation

The model was evaluated using multiple classification metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- Cohen's Kappa
- Matthews Correlation Coefficient (MCC)
- Specificity

Cross-validation and hyperparameter optimization were performed using Grid Search.

---

## Streamlit Application

The web application allows users to:

- Enter patient clinical measurements
- Estimate sepsis risk instantly
- View model predictions in real time
- Obtain probability-based risk assessment

---

## Installation

Clone the repository:

```bash
git clone https://github.com/navidml/golden-treatment-window-prediction.git
cd golden-treatment-window-prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app/app.py
```

---

## Project Structure

```text
golden-treatment-window-prediction/
│
├── app/
│   └── app.py
│
├── data/
│
├── models/
│   └── golden_treatment_model.pkl
│
├── notebooks/
│
├── requirements.txt
│
└── README.md
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- AdaBoost
- Random Forest
- Streamlit
- Joblib
- Matplotlib

---

## Live Demo

https://sepsis-risk-predictor.streamlit.app/

---

## Author

**Navid Bordbar**

Machine Learning • Data Science • Clinical AI

GitHub: https://github.com/navidml

---

## Future Work

- External validation on independent datasets
- Model explainability using SHAP
- Integration with electronic health records (EHR)
- Deployment in clinical decision support environments
- Comparative evaluation with XGBoost and LightGBM models

---

## License

This project is intended for research and educational purposes.
