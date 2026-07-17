import streamlit as st
from PIL import Image


def show_login():

    st.markdown("""
    <style>

    .login-title{
        text-align:center;
        font-size:42px;
        font-weight:bold;
        color:#0F172A;
    }

    .subtitle{
        text-align:center;
        color:gray;
        margin-bottom:25px;
        font-size:20px;
    }

    div.stButton > button{
        width:100%;
        height:48px;
        border-radius:12px;
        background:#2563EB;
        color:white;
        font-size:18px;
        border:none;
    }

    div.stButton > button:hover{
        background:#1D4ED8;
        color:white;
    }

    </style>
    """, unsafe_allow_html=True)

    left, right = st.columns([1.2,1])

    with left:

        image = Image.open("images/login.png")
        st.image(image, use_container_width=True)

    with right:

        st.markdown("<div class='login-title'>HELLO USER,Lets Login</div>", unsafe_allow_html=True)

        st.markdown("<div class='subtitle'>RespiCare AI Portal</div>", unsafe_allow_html=True)

        username = st.text_input(
            "👤 Username",
            placeholder="Enter Username"
        )

        password = st.text_input(
            "🔒 Password",
            placeholder="Enter Password",
            type="password"
        )

        remember = st.checkbox("Remember Me")

        st.write("")

        if st.button("Login"):

            if username == "admin" and password == "admin123":

                st.success("Login Successful!")

                st.session_state.page = "dashboard"

                st.rerun()

            else:

                st.error("Invalid Username or Password")

        st.write("")

        if st.button("⬅ Back"):

            st.session_state.page = "home"

            st.rerun()