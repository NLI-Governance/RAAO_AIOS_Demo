import streamlit as st
from PIL import Image
import os

def display_logo():
    logo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'branding', 'logo.png'))
    if os.path.exists(logo_path):
        st.image(logo_path, use_column_width=False, width=160)

def display_abl_footer():
    footer_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'branding', 'ABL_Logo.png'))
    st.markdown("---")
    if os.path.exists(footer_path):
        st.image(footer_path, use_column_width=False, width=120)
