import streamlit as st
from pathlib import Path

st.markdown(read_markdown_file(Path("README.md").read_text()))
