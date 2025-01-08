import streamlit as st
import random
import matplotlib.pyplot as plt
import pandas as pd

# Title and introduction
st.title("Mindful Moments!")
st.write("Welcome to Mindful Moments! Taking Care Of Your Mental Health")

# User input: How are you feeling today?
name = st.text_input("What's Your Name?")
if name:
    st.write(f"Hello, {name}!!!")
age = st.slider("What's Your Age", 12, 32, 20)
st.write(f"Age: {age}")
st.write("What is Your Gender?")
gender = st.radio("Choose", ["Male", "Female", "Others"])

st.header("Check-in: How Are You Feeling Today?")
feelings = ["Happy", "Sad", "Anxious", "Stressed", "Neutral"]
feeling_today = st.selectbox("Select how you're feeling today", feelings)

st.header("Mindful Moment: Take a Break and Relax")
actions = {
    "Happy": "1) Sit comfortably, close your eyes, and focus on your breath. Inhale deeply through your nose, hold for 4 seconds, and exhale slowly through your mouth. (5 minutes)\n2) Write down three things you're grateful for today. Reflect on why they're important. (3 minutes)",
    "Sad": "1) Write down your thoughts and feelings. Allow yourself to process your emotions. (5 minutes)\n2) Sit comfortably, close your eyes, and focus on your breath. Repeat these affirmations: 'I am deserving of love and care.' (5 minutes)",
    "Anxious": "Take a short walk outside, focusing on your surroundings.",
    "Stressed": "Try progressive muscle relaxation to release tension.",
    "Neutral": "Notice your thoughts and emotions without judgment."
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
    st.write("It's okay if you're not feeling better yet. Mental health is a journey!")
else:
    st.write("Remember that it's okay to not be okay. Seek support if needed.")

st.header("Student Depression Assessment")
questions = [
    "Have you experienced any academic pressure or stress in the past semester?",
    "Have you felt overwhelmed by your coursework or responsibilities?",
    "Have you experienced social isolation or loneliness on campus?",
    "Have you felt like you don't belong or are not good enough?",
    "Have you experienced symptoms of depression, such as changes in appetite or sleep patterns?"
]
responses = []
for question in questions:
    response = st.selectbox(question, ["Yes", "No"])
    responses.append(response)

st.header("Analysis and Recommendations")
yes_count = responses.count("Yes")
no_count = responses.count("No")

fig, ax = plt.subplots(figsize=(6, 6))
ax.pie([yes_count, no_count], labels=["Yes", "No"], autopct='%1.1f%%', colors=["#FF6347", "#32CD32"])
ax.axis('equal')
st.pyplot(fig)

if yes_count > 3:
    st.write("You may be experiencing symptoms of depression. We recommend reaching out to a mental health professional.")
elif yes_count > 1:
    st.write("You may be experiencing academic stress. Consider talking to a counselor.")
else:
    st.write("You're doing well! Keep taking care of your mental health.")

st.header("Additional Resources")
st.write("Here are some helpful resources:")
st.write("* National Alliance on Mental Illness (NAMI) Hotline: 1-800-950-6264")
st.write("* Crisis Text Line: Text HOME to 741741")
st.header("Have Happy Moments ;)")

# Load the dataset
file_path = "Student Depression Dataset.csv"  # Ensure the file is in the same directory
data = pd.read_csv(file_path)

# Check for missing values in relevant columns
if data.isnull().any().any():
    st.warning("Following is the Pie based on previous Observation of Student database")

# Plot 1: Pie chart for depression status
depression_counts = data['Depression'].value_counts()
labels = ['No Depression', 'Depression']
colors = ['lightgreen', 'salmon']

fig2, ax2 = plt.subplots(figsize=(6, 6))
ax2.pie(depression_counts, labels=labels, autopct='%1.1f%%', colors=colors)
ax2.axis('equal')
st.pyplot(fig2)

# Add a background color for better visuals
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #F0F8FF;
    }
    .sidebar .sidebar-content {
        background-color: #87CEFA;
    }
    </style>
    """,
    unsafe_allow_html=True
)