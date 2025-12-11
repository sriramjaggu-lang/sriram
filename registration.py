import streamlit as st
from datetime import datetime
st.title("Hello, Streamlit")
st.title("Student Registration form")
name=st.text_input("enter your name:")
branch=st.selectbox("select your branch",["computer", "commerce", "mathematics", "physics"])
marks=st.number_input("enter your marks",0,100)
age=st.slider("select your age",10,100,25)
dob=st.date_input("enter your date of birth")
st.write(cage=datetime.now().year - dob.year)
skills=st.multiselect("select your skills",["python","java","c++","html","css","javascript"])
if st.button("submit"):
    st.success("form submitted")
    st.write(branch)
    st.write(marks)