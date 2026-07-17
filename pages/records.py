import streamlit as st
import pandas as pd
from database import get_all_records


def show_records():

    st.title("📂 Previous Patient Records")
    st.markdown("### Respiratory Diagnosis History")

    records = get_all_records()

    if records:

        df = pd.DataFrame(
            records,
            columns=[
                "ID",
                "Patient Name",
                "Age",
                "Gender",
                "Disease",
                "Confidence",
                "Severity",
                "Prediction Date",
                "Prediction Time",
                "Audio File",
                "PDF Report"
            ]
        )

    else:

        df = pd.DataFrame(
            columns=[
                "ID",
                "Patient Name",
                "Age",
                "Gender",
                "Disease",
                "Confidence",
                "Severity",
                "Prediction Date",
                "Prediction Time",
                "Audio File",
                "PDF Report"
            ]
        )

    display_df = df[
        [
            "Patient Name",
            "Age",
            "Gender",
            "Disease",
            "Confidence",
            "Severity",
            "Prediction Date",
            "Prediction Time"
        ]
    ]

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    total = len(df)

    healthy = len(df[df["Disease"].str.lower() == "healthy"])

    diseased = total - healthy

    col1.metric("Total Patients", total)
    col2.metric("Healthy", healthy)
    col3.metric("Diseased", diseased)
    st.markdown("---")

    st.subheader("🔍 Search Patient")

    search = st.text_input("Enter Patient Name")

    if search:
        result = display_df[
            display_df["Patient Name"].str.contains(search, case=False, na=False)
        ]

        if len(result):
            st.dataframe(result, use_container_width=True, hide_index=True)
        else:
            st.warning("No patient found.")

    st.markdown("---")

    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()