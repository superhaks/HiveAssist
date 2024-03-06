"""Report components [3 pages PDF report]:
    1. Heading
    2. Overall Stats
    3. Hive Attention Status (HAS) bar chart
    4.
    5. Summary
"""
# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the dummy data
# df = pd.read_csv('student_sessions.csv')

# # Function to generate pie chart

# def generate_pie_chart(data):
#     labels = ['Attentive', 'Inattentive', 'Neutral']
#     sizes = [data['Attentive (%)'], data['Inattentive (%)'], data['Neutral (%)']]
#     explode = (0.1, 0, 0)  # explode 1st slice

#     # Plotting the pie chart with black background
#     fig1, ax1 = plt.subplots(facecolor='black')
#     ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90, colors=['green', 'red', 'blue'])
#     ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

#     # Set text color to white
#     plt.setp(ax1.get_yticklabels(), color='white')
#     plt.setp(ax1.get_xticklabels(), color='white')

#     # Displaying the pie chart
#     st.pyplot(fig1)


# # Streamlit UI
# st.title('Student Session Analysis')

# # Select session
# selected_session = st.selectbox('Select Session', df.index + 1)

# # Check if selected session index is valid
# if selected_session >= 1 and selected_session <= len(df):
#     # Display the selected session's data
#     st.write("## Session", selected_session)
#     session_data = df.loc[selected_session - 1]
#     st.write(session_data)

#     # Generate and display the pie chart for the selected session
#     st.write("## Pie Chart for Session", selected_session)
#     generate_pie_chart(session_data)
# else:
#     st.write("Invalid session selected.")

import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

# Load the dummy data
df = pd.read_csv('student_sessions.csv')

# Function to generate interactive pie chart
def generate_pie_chart(data):
    labels = ['Attentive', 'Inattentive', 'Neutral']
    values = [data['Attentive (%)'], data['Inattentive (%)'], data['Neutral (%)']]
    
    # Create a DataFrame for the pie chart
    pie_df = pd.DataFrame({'labels': labels, 'values': values})
    
    # Plot interactive pie chart
    fig = px.pie(pie_df, values='values', names='labels', 
                 title='Session Distribution', 
                 hover_data=['values'], 
                 labels={'labels': 'Category', 'values': 'Percentage'},
                 hole=0.4)
    
    # Update hover text
    fig.update_traces(textposition='inside', textinfo='percent+label')
    
    # Update layout
    fig.update_layout(font=dict(color='white'), plot_bgcolor='black')
    
    # Display the interactive pie chart
    st.plotly_chart(fig)

# Function to generate bar chart
def generate_bar_chart(data):
    st.bar_chart(data[['Attentive (%)', 'Inattentive (%)', 'Neutral (%)']])

# Function to generate area chart
def generate_area_chart(data):
    st.area_chart(data[['Attentive (%)', 'Inattentive (%)', 'Neutral (%)']])

# Streamlit UI
st.title('Student Session Analysis')

# Select session
selected_session = st.selectbox('Select Session', df.index + 1)

# Multiselect for chart type
chart_types = st.multiselect('Select Chart Type', ['Pie Chart', 'Bar Chart', 'Area Chart'])

# Check if selected session index is valid
if selected_session >= 1 and selected_session <= len(df):
    # Display the selected session's data
    st.write("## Session", selected_session)
    session_data = df.loc[selected_session - 1]
    st.write(session_data)

    # Generate and display charts based on selected chart types
    for chart_type in chart_types:
        st.write(f"## {chart_type} for Session {selected_session}")
        if chart_type == 'Pie Chart':
            generate_pie_chart(session_data)
        elif chart_type == 'Bar Chart':
            generate_bar_chart(session_data)
        elif chart_type == 'Area Chart':
            generate_area_chart(session_data)
else:
    st.write("Invalid session selected.")


