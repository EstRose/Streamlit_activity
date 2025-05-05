import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# --- DB Connection ---
# Replace with your own credentials
DB_USER = 'your_username'
DB_PASSWORD = 'your_password'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'sample_db'

# MySQL connection string
db_url = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url)

st.title("📊 Streamlit MySQL Data App")

# --- 1. Fetch and Display Data ---
st.header("View Data from Table")

# Optional filtering
table_name = st.text_input("Enter table name", "sample_table")

if st.button("Load Table"):
    try:
        query = text(f"SELECT * FROM {table_name}")
        df = pd.read_sql(query, engine)
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error: {e}")

# --- 2. Insert Data into Table ---
st.header("Insert New Row")

with st.form("Insert Form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Name")
    with col2:
        age = st.number_input("Age", min_value=0, step=1)

    submitted = st.form_submit_button("Insert Row")
    if submitted:
        try:
            insert_query = text("INSERT INTO sample_table (name, age) VALUES (:name, :age)")
            with engine.connect() as conn:
                conn.execute(insert_query, {"name": name, "age": age})
                conn.commit()
            st.success("✅ Row inserted successfully.")
        except Exception as e:
            st.error(f"Error inserting row: {e}")

# --- 3. Custom SQL Query ---
st.header("Run Custom SQL Query")

user_query = st.text_area("Enter your SQL query")
if st.button("Execute Query"):
    try:
        df_query = pd.read_sql(text(user_query), engine)
        st.dataframe(df_query)
    except Exception as e:
        st.error(f"Query failed: {e}")
