import streamlit as st

# Title of the dashboard
st.title('My Streamlit Dashboard')

# Display the current date and time
st.write("Current Date and Time (UTC):", "2026-03-27 22:36:38")

# Add a text input
user_input = st.text_input('Enter some text')

# Display the user input
if user_input:
    st.write('You entered:', user_input)