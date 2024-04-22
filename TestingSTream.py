import streamlit as st

# Define a function to display the value
def display_value(value):
    st.write("The current value is:", value)

# Main code
if __name__ == "__main__":
    # Create a slider widget
    value = st.slider("Select a value", min_value=0, max_value=100)

    # Call the function to display the value
    display_value(value)
