import streamlit as st
import os

def display_logo():
    """Display the RAAO logo from the confirmed branding path."""
    logo_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'branding', 'logo.png'))
    if os.path.exists(logo_path):
        st.image(logo_path, width=160)
    else:
        st.warning("⚠️ RAAO logo not found at /assets/branding/logo.png")

def display_abl_footer():
    """Display the ABL logo from the same branding path."""
    abl_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'branding', 'ABL_Logo.png'))
    if os.path.exists(abl_path):
        st.markdown("<br><hr style='border-color: #444;'>", unsafe_allow_html=True)
        st.image(abl_path, width=60)
        st.markdown("<small style='opacity: 0.7;'>Adaptive Bespoke Learning</small>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ ABL logo not found at /assets/branding/ABL_Logo.png")

def display_gui_version(gui_name, version="v1.0"):
    st.markdown(
        f"""
        <div style='text-align:right; font-size: 0.75rem; color: gray; margin-top: 1rem;'>
            🆔 <code>{gui_name} {version}</code>
        </div>
        """,
        unsafe_allow_html=True
    )

def display_language_toggle_button():
    st.selectbox("🌐 Language", ["English", "Español", "Français"], key="language_toggle")

def display_policy_assistant_button():
    with st.expander("💬 Ask a question", expanded=False):
        user_q = st.text_input("Ask a question about policy or procedure:")
        if user_q:
            st.info("🔧 Assistant module under development.")

def display_about_this_form(header, purpose, usage, routing):
    with st.expander("📖 About this form"):
        st.markdown(f"**Who is this for?**  \n{header}")
        st.markdown(f"**Purpose**  \n{purpose}")
        st.markdown(f"**How to use it**  \n{usage}")
        st.markdown(f"**What happens after submission**  \n{routing}")
