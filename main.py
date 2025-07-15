import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
from agents.web_agent import run_web_search
from agents.code_agent import run_code_execution
from agents.document_agent import run_document_parser
from agents.browser_agent import simulate_browser_actions

st.set_page_config(page_title="SRI-Inspired Agent System", layout="wide")

st.title("🤖 SRI-Inspired Modular AI Agent System")

task = st.sidebar.selectbox(
    "Select Agent",
    ["Web Agent", "Code Agent", "Document Agent", "Browser Agent"]
)

if task == "Web Agent":
    query = st.text_input("Enter your query for web search")
    if st.button("Search"):
        results = run_web_search(query)
        for r in results:
            st.write(f"- {r['title']}: {r['href']}")

elif task == "Code Agent":
    code = st.text_area("Write Python code to execute")
    if st.button("Run Code"):
        output = run_code_execution(code)
        st.code(output)

elif task == "Document Agent":
    uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "xlsx"])
    if uploaded_file:
        parsed = run_document_parser(uploaded_file)
        st.text_area("Parsed Output", parsed, height=300)

elif task == "Browser Agent":
    st.info("Browser automation placeholder - requires headless environment.")
    if st.button("Run Simulated Browser Actions"):
        output = simulate_browser_actions()
        st.write(output)
