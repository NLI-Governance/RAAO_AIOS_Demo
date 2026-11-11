import streamlit as st
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


def display_language_selector():
    """Keep the preferred language across reruns; translations are not wired up."""
    return st.selectbox(
        "🌐 Language", ["English", "Español", "Français"], key="language_toggle"
    )


def display_about_section(description):
    """Show page-specific guidance using the common form layout."""
    with st.expander("📖 About this form"):
        st.write(description)


def display_assistant_panel():
    """Render the demo assistant without requiring optional AI services."""
    with st.expander("💬 Need help?", expanded=False):
        st.caption("The AI assistant is not configured in this demo.")
        question = st.text_input("Ask a question about policy or procedure:")
        if question:
            st.info("Please contact your supervisor or HR for assistance.")
