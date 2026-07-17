import streamlit as st
import base64


# ==========================================
# Background
# ==========================================

def set_background():

    with open("images/welcome.png", "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>

        .stApp {{
            background-image:url("data:image/png;base64,{encoded}");
            background-size:cover;
            background-position:center;
            background-repeat:no-repeat;
            background-attachment:fixed;
        }}

        header {{
            visibility:hidden;
        }}

        footer {{
            visibility:hidden;
        }}

        #MainMenu {{
            visibility:hidden;
        }}

        [data-testid="stSidebar"]{{
            display:none;
        }}

        .title{{
            text-align:center;
            color:white;
            font-size:45px;
            font-weight:bold;
        }}

        .subtitle{{
            text-align:center;
            color:white;
            font-size:20px;
        }}

        div.stButton > button{{
            width:100%;
            height:120px;
            border-radius:18px;
            background:white;
            color:#4F46E5;
            font-size:22px;
            font-weight:bold;
            border:2px solid #4F46E5;
        }}

        div.stButton > button:hover{{
            background:#4F46E5;
            color:white;
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )


# ==========================================
# Dashboard
# ==========================================

def show_dashboard():

    set_background()

    st.markdown(
        "<div class='title'>🫁 RespiDiagnosis AI Dashboard</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<div class='subtitle'>AI Powered Respiratory Disease Detection</div>",
        unsafe_allow_html=True
    )

    st.write("")

    col1, col2 = st.columns([2,1])

    with col1:
        st.success("👋 Welcome, Admin")

    with col2:
        st.selectbox(
            "🌍 Language",
            ["English","हिन्दी","मराठी"]
        )

    st.write("")

    # Center Animation

    c1, c2, c3 = st.columns([1,5,1])

    with c2:

        st.video(
            "images/animations/doctor playing lungs.mp4",
            autoplay=True,
            muted=True,
            loop=True,width=100
        )

    st.write("")
    # ==========================================
    # Dashboard Buttons
    # ==========================================

    st.write("")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🎤\n\nNew Diagnosis", use_container_width=True):
            st.session_state.page = "prediction"
            st.rerun()

    with col2:
        if st.button("📋\n\nPrevious Records", use_container_width=True):
            st.session_state.page = "records"
            st.rerun()

    with col3:
        if st.button("👨‍⚕️\n\nDoctors", use_container_width=True):
            st.session_state.page = "staff"
            st.rerun()

    st.write("")

    col4, col5, col6, col7 = st.columns(4)

    with col4:
        if st.button("📄\n\nReviews", use_container_width=True):
            st.session_state.page = "review"
            st.rerun()

    with col5:
        if st.button("📊\n\nAI Analytics", use_container_width=True):
            st.session_state.page = "analytics"
            st.rerun()

    with col6:
        if st.button("ℹ️\n\nAbout", use_container_width=True):
            st.session_state.page = "about"
            st.rerun()

    with col7:
        if st.button("🚪\n\nLogout", use_container_width=True):
            st.session_state.page = "home"
            st.rerun()
    st.write("")
    st.divider()

    # ==========================================
    # Bottom Section
    # ==========================================

    left, right = st.columns([1, 4])

    with left:
        st.video(
            "images/animations/women pointing at lungs.mp4",
            autoplay=True,
            muted=True,
            loop=True,
            width=100
        )

    with right:

        st.markdown(
            """
### 🫁 AI Powered Healthcare Assistant

✔ Early Detection of Respiratory Diseases

✔ Voice Guided Diagnosis

✔ PDF Medical Report

✔ Wikipedia Disease Information

✔ Recommended Doctors

✔ Rural Healthcare Support

✔ Hindi • English • Marathi Support
"""
        )

    st.write("")
    st.divider()

    st.markdown(
        """
<div style="text-align:center;color:white;font-size:18px;">
Developed with ❤️ for Rural Healthcare using Artificial Intelligence
</div>
""",
        unsafe_allow_html=True,
    )

    st.caption(
        "© 2026 RespiDiagnosis AI | Final Year BE Project"
    )