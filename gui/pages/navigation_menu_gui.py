import streamlit as st

st.set_page_config(page_title="Navigation Menu", layout="wide")

def main():
    st.title("📁 AIOS Navigation Menu")
    st.markdown("Use this dashboard to explore available RAAO system modules.")
    
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("HR Modules")
        st.button("🧍 Employee Application")
        st.button("📋 Training Tracker")
        st.button("📝 Disciplinary Log")

    with col2:
        st.subheader("Grants & Programs")
        st.button("💸 Grant Funding Code Manager")
        st.button("📊 Grant Tracker")
        st.button("🧠 AI Policy Assistant")

    st.markdown("---")
    st.markdown("⚙️ Admin access available in footer panel.")

if __name__ == "__main__":
    main()
