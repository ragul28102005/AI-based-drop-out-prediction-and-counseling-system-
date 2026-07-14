import streamlit as st
import pandas as pd

st.title("Reports")

df=pd.read_csv("student_data.csv")

st.dataframe(df)

st.bar_chart(df["Attendance"])

st.line_chart(df["Marks"])
