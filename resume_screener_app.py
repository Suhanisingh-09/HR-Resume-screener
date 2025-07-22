import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Title
st.title("AI-Powered Resume Screening (HR ATS Demo)")

# Define keywords for HR role
job_keywords = [
    "HRM", "recruitment", "onboarding", "employee engagement",
    "Excel", "communication", "teamwork", "conflict resolution",
    "interview scheduling", "HR policies"
]

# Function to calculate match
def calculate_match(resume_text, keywords):
    resume_text = resume_text.lower()
    match_count = 0
    for word in keywords:
        if word.lower() in resume_text:
            match_count += 1
    return round((match_count / len(keywords)) * 100, 2)

# File uploader
uploaded_files = st.file_uploader("Upload Resume Files (.txt)", type="txt", accept_multiple_files=True)

if uploaded_files:
    results = []
    for file in uploaded_files:
        content = file.read().decode("utf-8")
        score = calculate_match(content, job_keywords)
        results.append({"Resume": file.name, "Match Score (%)": score})

    df = pd.DataFrame(results)
    df = df.sort_values(by="Match Score (%)", ascending=False).reset_index(drop=True)
    st.subheader("Ranking Table")
    st.dataframe(df)

# Bar Chart
st.subheader("📊 Match Score Chart")

import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
fig, ax = plt.subplots()
sns.barplot(x="Match Score (%)", y="Resume", data=df, palette="coolwarm", ax=ax)
st.pyplot(fig)



