import streamlit as st
from pathlib import Path

markdown_content = Path("README.md").read_text()
markdown_content = markdown_content.replace("dataReadme.png", "pfad/zum/bildname.png")
