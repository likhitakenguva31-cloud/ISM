import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(page_title="Income Dashboard", layout="wide")
st.title("📊 Income Dashboard")
st.write("Analyzing income patterns and trends")

@st.cache_data
def load_data():
    dataframes = {}
    for csv_file in Path(".").glob("*.csv"):
        try:
            df_name = csv_file.stem.replace("-", "_").replace(" ", "_")
            dataframes[df_name] = pd.read_csv(csv_file)
        except Exception as e:
            st.error(f"❌ Error loading {csv_file.name}: {e}")
    return dataframes

dataframes = load_data()

if dataframes:
    selected = st.selectbox("Select dataset:", list(dataframes.keys()))
    df = dataframes[selected]
    st.metric("Rows", df.shape[0])
    st.metric("Columns", df.shape[1])
    st.dataframe(df.head(10), use_container_width=True)
else:
    st.write("No CSV files found")
