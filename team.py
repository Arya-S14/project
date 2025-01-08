import streamlit as st
import random
import matplotlib.pyplot as plt
import pandas as pd

# Title and introduction
st.title("Mindful Moments !!!! ")
st.write("Welcome to Mindful Moments! Taking Care Of Your Mental Health")

# User input: How are you feeling today?
name = st.text_input("What's Your Name ?")
if name:
    st.write(f"Hello {name} !!!")
age = st.slider("What's Your Age ", 12, 32, 20)
st.write(f"Your Age: {age}")
st.write("What is Your Gender")
gender = st.radio("Choose", ["Male", "Female", "Others"])

st.header("Check-in: How Are You Feeling Today?")
feelings = ["Happy", "Sad", "Anxious", "Stressed", "Neutral"]
feeling_today = st.selectbox("Select how you're feeling today", feelings)

st.header("Mindful Moment: Take a Break and Relax")
actions = {
    "Happy": "1) Sit comfortably, close your eyes, and focus on your breath. Inhale deeply through your nose, hold for 4 seconds, and exhale slowly through your mouth. (5 minutes)\n \n2) Write down three things you're grateful for today.",
    "Sad": "1) Write down your thoughts and feelings without editing or judgment.\n \n2) Sit comfortably, close your eyes, and focus on your breath. Repeat positive affirmations.",
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
    st.write("It's okay if you're not feeling better yet. Remember that mental health is a journey.")
else:
    st.write("If you're feeling overwhelmed, don't hesitate to reach out to a mental health professional.")

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
    response = st.selectbox(question, ["Yes", "No"], key=question)
    responses.append(response)

st.header("Analysis and Recommendations")
yes_count = responses.count("Yes")
no_count = responses.count("No")

fig, ax = plt.subplots()
ax.pie([yes_count, no_count], labels=["Yes", "No"], autopct='%1.1f%%', colors=['salmon', 'lightgreen'])
ax.axis('equal')
st.pyplot(fig)

if yes_count > 3:
    st.write("You may be experiencing some symptoms of depression. We recommend reaching out to a mental health professional for support.")
elif yes_count > 1:
    st.write("You may be experiencing some academic stress or pressure. We recommend talking to an academic advisor or counselor for support.")
else:
    st.write("You seem to be doing well! Keep up the good work and prioritize your mental health.")

st.header("Additional Resources")
st.write("If you're struggling with your mental health, here are some additional resources:")
st.write("* National Alliance on Mental Illness (NAMI) Hotline: 1-800-950-6264")
st.write("* Crisis Text Line: Text HOME to 741741")

st.header("Dataset Analysis")
# Load the dataset
file_path = "/mnt/data/Student Depression Dataset.csv"  # Uploaded file path
data = pd.read_csv(file_path)

# Check for missing values and handle them
if data.isnull().any().any():
    st.warning("Missing values detected. Handling them automatically by filling categorical values with mode and numerical values with median.")
    for column in data.columns:
        if data[column].dtype == 'object':
            data[column].fillna(data[column].mode()[0], inplace=True)
        else:
            data[column].fillna(data[column].median(), inplace=True)

# Display dataset summary
st.write("Dataset Summary:")
st.write(data.describe(include='all'))

# Plot: Depression status distribution
st.subheader("Depression Status Distribution")
depression_counts = data['Depression'].value_counts()
fig2, ax2 = plt.subplots()
ax2.bar(depression_counts.index, depression_counts.values, color=['lightgreen', 'salmon'])
ax2.set_xlabel("Depression Status")
ax2.set_ylabel("Count")
ax2.set_title("Distribution of Depression Status")
st.pyplot(fig2)

# Plot: Age distribution of students
st.subheader("Age Distribution")
if 'Age' in data.columns and pd.api.types.is_numeric_dtype(data['Age']):
    fig3, ax3 = plt.subplots()
    ax3.hist(data['Age'], bins=10, color='skyblue', edgecolor='black')
    ax3.set_xlabel("Age")
    ax3.set_ylabel("Count")
    ax3.set_title("Age Distribution of Students")
    st.pyplot(fig3)
else:
    st.warning("Age column is missing or not numeric. Cannot plot age distribution.")

st.header("Have Happy Moments ;) ")
