import pandas as pd
import random
from datetime import datetime, timedelta

# Function to generate dummy data for a single session
def generate_session():
    session_start = datetime(2024, 2, random.randint(1, 28), random.randint(8, 16), 0)  # Random start time
    session_end = session_start + timedelta(hours=random.randint(1, 3))  # Random session duration (1-3 hours)
    total_time = (session_end - session_start).total_seconds() / 60  # Total session time in minutes
    
    # Random percentage of attentive time (20%-80%)
    attentive_time = random.uniform(20, 80)
    
    # Random percentage of inattentive time (10%-remaining time)
    max_inattentive_time = 100 - attentive_time
    inattentive_time = random.uniform(10, max_inattentive_time)
    
    # Remaining time is neutral
    neutral_time = 100 - (attentive_time + inattentive_time)
    
    return {
        'Session Start': session_start,
        'Session End': session_end,
        'Attentive (%)': attentive_time,
        'Inattentive (%)': inattentive_time,
        'Neutral (%)': neutral_time
    }

# Generate dummy data for multiple sessions
num_sessions = 50
dummy_data = [generate_session() for _ in range(num_sessions)]

# Create DataFrame from dummy data
df = pd.DataFrame(dummy_data)

# Sort sessions by start time
df = df.sort_values(by='Session Start')

# Save DataFrame to CSV
df.to_csv('student_sessions.csv', index=False)

print("CSV file 'student_sessions.csv' has been generated successfully.")
