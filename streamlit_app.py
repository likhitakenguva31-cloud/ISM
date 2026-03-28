import streamlit as st
import pandas as pd

# Load data
@st.cache
def load_data():
    df = pd.read_csv('data/refugee_data.csv')  # Assuming a CSV file
    return df

data = load_data()

# App Title
st.title('Refugee Mental Health Dashboard')

# Overview Tab
st.header('Overview')
st.write('This dashboard provides insights into the mental health of refugees.')

# Migration Trauma Factors Tab
st.header('Migration Trauma Factors')
trauma_factors = data['trauma_factors']  # Example column
st.bar_chart(trauma_factors.value_counts())

# Policy Impact Tab
st.header('Policy Impact')
policy_impact = data['policy_impact']  # Example column
st.line_chart(policy_impact)

# Interactive Elements
if st.checkbox('Show Raw Data'):
    st.subheader('Raw Data')
    st.write(data)
