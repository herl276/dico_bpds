import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model dan scaler
model = joblib.load("dropout_app/dropout_model.pkl")
scaler = joblib.load("dropout_app/scaler.pkl")

st.title("Prediksi Dropout Mahasiswa (Batch Mode)")
st.markdown("Upload file CSV berisi data siswa untuk diprediksi apakah mereka akan dropout.")

uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("Preview Data")
    st.dataframe(df.head())

    try:
        X = df[[
       'Marital_status', 'Application_mode', 'Application_order', 'Course',
       'Daytime_evening_attendance', 'Previous_qualification',
       'Previous_qualification_grade', 'Nacionality', 'Mothers_qualification',
       'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation',
       'Admission_grade', 'Displaced', 'Educational_special_needs', 'Debtor',
       'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder',
       'Age_at_enrollment', 'International',
       'Curricular_units_1st_sem_credited',
       'Curricular_units_1st_sem_enrolled',
       'Curricular_units_1st_sem_evaluations',
       'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
       'Curricular_units_1st_sem_without_evaluations',
       'Curricular_units_2nd_sem_credited',
       'Curricular_units_2nd_sem_enrolled',
       'Curricular_units_2nd_sem_evaluations',
       'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
       'Curricular_units_2nd_sem_without_evaluations', 'Unemployment_rate',
       'Inflation_rate', 'GDP'
        ]]

        # Preprocessing
        X_scaled = scaler.transform(X)

        # Predict
        predictions = model.predict(X_scaled)
        pred_labels = np.where(predictions == 1, "Dropout", "Tidak Dropout")

        # Tambahkan kolom hasil prediksi ke df
        df["Status_Predicted"] = pred_labels

        st.subheader("Hasil Prediksi")
        st.dataframe(df[["Status_Predicted"]].value_counts().rename("Jumlah"))
        st.markdown("**Preview Tabel Lengkap dengan Prediksi:**")
        st.dataframe(df.head(20))

        # Download file hasil
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download Hasil sebagai CSV",
            data=csv,
            file_name='prediksi_dropout.csv',
            mime='text/csv'
        )

    except KeyError as e:
        st.error(f"Kolom tidak ditemukan dalam CSV: {e}")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memproses file: {e}")
