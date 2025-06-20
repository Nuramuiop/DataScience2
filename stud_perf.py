import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

model = joblib.load("model_gb.pkl")
le = LabelEncoder()

col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=130)
with col2:
    st.header('Student Performance Prediction (Prototype) :sparkles:')

data = pd.DataFrame()

col1, col2, col3 = st.columns(3)

label_to_value = {"Yes": 1, "No": 0}

with col1:
    # st.header("Kolom 1")
    Previous_qualification_grade = int(st.number_input(label='Previous_qualification_grade', value=23))
    data["Previous_qualification_grade"] = [Previous_qualification_grade]

with col2:
    Admission_grade = float(st.number_input(label='Admission_grade', value=3))
    data["Admission_grade"] = [Admission_grade]

with col3:
    Displaced = st.selectbox(label='Displaced', options=list(label_to_value.keys()), index=1)
    data["Displaced"] = label_to_value[Displaced]



col1, col2, col3 = st.columns(3)

with col1:
    Tuition_fees_up_to_date = st.selectbox(label='Tuition_fees_up_to_date', options=list(label_to_value.keys()), index=1)
    data["Tuition_fees_up_to_date"] = label_to_value[Tuition_fees_up_to_date]

with col2:
    Scholarship_holder = st.selectbox(label='Scholarship_holder',options=list(label_to_value.keys()), index=1)
    data["Scholarship_holder"] = label_to_value[Scholarship_holder]

with col3:
    Curricular_units_1st_sem_approved = int(st.number_input(label='Curricular_units_1st_sem_approved', value=4))
    data["Curricular_units_1st_sem_approved"] = [Curricular_units_1st_sem_approved]



col1, col2, col3 = st.columns(3)

with col1:
    Curricular_units_1st_sem_grade = int(st.number_input(label='Curricular_units_1st_sem_grade', value=4))
    data["Curricular_units_1st_sem_grade"] = [Curricular_units_1st_sem_grade]

with col2:
    # st.header("Kolom 1")
    Curricular_units_2nd_sem_approved = int(st.number_input(label='Curricular_units_2nd_sem_approved', value=3))
    data["Curricular_units_2nd_sem_approved"] = [Curricular_units_2nd_sem_approved]

with col3:
    Curricular_units_2nd_sem_grade = int(st.number_input(label='Curricular_units_2nd_sem_grade', value=7))
    data["Curricular_units_2nd_sem_grade"] = [Curricular_units_2nd_sem_grade]




with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)

if st.button('Predict'):
    prediction_result = model.predict(data)[0]
    real_label = le.inverse_transform([prediction_result])[0]
    st.write("Credit Scoring: {}".format(real_label))
