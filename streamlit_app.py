import streamlit as st
import pandas as pd
import os
from pathlib import Path

# Set page config
st.set_page_config(page_title="Income Dashboard", layout="wide")

st.title("📊 Income Dashboard")
st.write("Analyzing income patterns and trends")

# Load CSV files
@st.cache_data
def load_data():
    """Load all CSV files from the data directory"""
    dataframes = {}
    
    data_dir = Path("data")
    if data_dir.exists():
        for csv_file in data_dir.glob("*.csv"):
            try:
                df_name = csv_file.stem.replace("-", "_").replace(" ", "_")
                dataframes[df_name] = pd.read_csv(csv_file)
                st.success(f"✅ Loaded: {csv_file.name}")
            except Exception as e:
                st.error(f"❌ Failed to load {csv_file.name}: {e}")
    
    return dataframes

dataframes = load_data()

if dataframes:
    selected_dataset = st.selectbox("Select a dataset:", list(dataframes.keys()))
    df = dataframes[selected_dataset]
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Rows", df.shape[0])
    with col2:
        st.metric("Columns", df.shape[1])
    with col3:
        st.metric("Missing Values", df.isnull().sum().sum())
    
    st.subheader("Dataset Preview")
    st.dataframe(df.head(10), use_container_width=True)
    
    st.subheader("Summary Statistics")
    st.dataframe(df.describe(), use_container_width=True)
else:
    st.warning("No CSV files found. Add data to the 'data' folder!")
