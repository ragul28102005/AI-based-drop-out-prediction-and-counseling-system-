import streamlit as st

from models.prediction import predict
from models.counseling import counseling

st.title("Prediction")

attendance=st.slider("Attendance",0,100)

marks=st.slider("Marks",0,100)

income=st.number_input("Income")

age=st.number_input("Age")

if st.button("Predict"):

    result=predict([age,attendance,marks,income])

    if result==1:
        st.error("High Risk")
    else:
        st.success("Low Risk")

    st.info(counseling(result))
