import streamlit as st
from pathlib import Path

markdown_content = Path("README.md").read_text()
markdown_content = markdown_content.replace("/dataReadme/network_rechtsextrem.PNG", "../dataReadme/network_rechtsextrem.PNG")
