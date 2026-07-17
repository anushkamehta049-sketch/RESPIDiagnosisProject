import streamlit as st
import os
from datetime import datetime
from audio_recorder_streamlit import audio_recorder
import time
from utils.pdf_generator import generate_pdf
from database import insert_record
from utils.predict import predict_disease
from gtts import gTTS
import tempfile

# -----------------------------------
# Disease Information
# -----------------------------------

disease_info = {

    "healthy": {
        "description": "No respiratory disease detected.",
        "symptoms": "Normal breathing.",
        "treatment": "No treatment required.",
        "doctor": "General Physician"
    },

    "asthma": {
        "description": "Airways become narrow and swollen.",
        "symptoms": "Wheezing, coughing, chest tightness.",
        "treatment": "Use inhaler and avoid dust.",
        "doctor": "Pulmonologist"
    },

    "copd": {
        "description": "Chronic Obstructive Pulmonary Disease.",
        "symptoms": "Shortness of breath, cough.",
        "treatment": "Quit smoking, medicines and breathing exercises.",
        "doctor": "Pulmonologist"
    },

    "pneumonia": {
        "description": "Lung infection caused by bacteria or viruses.",
        "symptoms": "Fever, cough, chest pain.",
        "treatment": "Antibiotics, fluids and rest.",
        "doctor": "Chest Specialist"
    }
}

youtube_links = {

    "healthy": "https://youtu.be/1_62HeAdfwo?si=8PWdtnyRX25WuSQw",

    "asthma": "https://youtu.be/PzfLDi-sL3w?si=QztMMb7-U9y6b4DL",

    "copd": "https://youtu.be/T1G9Rl65M-Q?si=_fndSgIDvuoXgji0",

    "pneumonia": "https://youtu.be/GNjzapyrEN0?si=B7AFoW71Il5qD89T",
     
    "bronchial":"https://youtu.be/6-6gHWiGI0Y?si=gAlKW-UdVc8ztZyH"

}





# -----------------------------------
# Prediction Page
# -----------------------------------

