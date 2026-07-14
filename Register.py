import streamlit as st

st.title("Student Registration")

name=st.text_input("Student Name")
age=st.number_input("Age")

attendance=st.slider("Attendance",0,100)

marks=st.slider("Marks",0,100)

income=st.number_input("Family Income")

if st.button("Register"):
    st.success("Student Registered")
