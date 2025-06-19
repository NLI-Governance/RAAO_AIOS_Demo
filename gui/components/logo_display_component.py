import streamlit as st

def render_logo_box():
    box_style = """
        <div style='
            background-color: #fdfdfd;
            border-radius: 12px;
            width: 150px;
            height: 100px;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 0 auto;
            box-shadow: 0 0 6px rgba(0,0,0,0.1);
        '>
            <img src='assets/branding/logo.png' style='max-height: 90%; max-width: 90%;'/>
        </div>
    """
    st.markdown(box_style, unsafe_allow_html=True)
