import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('penyakit_jantung.sav', 'rb'))

st.title('PREDIKSI SERANGAN JANTUNG')

col1, col2 = st.columns(2)

with col1 :
    age = st.text_input ('Input Nilai Age')
with col2 :
    sex = st.text_input ('Input Nilai Sex')
with col1 :
    cp = st.text_input ('Input Nilai Cp')
with col2 :
    trtbps = st.text_input ('Input Nilai Trtbps')
with col1 :
    chol = st.text_input ('Input Nilai Chol')
with col2 :
    fbs = st.text_input ('Input Nilai Fbs')
with col1 :
    restecg = st.text_input ('Input Nilai Restecg')
with col2 :
    thalachh = st.text_input ('Input Nilai Thalachh')
with col1 :
    exng = st.text_input ('Input Nilai Exng')
with col2 :
    oldpeak = st.text_input ('Input Nilai Oldpeak')
with col1 :
    slp = st.text_input ('Input Nilai Slp')
with col2 :
    caa = st.text_input ('Input Nilai Caa')
with col1 :
    thall = st.text_input ('Input Nilai Thall')

heart_diagnosis = ''

if st.button('Test Prediksi Serangan Jantung') :
    heart_prediction = model.predict([[age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]])

    if (heart_prediction[0] == 0):
        haert_diagnosis = 'Pasien tidak terkena serangan jantung'
    else :
        heart_diagnosis = 'Pasien terkena serangan jantung'
    
st.success(heart_diagnosis)
