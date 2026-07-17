import streamlit as st
import base64


# ==========================================
# Background Image
# ==========================================

def set_background():

    with open("images/welcome.png", "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

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

        [data-testid="stSidebar"] {{
            display:none;
        }}

        .title {{
            text-align:center;
            color:white;
            font-size:55px;
            font-weight:bold;
        }}

        .subtitle {{
            text-align:center;
            color:white;
            font-size:24px;
            margin-top:-10px;
        }}

        div.stButton > button {{
            width:100%;
            height:55px;
            border-radius:15px;
            background:#6C63FF;
            color:white;
            font-size:22px;
            font-weight:bold;
            border:none;
        }}

        div.stButton > button:hover {{
            background:#5444E5;
            color:white;
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


# ==========================================
# Home Page
# ==========================================

def show_home():

    set_background()

    st.write("")

    col1, col2 = st.columns([6,2])

    with col1:
        st.markdown(
            "<div class='title'>🫁 RespiDiagnosis AI</div>",
            unsafe_allow_html=True
        )

    with col2:

        language = st.selectbox(
            "🌍 Language",
            [
                "English",
                "हिन्दी",
                "मराठी"
            ]
        )

    st.write("")

    left, center, right = st.columns([1,2,1])

    with center:

        st.video(
            "images/animations/Online Doctor.mp4",
            autoplay=True,
            muted=True,
            loop=True,
            width=100
        )

    st.markdown(
        "<div class='subtitle'>Welcome To RespiDiagnosis AI</div>",
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <h4 style="text-align:center;color:white;">
        Breathing is Nature's Greatest Gift.<br>
        Let's Protect It Together.
        </h4>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    # ==========================================
    # Heart Animation & Welcome
    # ==========================================

    st.write("")

    c1, c2 = st.columns([1, 4])

    with c1:
        st.video(
            "images/animations/heart loading.mp4",
            autoplay=True,
            muted=True,
            loop=True,
            width=100
        )

    with c2:

        st.success("❤️ AI Powered Respiratory Disease Detection System")

        if language == "English":

            st.info(
                "Welcome! Please click Get Started to continue."
            )

            # Uncomment after testing
            # st.audio("images/audios/english audio welcome.mp3")

        elif language == "हिन्दी":

            st.info(
                "स्वागत है! आगे बढ़ने के लिए Get Started दबाएँ।"
            )

            # st.audio("images/audios/hindi audio welcome.mp3")

        else:

            st.info(
                "स्वागत आहे! पुढे जाण्यासाठी Get Started वर क्लिक करा."
            )

            # st.audio("images/audios/marathi audio welcome.mp3")

    st.write("")
    st.write("")

    # ==========================================
    # Get Started Button
    # ==========================================

    left, center, right = st.columns([2, 2, 2])

    with center:

        if st.button(
                "🚀 Get Started",
                use_container_width=True
        ):
            st.session_state.page = "login"

            st.rerun()

    st.write("")
    st.divider()

    # ==========================================
    # Footer
    # ==========================================

    footer1, footer2 = st.columns([1, 5])

    with footer1:



        st.markdown("""
    ### 🫁 AI Powered Respiratory Care

    ✔ Early Disease Detection

    ✔ Voice Assisted Diagnosis

    ✔ Rural Healthcare Friendly

    ✔ Doctor Recommendation

    ✔ Fast PDF Reports
    """)

    st.write("")

    st.caption(
        "© 2026 RespiDiagnosis AI | Final Year BE Project"
    )