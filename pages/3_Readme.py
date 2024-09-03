import streamlit as st
from pathlib import Path

absolute_path = Path("dataReadme/network_rechtsextrem.PNG").resolve()

markdown_content = Path("README.md").read_text()
markdown_content = markdown_content.replace("dataReadme/network_rechtsextrem.PNG", "network_rechtsextrem.PNG")

st.markdown(markdown_content)

st.image(str(absolute_path))
