import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="COVID-19 Global Stats", layout="wide")

# Title
st.title("🌍 COVID-19 Global Stats Dashboard")
st.markdown("This dashboard fetches data from a public API and visualizes it with multiple chart types.")

# Fetch API data
url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    st.error("Failed to fetch data.")
    st.stop()

# Parse JSON data
df = pd.json_normalize(data)
df = df[["country", "cases", "todayCases", "deaths", "todayDeaths", "recovered", "active", "critical", "tests", "population"]]

# Sidebar filter
st.sidebar.header("Filter Options")
top_n = st.sidebar.slider("Select number of countries", min_value=5, max_value=50, value=10)

# Filtered DataFrame
top_df = df.sort_values("cases", ascending=False).head(top_n)

# Show data
st.subheader("Top Countries by Total Cases")
st.dataframe(top_df)

# Chart 1: Bar Chart - Total Cases
st.subheader("Bar Chart - Total Cases")
st.bar_chart(top_df.set_index("country")["cases"])

# Chart 2: Line Chart - Recovered Cases
st.subheader("Line Chart - Recovered Cases")
st.line_chart(top_df.set_index("country")["recovered"])

# Chart 3: Area Chart - Active Cases
st.subheader("Area Chart - Active Cases")
st.area_chart(top_df.set_index("country")["active"])

# Chart 4: Deaths Comparison using st.bar_chart
st.subheader("Bar Chart - Total Deaths")
st.bar_chart(top_df.set_index("country")["deaths"])

# Chart 5: Horizontal Table (instead of pie)
st.subheader("Table - Top 5 Countries by Deaths")
st.table(top_df.sort_values("deaths", ascending=False).head(5)[["country", "deaths"]])
