import streamlit as st
import tempfile
import os
from agent import CSVAnalyzer

# Set page config
st.set_page_config(
    page_title="CSV Analysis Assistant",
    page_icon="📊",
    layout="wide"
)

# Initialize session state
if 'analyzer' not in st.session_state:
    st.session_state.analyzer = CSVAnalyzer()
if 'csv_loaded' not in st.session_state:
    st.session_state.csv_loaded = False

# Title and description
st.title("📊 CSV Analysis Assistant")
st.markdown("""
    Upload your CSV file and ask questions about your data. The AI will help you analyze it!
""")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Save the uploaded file to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as tmp_file:
        tmp_file.write(uploaded_file.getvalue())
        tmp_file_path = tmp_file.name
    
    # Load CSV and initialize agent
    success, message = st.session_state.analyzer.load_csv(tmp_file_path)
    if success:
        st.success(message)
        success, message = st.session_state.analyzer.initialize_agent()
        if success:
            st.session_state.csv_loaded = True
            st.success(message)
        else:
            st.error(message)
    else:
        st.error(message)
    
    # Clean up the temporary file
    os.unlink(tmp_file_path)

# Question input
if st.session_state.csv_loaded:
    question = st.text_input("Ask a question about your data:", 
                           placeholder="e.g., What is the average value in column X?")
    
    if question:
        with st.spinner("Analyzing your data..."):
            success, response = st.session_state.analyzer.analyze(question)
            if success:
                st.success("Analysis Complete!")
                st.write(response)
            else:
                st.error(response)
else:
    st.info("Please upload a CSV file to begin analysis.") 