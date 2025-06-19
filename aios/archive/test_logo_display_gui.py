import streamlit as st
import sys
from pathlib import Path

# ✅ Inject root path so 'gui' becomes importable
sys.path.append(str(Path(__file__).resolve().parents[1]))

from gui.components.logo_display_component import render_logo_box

st.set_page_config(page_title="Logo Display Component Test")

st.markdown("## 🔧 Logo Display Component Test")
st.write("The logo below should appear centered in a white rounded box:")

render_logo_box()
