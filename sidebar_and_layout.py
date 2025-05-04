import streamlit as st
import pandas as pd

# Title and description
st.title("Data Warehousing and Enterprise Data Management")
st.markdown("This dashboard demonstrates layout organization using Streamlit. The content is based on data warehousing practices.")

# Sidebar Filters
st.sidebar.header("Filter Options")

# Simulated dataset
data = {
    "Department": ["Sales", "HR", "IT", "Finance", "Sales", "IT", "HR", "Finance"],
    "Data Source": ["CRM", "HRMS", "ERP", "Accounting", "CRM", "ERP", "HRMS", "Accounting"],
    "Records": [1000, 800, 1500, 1200, 1100, 1400, 750, 1300]
}

df = pd.DataFrame(data)

# Sidebar filter
selected_dept = st.sidebar.multiselect("Select Department", options=df["Department"].unique(), default=df["Department"].unique())

# Filtered DataFrame
filtered_df = df[df["Department"].isin(selected_dept)]

# Tabs for content sections
tab1, tab2 = st.tabs(["Overview", "Data Table"])

with tab1:
    st.subheader("What is Data Warehousing?")
    st.write("""
        A data warehouse is a central repository of integrated data from multiple sources. 
        It stores current and historical data and is used for reporting and data analysis. 
        Enterprise Data Management (EDM) ensures that data is accurate, consistent, and accessible across the organization.
    """)

    st.subheader("Enterprise Data Management Practices")
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**✓ Data Governance**")
        st.markdown("**✓ Metadata Management**")
        st.markdown("**✓ Master Data Management (MDM)**")

    with col2:
        st.markdown("**✓ Data Integration**")
        st.markdown("**✓ Data Quality Management**")
        st.markdown("**✓ Data Security**")

with tab2:
    st.subheader("Filtered Data from Departments")
    st.dataframe(filtered_df)

# Expander Section
with st.expander("📊 Data Warehouse Metrics Summary"):
    st.write(f"**Total Records:** {filtered_df['Records'].sum()}")
    st.write(f"**Average Records per Department:** {filtered_df['Records'].mean():.2f}")
    st.bar_chart(filtered_df.set_index("Department")["Records"])

with st.expander("📚 Additional Resources"):
    st.markdown("""
    - [Data Warehouse Concepts - Oracle](https://docs.oracle.com/en/)
    - [What is Enterprise Data Management? - IBM](https://www.ibm.com/topics/enterprise-data-management)
    - [Best Practices for Data Integration](https://www.informatica.com/)
    """)

