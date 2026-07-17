import streamlit as st
from database import create_table
from pages.analytics import show_analytics

# ----------------------------
# Page Configuration
# ----------------------------

st.set_page_config(
    page_title="RespiCare AI",
    page_icon="🫁",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------------
# Hide Streamlit Menu
# ----------------------------

hide_streamlit_style = """
<style>

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

[data-testid="stSidebar"]{
    display:none;
}

.block-container{
    padding-top:1rem;
}

</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ----------------------------
# Import Pages
# ----------------------------

from pages.home import show_home
from pages.login import show_login
from pages.dashboard import show_dashboard
from pages.prediction import show_prediction
from pages.records import show_records
from pages.staff import show_staff
from pages.about import show_about
from pages.review import show_review

# ----------------------------
# Session State
# ----------------------------

if "page" not in st.session_state:
    st.session_state.page = "home"

# Create the database and table if they don't exist
create_table()
# ----------------------------
# Navigation
# ----------------------------

page = st.session_state.page

if page == "home":
    show_home()

elif page == "login":
    show_login()

elif page == "dashboard":
    show_dashboard()

elif page == "prediction":
    show_prediction()

elif page == "records":
    show_records()

elif page == "staff":
    show_staff()

elif page == "about":
    show_about()

elif page == "review":
    show_review()

elif page == "analytics":
    show_analytics()

else:
    st.session_state.page = "home"
    st.rerun()