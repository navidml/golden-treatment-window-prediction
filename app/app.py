import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Sepsis Prediction System",
    layout="wide"
)

model = joblib.load(r"C:\Users\navid\OneDrive\دسکتاپ\projects\9)Golden Treatment Window Prediction\models\golden_treatment_model.pkl")

if not hasattr(model, "algorithm"):
    model.algorithm = "SAMME.R"


st.title("Sepsis Prediction System")
st.markdown("##### Enter patient clinical information below to assess sepsis risk.")
st.write("---")

left_space, main_content, right_space = st.columns([1, 4, 1])

with main_content:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Laboratory & Score Metrics")
        
        lactate_mmol = st.number_input(
            "Lactate (mmol/L)",
            value=2.0
        )

        apache_iv = st.number_input(
            "APACHE IV Score",
            value=50
        )

        ph_arterial = st.number_input(
            "Arterial pH",
            value=7.40,
            format="%.2f"
        )

        creatinine = st.number_input(
            "Creatinine",
            value=1.0
        )

        spo2_mean = st.number_input(
            "Mean SpO2 (%)",
            value=98.0
        )

    with col2:
        st.markdown("### Vital Signs & Clinical Criteria")

        sofa_score = st.number_input(
            "SOFA Score",
            value=2
        )

        fluids_ml_24h = st.number_input(
            "Fluids 24h (mL)",
            value=2000
        )

        respiratory_rate_min = st.number_input(
            " Respiratory Rate Min",
            value=16
        )

        bicarbonate = st.number_input(
            "Bicarbonate",
            value=24.0
        )

        sirs_criteria = st.number_input(
            "SIRS Criteria",
            value=1
        )

        temp_celsius_min = st.number_input(
            "Minimum Temperature (°C)",
            value=37.0
        )

    st.write("") 
    
    submit_button = st.button("🔮 Predict Sepsis Risk", use_container_width=True, type="primary")

if submit_button:

    input_df = pd.DataFrame({
        'lactate_mmol': [lactate_mmol],
        'apache_iv': [apache_iv],
        'ph_arterial': [ph_arterial],
        'creatinine': [creatinine],
        'spo2_mean': [spo2_mean],
        'sofa_score': [sofa_score],
        'fluids_ml_24h': [fluids_ml_24h],
        'respiratory_rate_min': [respiratory_rate_min],
        'bicarbonate': [bicarbonate],
        'sirs_criteria': [sirs_criteria],
        'temp_celsius_min': [temp_celsius_min]
    })

    try:
        prediction = model.predict(input_df)[0]

        if prediction == 1:
            st.error("⚠️ High Risk of Sepsis")
        else:
            st.success("✅ Low Risk of Sepsis")

        try:
            probability = model.predict_proba(input_df)[0][1]

            st.metric(
                "Sepsis Probability",
                f"{probability:.1%}"
            )

            st.progress(float(probability))

        except Exception as e:
            st.warning(f"Probability unavailable: {e}")

    except Exception as e:
        st.error(f"Prediction Error: {e}")
