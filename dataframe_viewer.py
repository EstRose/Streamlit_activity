import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("sample", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Full DataFrame")
    st.dataframe(df)

    if st.checkbox("Show raw data"):
        st.subheader("Raw Data")
        st.write(df)

    column_to_filter = st.selectbox("Select column to filter by", df.columns)
    selected_value = st.selectbox(f"Filter {column_to_filter} by value", df[column_to_filter].unique())
    filtered_df = df[df[column_to_filter] == selected_value]

    st.subheader("Filtered Data")
    st.dataframe(filtered_df)