def show_prediction():
    if "audio_path" not in st.session_state:
        st.session_state.audio_path = None
    if "show_recorder" not in st.session_state:
        st.session_state.show_recorder = False

    st.title("🫁 New Patient Diagnosis")
    st.markdown("""
    <style>

    .ball{
    width:90px;
    height:90px;
    background:#1E88E5;
    border-radius:50%;
    margin:auto;
    animation:breath 8s infinite ease-in-out;
    box-shadow:0 0 25px #2196F3;
    }

    @keyframes breath{

    0%{
    transform:translateY(120px);
    }

    35%{
    transform:translateY(-80px);
    }

    55%{
    transform:translateY(-80px);
    }

    100%{
    transform:translateY(120px);
    }

    }

    .text{
    text-align:center;
    font-size:28px;
    font-weight:bold;
    color:#1565C0;
    margin-top:20px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input("👤 Patient Name")

        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"]
        )

        symptoms = st.text_area(
            "Symptoms"
        )

    with col2:

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=100,
            value=25
        )

        mobile = st.text_input(
            "📱 Mobile Number"
        )

    st.markdown("---")

    st.subheader("🎤 Voice Sample")

    left, right = st.columns(2)

    audio_path = None

    # ======================================
    # Upload Audio
    # ======================================

    with left:

        st.markdown("### 📁 Upload Audio")

        uploaded_audio = st.file_uploader(
            "Upload WAV File",
            type=["wav"],
            key="upload_audio"
        )

        if uploaded_audio:
            os.makedirs("recordings", exist_ok=True)

            audio_path = os.path.join("recordings", uploaded_audio.name)

            st.session_state.audio_path = audio_path

            save_path = os.path.join("recordings", uploaded_audio.name)

            with open(save_path, "wb") as f:
                f.write(uploaded_audio.getbuffer())

            st.session_state.audio_path = save_path

            st.success("✅ Audio Uploaded")



    # ======================================
    # Record Audio
    # ======================================

    with right:

        st.markdown("### 🎙 Record Audio")

        if not st.session_state.show_recorder:

            if st.button(
                    "🫁 Start Breathing Test",
                    use_container_width=True
            ):
                st.session_state.show_recorder = True
                st.rerun()

        if st.session_state.show_recorder:

            st.info("🫁 Inhale... Hold... Exhale... Then record your cough.")

            progress = st.progress(0)

            status = st.empty()

            for i in range(100):

                if i < 35:
                    status.info("🫁 Inhale")

                elif i < 55:
                    status.warning("✋ Hold")

                else:
                    status.success("🌬 Exhale")

                progress.progress(i + 1)

                time.sleep(0.03)

            st.success("🎙 Now record your cough.")

            audio_bytes = audio_recorder(
                text="Click microphone to Record",
                recording_color="#ff4b4b",
                neutral_color="#6aa36f",
                icon_name="microphone",
                icon_size="2x",
                key="cough_recorder"
            )

            if audio_bytes is not None:
                os.makedirs("recordings", exist_ok=True)

                save_path = os.path.join(
                    "recordings",
                    "recorded_audio.wav"
                )

                with open(save_path, "wb") as f:
                    f.write(audio_bytes)

                st.session_state.audio_path = save_path

                st.success("✅ Recording Saved")

                st.audio(audio_bytes)

                st.session_state.show_recorder = False

    st.markdown("---")

    if st.button("🩺 Predict Disease"):

        if name == "":
            st.warning("Enter patient name.")
            st.stop()

        audio_path = st.session_state.get("audio_path")

        if audio_path is None:
            st.error("Please upload or record audio.")
            st.stop()

        if not os.path.exists(audio_path):
            st.error("Audio file not found.")
            st.stop()

        with st.spinner("Analyzing respiratory sound..."):
            disease, confidence, probabilities, classes = predict_disease(audio_path)

            # Save prediction in session state
        st.session_state["disease"] = disease
        st.session_state["confidence"] = confidence

        st.success("✅ Prediction Completed")

        st.metric(
            "Predicted Disease",
            disease
        )

        st.metric(
            "Confidence",
            f"{confidence:.2f}%"
        )

        # -----------------------------------
        # Risk Level
        # -----------------------------------

        # -----------------------------------
        # Risk Level
        # -----------------------------------

        # Convert prediction to lowercase
        disease = str(disease).lower()

        severity = "Unknown"

        if disease == "healthy":
            severity = "Low"
            st.success("🟢 Risk Level : LOW")

        elif disease == "asthma":
            severity = "Medium"
            st.warning("🟡 Risk Level : MEDIUM")

        elif disease in ["copd", "bronchial", "pneumonia"]:
            severity = "High"
            st.error("🔴 Risk Level : HIGH")

        else:
            st.warning("⚠ Unknown disease predicted.")


        # -----------------------------------
        # Save Record to Database
        # -----------------------------------

        now = datetime.now()

        insert_record(
            patient_name=name,
            age=age,
            gender=gender,
            disease=disease,
            confidence=round(confidence, 2),
            severity=severity,
            prediction_date=now.strftime("%d-%m-%Y"),
            prediction_time=now.strftime("%H:%M"),
            audio_file=audio_path,
            pdf_report=""
        )

        st.success("✅ Patient record saved successfully.")

        # -----------------------------------
        # Disease Information
        # -----------------------------------

        if disease in disease_info:
            info = disease_info[disease]

            st.markdown("---")
            st.subheader("📚 Disease Information")

            st.write("### 📝 Description")
            st.write(info["description"])

            st.write("### 🤒 Symptoms")
            st.write(info["symptoms"])

            st.write("### 💊 Treatment")
            st.write(info["treatment"])

            st.write("### 👨‍⚕ Recommended Doctor")
            st.success(info["doctor"])

        st.markdown("---")

        st.markdown("---")
        st.subheader("🎥 Recommended Video")

        st.link_button(
            "▶ Watch on YouTube",
            youtube_links[disease]
        )

        pdf_path = generate_pdf(
            patient=name,
            age=age,
            gender=gender,
            disease=disease,
            confidence=confidence,
            symptoms=symptoms
        )

        with open(pdf_path, "rb") as file:
            pdf_bytes = file.read()

        st.download_button(
            label="📄 Download Medical Report",
            data=pdf_bytes,
            file_name=f"{name}_Report.pdf",
            mime="application/pdf"
        )

        # -----------------------------------
        # Prediction Summary
        # -----------------------------------

        summary = {
            "Patient": name,
            "Age": age,
            "Gender": gender,
            "Disease": disease,
            "Confidence": f"{confidence:.2f}%",
            "Risk": severity,
            "Date": now.strftime("%d-%m-%Y"),
            "Time": now.strftime("%H:%M")
        }

        st.subheader("📋 Diagnosis Summary")

        st.json(summary)

    st.markdown("---")


    col1, col2 = st.columns(2)

    with col1:

        if st.button("🔊 Speak Diagnosis"):

            if "disease" not in st.session_state:
                st.warning("Please predict disease first.")
            else:

                speech = (
                    f"Patient {name}. "
                    f"Predicted disease is {st.session_state['disease']}. "
                    f"Confidence is {st.session_state['confidence']:.1f} percent."
                )

                tts = gTTS(text=speech, lang="en")

                temp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")

                tts.save(temp.name)

                st.audio(temp.name, autoplay=True)

    st.markdown("---")

    if st.button("⬅ Back to Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()