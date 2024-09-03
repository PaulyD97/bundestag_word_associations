import streamlit as st
from pathlib import Path

markdown_content = Path("README.md").read_text()
st.markdown(markdown_content)

st.image("../dataReadme/network_rechtsextrem.PNG")
