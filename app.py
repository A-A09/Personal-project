import streamlit as st

st.header("Football Journey")

# Streamlit app
with st.sidebar: 

    st.title("**Navigation**")
    choice = st.radio("Choose an option", ["Intro","Videos"])

if choice =="Intro":
    st.text("\n")
    st.subheader("Intro")
    st.text("This is the title and a short welcome message: Kick-off Basics: The Fundamentals of Padel Welcome to my Football learning journey! Here, you will find a series of insightful instructional videos designed to showcase my progress as I learn the fundamentals of football, including essential skills, rules, and techniques. Whether you're a beginner or just curious about the process, these videos aim to inspire and guide you through the basics of the sport. Have fun!")
    
if choice == "Videos":

    st.text("\n")
    st.subheader("the videos will be here")

# to run streamlit use this command: python -m streamlit run app.py            
# streamlit run c:/Users/abdul/OneDrive/Desktop/projects/Learning/app.py
