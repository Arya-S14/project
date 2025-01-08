import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and introduction
st.title("Mental Health Analysis")
st.write("Welcome to this mental health analysis tool! We'll ask you a series of questions to help us understand your mental health and well-being.")

# User input: Demographic information
st.header("Demographic Information")
age = st.selectbox("What is your age?", ["18-24", "25-34", "35-44", "45-54", "55+"])
occupation = st.selectbox("What is your occupation?", ["Student", "Working Professional", "Homemaker", "Retired", "Other"])

# User input: Mental health questions
st.header("Mental Health Questions")
questions = [
    "Have you experienced any anxiety or fear in the past week?",
    "Have you felt sad or depressed in the past week?",
    "Have you had trouble sleeping in the past week?",
    "Have you experienced any physical symptoms like headaches or stomachaches in the past week?",
    "Have you felt overwhelmed or stressed in the past week?"
]
responses = []
for question in questions:
    response = st.selectbox(question, ["Yes", "No"])
    responses.append(response)

# Analyze responses and create pie charts
st.header("Analysis")
yes_count = responses.count("Yes")
no_count = responses.count("No")

fig, ax = plt.subplots()
ax.pie([yes_count, no_count], labels=["Yes", "No"], autopct='%1.1f%%')
ax.axis('equal')
st.pyplot(fig)

# Provide recommendations based on analysis
st.header("Recommendations")
if yes_count > 3:
    st.write("It seems like you're experiencing some mental health challenges. We recommend reaching out to a mental health professional for support.")
elif yes_count > 1:
    st.write("It seems like you're experiencing some stress or anxiety. We recommend trying some relaxation techniques like deep breathing or meditation.")
else:
    st.write("It seems like you're doing well mentally! Keep up the good work and prioritize your self-care.")

# Provide additional resources
st.header("Additional Resources")
st.write("If you're struggling with your mental health, here are some additional resources that may be helpful:")
st.write("* National Alliance on Mental Illness (NAMI) Hotline: 1-800-950-6264")
st.write("* Crisis Text Line: Text HOME to 741741")


