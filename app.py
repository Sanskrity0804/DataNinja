import streamlit as st
from data_analyzer import SmartDataExplorer

st.title("📊 Smart Data Explorer")
uploaded_file = st.file_uploader("Upload CSV file", type="csv")

if uploaded_file:
    try:
        analyzer = SmartDataExplorer(uploaded_file)
        
        st.subheader("🔍 Data Summary")
        st.json(analyzer.analyze())  # Use st.json for cleaner output
        
        column = st.selectbox("Select a column", analyzer.df.columns)
        st.plotly_chart(analyzer.plot(column))
        
    except Exception as e:
        st.error(f"Error: {e}")  # Show errors to the user