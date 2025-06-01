import streamlit as st
import numpy as np
import joblib

# Load model dan scaler
model = joblib.load("dropout_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Prediksi Dropout Mahasiswa")

st.markdown("Masukkan informasi berikut untuk memprediksi kemungkinan dropout:")

# INPUT USER
marital_status = st.selectbox("Marital Status", [1, 2])
application_mode = st.selectbox("Application Mode", list(range(1, 50)))
application_order = st.number_input("Application Order", 1, 20, 1)
course = st.number_input("Course ID", 1, 10000)
attendance = st.selectbox("Daytime/Evening Attendance", [0, 1])
prev_qualification = st.number_input("Previous Qualification", 1, 50, 1)
prev_grade = st.number_input("Previous Qualification Grade", 0.0, 200.0, 120.0)
nacionality = st.number_input("Nationality", 1, 20, 1)
mother_qual = st.number_input("Mother's Qualification", 1, 50, 1)
father_qual = st.number_input("Father's Qualification", 1, 50, 1)
admission_grade = st.number_input("Admission Grade", 0.0, 200.0, 120.0)
age = st.number_input("Age at Enrollment", 17, 80, 20)
gpa1 = st.number_input("GPA Semester 1", 0.0, 20.0, 12.0)
gpa2 = st.number_input("GPA Semester 2", 0.0, 20.0, 12.0)

# Tambahkan fitur sesuai kebutuhan
features = np.array([
    marital_status, application_mode, application_order, course, attendance,
    prev_qualification, prev_grade, nacionality, mother_qual, father_qual,
    admission_grade, age, gpa1, gpa2
]).reshape(1, -1)

# Preprocessing input
features_scaled = scaler.transform(features)

# Prediksi
if st.button("Prediksi"):
    pred = model.predict(features_scaled)[0]
    prob = model.predict_proba(features_scaled)[0][1]
    
    if pred == 1:
        st.error(f"❌ Siswa ini berisiko dropout (Probabilitas: {prob:.2f})")
    else:
        st.success(f"✅ Siswa ini *tidak berisiko* dropout (Probabilitas: {prob:.2f})")