
import matplotlib.pyplot as plt

# Load the dataset
file_path = "Student Depression Dataset.csv"  # Ensure the file is in the same directory or provide the full path
data = pd.rcead_csv(file_path)

# Check for missing values in relevant columns
if data.isnull().any().any():
    print("Warning: Missing values detected. Consider handling them before analysis.")

# Plot 1: Pie chart for depression status
depression_counts = data['Depression'].value_counts()
labels = ['No Depression', 'Depression']
colors = ['lightgreen', 'salmon']

plt.figure(figsize=(8, 8))
plt.pie(
    depression_counts,
    labels=labels,
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=(0, 0.1),  # Slightly offset the 'Depression' slice
)
plt.title('Proportion of Students with Depression')
plt.show()