import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Logo Preview Tool", layout="centered")

st.title("📷 Logo Preview Tool")

logo_path = os.path.expanduser("~/Dropbox/EI_Cloud/ABL_Rev2_6_1_25/assets/branding/logo.png")

if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.subheader("Current System Logo:")
    st.image(logo, width=200, caption="Displayed at 200px width")
    st.image(logo, width=400, caption="Displayed at 400px width")
else:
    st.warning("No logo.png found in branding path.")

st.divider()

st.subheader("Upload a New Logo (optional preview)")
uploaded = st.file_uploader("Upload a PNG logo to preview below", type=["png", "jpg", "jpeg"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, width=200, caption="Uploaded at 200px")
    st.image(img, width=400, caption="Uploaded at 400px")
    st.info("Note: This does not overwrite the system logo. Use Finder to move the new file into branding folder if desired.")
