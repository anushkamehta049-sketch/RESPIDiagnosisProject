import streamlit as st

# ---------------------------------------
# Doctors Page
# ---------------------------------------

def show_staff():

    st.title("👨‍⚕️ Our Expert Pulmonologists")
    st.markdown("### Trusted Respiratory Specialists")

    st.markdown("---")

    # ===================================
    # Hospital Introduction
    # ===================================

    st.subheader("🏥 Our Partner Hospital")

    st.video(
        "images/animations/hospital.mp4",
        autoplay=True,
        muted=True,
        loop=True,
        width=100,

    )

    st.info(
        "Our hospital is equipped with modern respiratory diagnostic "
        "equipment, experienced pulmonologists and AI-assisted disease "
        "prediction technology."
    )

    st.markdown("---")

    # ===================================
    # Doctor 1
    # ===================================

    col1, col2 = st.columns([1, 2])

    with col1:

        st.image(
            "images/doctors/doctor2.jpg",
            width=220
        )

    with col2:

        st.video(
            "images/animations/doctor verified right.mp4",
            autoplay=True,
            muted=True,
            loop=True,
            width=70,

        )

        st.subheader("👨‍⚕️ Dr. Rajesh Sharma")

        st.write("**Qualification:** MBBS, MD (Pulmonary Medicine)")

        st.write("**Experience:** 15 Years")

        st.write("**Specialization:** Pulmonologist")

        st.write("**Hospital:** Apollo Hospital")

        st.write("**Rating:** ⭐⭐⭐⭐⭐ (4.9/5)")

        st.write("**Location:** Pune")

        st.write("**Contact:** +91 9876543210")

        st.write("**Email:** rajesh.sharma@gmail.com")



    st.markdown("---")

    # ===================================
    # Doctor 2
    # ===================================

    col1, col2 = st.columns([1, 2])

    with col1:

        st.image(
            "images/doctors/doctor1.jpg",
            width=220
        )

    with col2:

        st.video(
            "images/animations/doctor intro hi.mp4",
            autoplay=True,
            muted=True,
            loop=True,
            width=70,

        )

        st.subheader("👩‍⚕️ Dr. Priya Mehta")

        st.write("**Qualification:** MBBS, DNB Respiratory Medicine")

        st.write("**Experience:** 12 Years")

        st.write("**Specialization:** Chest Physician")

        st.write("**Hospital:** Fortis Hospital")

        st.write("**Rating:** ⭐⭐⭐⭐⭐ (4.8/5)")

        st.write("**Location:** Mumbai")

        st.write("**Contact:** +91 9988776655")

        st.write("**Email:** priyamehta@gmail.com")



    st.markdown("---")

    # ===================================
    # Doctor 3
    # ===================================

    col1, col2 = st.columns([1, 2])

    with col1:

        st.image(
            "images/doctors/doctor3.jpg",
            width=220
        )

    with col2:

        st.video(
            "images/animations/heart loading.mp4",
            autoplay=True,
            muted=True,
            loop=True,
            width=70,

        )

        st.subheader("👨‍⚕️ Dr. Amit Verma")

        st.write("**Qualification:** MBBS, MD (Respiratory Medicine)")

        st.write("**Experience:** 18 Years")

        st.write("**Specialization:** COPD & Asthma Specialist")

        st.write("**Hospital:** Max Healthcare")

        st.write("**Rating:** ⭐⭐⭐⭐⭐ (4.9/5)")

        st.write("**Location:** Delhi")

        st.write("**Contact:** +91 9876501234")

        st.write("**Email:** amit.verma@gmail.com")



    st.markdown("---")

    # ===================================
    # Doctor 4
    # ===================================

    col1, col2 = st.columns([1, 2])

    with col1:

        st.image(
            "images/doctors/doctor4.jpg",
            width=220
        )

    with col2:

        st.video(
            "images/animations/man standing with lungs report.mp4",
            autoplay=True,
            muted=True,
            loop=True,
            width=70,

        )

        st.subheader("👩‍⚕️ Dr. Risha Kulkarni")

        st.write("**Qualification:** MBBS, DM Pulmonology")

        st.write("**Experience:** 14 Years")

        st.write("**Specialization:** Pneumonia & Lung Infection")

        st.write("**Hospital:** AIIMS")

        st.write("**Rating:** ⭐⭐⭐⭐⭐ (5.0/5)")

        st.write("**Location:** New Delhi")

        st.write("**Contact:** +91 9123456780")

        st.write("**Email:** risha.kulkarni@gmail.com")



    st.markdown("---")

    # ===================================
    # Hospital Facilities
    # ===================================

    st.subheader("🏥 Why Choose Our Hospital?")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("🫁 AI Respiratory Diagnosis")

    with c2:
        st.success("👨‍⚕️ Experienced Specialists")

    with c3:
        st.success("🧪 Modern Diagnostic Labs")

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.info("🚑 24×7 Emergency")

    with c2:
        st.info("💊 Pharmacy Available")

    with c3:
        st.info("📱 Online Consultation")

    st.markdown("---")

    # ===================================
    # Emergency Contact
    # ===================================

    st.subheader("🚨 Emergency Contact")

    st.error("📞 Ambulance : 108")

    st.info("☎ Hospital Helpline : +91 1800-123-456")

    st.success("📧 Email : support@respidiagnosis.com")

    st.markdown("---")

    # ===================================
    # Footer
    # ===================================

    st.caption(
        "RespiDiagnosis AI | Connecting patients with trusted respiratory specialists."
    )

    st.write("")

    if st.button("⬅ Back to Dashboard"):

        st.session_state.page = "dashboard"

        st.rerun()