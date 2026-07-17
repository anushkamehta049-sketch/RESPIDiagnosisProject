import streamlit as st

# -----------------------------------
# About Page
# -----------------------------------

def show_about():

    st.title("🫁 About RespiCare AI")

    st.markdown(
        """
        <h4 style='color:#1E88E5;'>
        AI Powered Respiratory Disease Detection & Awareness Platform
        </h4>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # ==================================================
    # NEWS SECTION
    # ==================================================

    st.header("📰 Respiratory Disease News & Awareness")

    st.write(
        """
        Respiratory diseases are becoming one of the biggest health challenges
        across the world. Every year thousands of people lose their lives
        because diseases like Asthma, Pneumonia, COPD and Bronchitis are not
        detected at an early stage.
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        st.image("images/news/news1.png", use_container_width=True)

    with col2:
        st.image("images/news/news2.png", use_container_width=True)

    st.write("")

    col3, col4 = st.columns(2)

    with col3:
        st.image("images/news/news3.png", use_container_width=True)

    with col4:
        # Replace with news4.jpg if available
        st.image("images/news/news4.png", use_container_width=True)

    st.markdown("---")

    # ==================================================
    # WHY EARLY DETECTION
    # ==================================================

    st.header("⚠ Why Early Detection is Important")

    st.error("""
Ignoring respiratory diseases can permanently damage the lungs.
Many patients visit hospitals only when breathing becomes extremely difficult.
By then treatment becomes more expensive, complicated and sometimes impossible.
""")

    st.info("""
Early diagnosis allows doctors to begin treatment sooner,
improving recovery chances and reducing complications.
""")

    st.markdown("---")

    # ==================================================
    # DISEASES
    # ==================================================

    st.header("🫁 Major Respiratory Diseases")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["Asthma", "Pneumonia", "COPD", "Bronchitis"]
    )

    with tab1:
        st.subheader("Asthma")
        st.write("""
Asthma narrows the airways and makes breathing difficult.

If ignored:

• Severe asthma attacks

• Low oxygen level

• Frequent hospitalization

• Permanent airway damage
""")

    with tab2:
        st.subheader("Pneumonia")
        st.write("""
Pneumonia is a serious lung infection.

Without treatment:

• Fluid fills the lungs

• High fever

• Difficulty breathing

• Respiratory failure

• Can become life-threatening
""")

    with tab3:
        st.subheader("COPD")
        st.write("""
COPD is a progressive disease that slowly destroys lung function.

Possible complications:

• Permanent lung damage

• Breathlessness

• Oxygen dependency

• Heart complications
""")

    with tab4:
        st.subheader("Bronchitis")
        st.write("""
Bronchitis causes inflammation of the bronchial tubes.

Ignoring it may lead to:

• Chronic cough

• Repeated infections

• Reduced lung capacity

• COPD
""")

    st.markdown("---")

    # ==================================================
    # RURAL PROBLEMS
    # ==================================================

    st.header("🏡 Challenges in Rural Areas")

    st.warning("""
Many people living in villages face serious healthcare problems.

• Lack of specialist doctors

• Long distance to hospitals

• Low awareness

• Financial difficulties

• Poor diagnostic facilities

• Delayed treatment

• Dependence on self-medication

As a result many respiratory diseases are diagnosed only in advanced stages.
""")

    st.markdown("---")

    # ==================================================
    # RISK FACTORS
    # ==================================================

    st.header("🚭 Common Risk Factors")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("🚬 Smoking")

        st.success("🏭 Air Pollution")

        st.success("🧪 Chemical Exposure")

    with c2:
        st.success("🦠 Viral Infections")

        st.success("🌫 Dust")

        st.success("🔥 Indoor Smoke")

    with c3:
        st.success("👴 Old Age")

        st.success("👶 Weak Immunity")

        st.success("🧬 Family History")

    st.markdown("---")

    # ==================================================
    # OUR SOLUTION
    # ==================================================

    st.header("🤖 Our AI Solution")

    st.write("""
RespiCare AI helps healthcare professionals by providing
an intelligent preliminary prediction of respiratory diseases.

Our system aims to:

✅ Detect diseases early

✅ Assist doctors

✅ Reduce diagnosis time

✅ Increase awareness

✅ Maintain patient records

✅ Recommend specialists

✅ Improve healthcare accessibility
""")

    st.markdown("---")

    # ==================================================
    # WHY CHOOSE US
    # ==================================================

    st.header("⭐ Why Choose RespiCare AI")

    col1, col2 = st.columns(2)

    with col1:

        st.success("✔ AI Assisted Prediction")

        st.success("✔ Easy User Interface")

        st.success("✔ Fast Results")

        st.success("✔ Secure Records")

    with col2:

        st.success("✔ Expert Doctors")

        st.success("✔ Patient Friendly")

        st.success("✔ Modern Technology")

        st.success("✔ Awareness Platform")

    st.markdown("---")

    # ==================================================
    # DISCLAIMER
    # ==================================================

    st.header("⚕ Medical Disclaimer")

    st.info("""
This system is intended only for educational purposes and
AI-assisted preliminary prediction.

It does NOT replace professional medical diagnosis.

Always consult a qualified pulmonologist or physician
before taking any medical decision.
""")

    st.markdown("---")

    # ==================================================
    # FOOTER
    # ==================================================

    st.success("❤️ Every Breath Matters")

    st.caption(
        "RespiCare AI | Early Detection • Better Treatment • Healthier Lives"
    )

    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()