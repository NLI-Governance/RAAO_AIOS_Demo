import streamlit as st

st.set_page_config(page_title="NDA Gate")

st.title("NDA Access Gateway")
st.markdown("By clicking agree, you confirm that you understand the NDA requirements.")

if st.button("Agree and Continue"):
    st.switch_page("navigation_menu_gui.py")  # ✅ Correct: uses filename, not display title
