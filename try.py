import streamlit as st
import random
import matplotlib.pyplot as plt
import pandas as pd


# Title and introduction
st.title("Mindful Moments !!!! ")
st.write("Welcome to Mindful Moments! Taking Care Of Your Mental Health")

# User input: How are you feeling today?
name = st.text_input("What's Your Name ?")
if(name):
    st.write(f"Hello {name} !!!")
age = st.slider("What's Your Age ", 12, 32, 20)
st.write(age)
st.write("What is Your Gender")
gender = st.radio("Choose",["Male","Female","Others"])


st.header("Check-in: How Are You Feeling Today?")
feelings = ["Happy", "Sad", "Anxious", "Stressed", "Neutral"]
feeling_today = st.selectbox("Select how you're feeling today", feelings)

st.header("Mindful Moment: Take a Break and Relax")
actions = {
    "Happy": "1)Sit comfortably, close your eyes, and focus on your breath. Inhale deeply through your nose, hold for 4 seconds, and exhale slowly through your mouth. (5 minutes)\n \n 2)Write down three things you're grateful for today. Reflect on why they're important to you and how they've positively impacted your life. (3 minutes)",
    "Sad": "1)Write down your thoughts and feelings without editing or judgment. Allow yourself to process your emotions and reflect on what you're experiencing. (5 minutes)\n \n 2)Sit comfortably, close your eyes, and focus on your breath. Repeat the following phrases to yourself: I am kind to myself, I am deserving of love and care,I am strong (5 minutes)",
    "Anxious": "Take a short walk outside and focus on your surroundings.",
    "Stressed": "Try some progressive muscle relaxation to release tension.",
    "Neutral": "Take a moment to notice your thoughts and emotions without judgment."
}
action = actions[feeling_today]
st.write(action)


st.header("You Did It! Earn Your Reward")
rewards = ["Take a break and watch a funny video", "Treat yourself to a favorite snack", "Read a chapter in a book you're enjoying"]
reward = random.choice(rewards)
st.write(reward)


st.header("Check-in: How Do You Feel Now?")
feelings_after = ["Better", "Same", "Worse"]
feeling_after = st.selectbox("Select how you're feeling now", feelings_after)


st.header("Thank You for Taking Care of Your Mental Health!")
if feeling_after == "Better":
    st.write("Keep up the good work! Remember to prioritize your mental health every day.")
elif feeling_after == "Same":
    st.write("It's okay if you're not feeling better yet. Remember that mental health is a journey, and it's okay to take things one step at a time.")
else:
    st.write("Remember that it's okay to not be okay. If you're feeling overwhelmed or struggling with your mental health, don't hesitate to reach out to a trusted friend, family member, or mental health professional for support.")


st.header("Student Depression Assessment")
questions = [
    "Have you experienced any academic pressure or stress in the past semester?",
    "Have you felt overwhelmed by your coursework or responsibilities?",
    "Have you experienced any social isolation or loneliness on campus?",
    "Have you felt like you don't belong or are not good enough?",
    "Have you experienced any symptoms of depression, such as changes in appetite or sleep patterns?"
]
responses = []
for question in questions:
    response = st.selectbox(question, ["Yes", "No"])
    responses.append(response)


st.header("Analysis and Recommendations")
yes_count = responses.count("Yes")
no_count = responses.count("No")

fig, ax = plt.subplots()
ax.pie([yes_count, no_count], labels=["Yes", "No"], autopct='%1.1f%%')
ax.axis('equal')
st.pyplot(fig)

if yes_count > 3:
    st.write("You may be experiencing some symptoms of depression. We recommend reaching out to a mental health professional for support.")
elif yes_count > 1:
    st.write("You may be experiencing some academic stress or pressure. We recommend talking to a academic advisor or counselor for support.")
else:
    st.write("You seem to be doing well! Keep up the good work and prioritize your mental health.")


st.header("Additional Resources")
st.write("If you're struggling with your mental health, here are some additional resources that may be helpful:")
st.write("* National Alliance onMental Illness (NAMI) Hotline: 1-800-950-6264")
st.write("* Crisis Teext Line: Text HOME to 741741")
st.header("Have Happy Moments ;) ")


# Load the dataset
file_path = "Student Depression Dataset.csv"  # Ensure the file is in the same directory or provide the full path
data = pd.read_csv(file_path)

# Check for missing values in relevant columns
if data.isnull().any().any():
    print("Warning: Missing values detected. Consider handling them before analysis.")

# Plot 1: Pie chart for depression status
depression_counts = data['Depression'].value_counts()
labels = ['No Depression', 'Depression']
colors = ['lightgreen', 'salmon']

plt.fig
