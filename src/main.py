
import streamlit as st
import pandas as pd
import sqlite3
from datetime import datetime
import classfier

# SQLite setup
conn = sqlite3.connect('feelings.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS feelings (date TEXT, text TEXT, category TEXT)''')
conn.commit()

# Streamlit UI
st.title("Daily Feelings Tracker")
st.write("Track how you feel every day.")

# Input text
feeling_text = st.text_input("How are you feeling today?")

if st.button("Categorize and Save"):
    if feeling_text:
        categories = classfier.categorize_feeling(feeling_text)
        today = datetime.now().strftime("%Y-%m-%d")
        
        # Save to SQLite
        for category in categories:
            category = category.strip()
            c.execute("INSERT INTO feelings (date, text, category) VALUES (?, ?, ?)", 
                    (today, feeling_text, category))
            conn.commit()
        
            st.success(f"Your feeling has been categorized as: {category}")
    else:
        st.warning("Please enter a feeling.")

# Display saved feelings
if st.button("View Feelings History"):
    df = pd.read_sql_query("SELECT * FROM feelings", conn)
    st.write(df)