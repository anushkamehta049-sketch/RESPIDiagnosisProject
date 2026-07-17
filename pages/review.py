import streamlit as st
import pandas as pd
from datetime import datetime
import os


# ==========================================
# REVIEW PAGE
# ==========================================

def show_review():

    st.title("💬 Reviews & Testimonials")

    st.write(
        "Explore what our MBBS students and patients say about "
        "RespiDiagnosis AI."
    )

    st.markdown("---")

    # ==========================================
    # MBBS STUDENT TESTIMONIALS
    # ==========================================

    st.header("🎥 Video Testimonials from MBBS Students")

    st.info(
        "These testimonials were voluntarily shared by MBBS students "
        "after reviewing RespiDiagnosis AI for educational purposes."
    )

    # ---------------- Student 1 ----------------

    st.subheader("👩‍⚕️ Yogeshwari Upadhyay")

    col1, col2 = st.columns([1, 2])

    with col1:

        st.video("images/review/student1.mp4")

    with col2:

        st.write("🎓 MBBS Final Year Student")

        st.write("⭐⭐⭐⭐⭐")

        st.success(
            "RespiDiagnosis AI is easy to use and provides "
            "quick cough analysis. The report generation "
            "feature is excellent."
        )

    st.markdown("---")

    # ---------------- Student 2 ----------------

    st.subheader("👨‍⚕️ Shreya Shejul")

    col1, col2 = st.columns([1, 2])

    with col1:

        st.video("images/review/student2.mp4")

    with col2:

        st.write("🎓 MBBS 3rd year student")

        st.write("⭐⭐⭐⭐⭐")

        st.success(
            "The interface is very user-friendly. "
            "The AI prediction system and disease "
            "information are useful for preliminary screening."
        )

    st.markdown("---")

    # ---------------- Student 3 ----------------

    st.subheader("👩‍⚕️ Vaishnavi Chavan")

    col1, col2 = st.columns([1, 2])



    with col2:

        st.write("🎓 Third Year MBBS Student")

        st.write("⭐⭐⭐⭐⭐")

        st.success(
            "A well-developed healthcare project. "
            "Patient reports, cough analysis, and disease "
            "education make this application very impressive."
        )

    st.markdown("---")

    st.warning(
        "Disclaimer: These testimonials represent the personal opinions "
        "of MBBS students who evaluated the application for academic and "
        "demonstration purposes. RespiDiagnosis AI is intended only for "
        "preliminary screening and educational support."
    )

    st.markdown("---")

    # ==========================================
    # PATIENT REVIEW FORM
    # ==========================================

    st.header("⭐ Patient Feedback")

    st.write(
        "Your valuable feedback helps us improve "
        "RespiDiagnosis AI."
    )

    with st.form("review_form"):

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
                "Patient Name (Optional)"
            )

            age = st.number_input(
                "Age",
                0,
                120,
                step=1
            )

        with col2:

            service = st.selectbox(

                "Service Used",

                [

                    "Asthma Detection",
                    "Bronchial Detection",
                    "COPD Detection",
                    "Healthy Screening",
                    "Pneumonia Detection"

                ]

            )

            rating = st.radio(

                "Overall Rating",

                [1,2,3,4,5],

                horizontal=True

            )

        feedback = st.text_area(

            "Share your experience"

        )

        improvement = st.text_area(

            "Suggestions for improvement"

        )

        submit = st.form_submit_button(

            "✅ Submit Review"

        )
        # ==========================================
        # SAVE REVIEW
        # ==========================================

    if submit:

        data = {

            "Name": name,
            "Age": age,
            "Service": service,
            "Rating": rating,
            "Feedback": feedback,
            "Improvement": improvement,
            "Date": datetime.now().strftime("%d-%m-%Y %H:%M")

        }

        file_path = "reviews.csv"

        if os.path.exists(file_path):

            df = pd.read_csv(file_path)

            df = pd.concat(
                [df, pd.DataFrame([data])],
                ignore_index=True
            )

        else:

            df = pd.DataFrame([data])

        df.to_csv(
            file_path,
            index=False
        )

        st.success(
            "🎉 Thank you! Your review has been submitted successfully."
        )

        st.balloons()

    st.markdown("---")

    # ==========================================
    # REVIEW ANALYTICS
    # ==========================================

    st.header("📊 Patient Review Analytics")

    file_path = "reviews.csv"

    if os.path.exists(file_path):

        df = pd.read_csv(file_path)

        total_reviews = len(df)

        avg_rating = round(df["Rating"].mean(), 2)

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "📝 Total Reviews",
                total_reviews
            )

        with col2:

            st.metric(
                "⭐ Average Rating",
                f"{avg_rating}/5"
            )

        st.markdown("---")

        st.subheader("💬 Latest Patient Reviews")

        latest_reviews = df.tail(5).iloc[::-1]

        for _, row in latest_reviews.iterrows():

            stars = "⭐" * int(row["Rating"])

            reviewer = row["Name"]

            if pd.isna(reviewer) or str(reviewer).strip() == "":
                reviewer = "Anonymous"

            with st.container():

                st.markdown(
                    f"""
    ### 👤 {reviewer}

    **🏥 Service:** {row['Service']}

    **⭐ Rating:** {stars}

    **💬 Feedback:**

    {row['Feedback']}

    **🛠️ Suggestions:**

    {row['Improvement']}

    **📅 Submitted:** {row['Date']}

    ---
    """
                )

    else:

        st.info(
            "No reviews available yet. Be the first to submit one!"
        )

    st.markdown("---")

    st.success(
        "❤️ Thank you for supporting RespiDiagnosis AI."
    )

    st.caption(
        "RespiDiagnosis AI • AI-powered Respiratory Disease Detection System"
    )

    st.markdown("---")

    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"

        st.rerun()