import streamlit as st
import joblib
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report

# ==========================================
# Analytics Page
# ==========================================

def show_analytics():

    # -------------------------------
    # Paths
    # -------------------------------

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    MODEL_PATH = os.path.join(BASE_DIR, "model")

    METRICS_FILE = os.path.join(MODEL_PATH, "metrics.pkl")

    # -------------------------------
    # Load Metrics
    # -------------------------------

    if not os.path.exists(METRICS_FILE):
        st.error("metrics.pkl not found.\nPlease train the model first.")
        return

    metrics = joblib.load(METRICS_FILE)

    # -------------------------------
    # Title
    # -------------------------------

    st.title("🧠 AI Model Analytics Dashboard")

    st.markdown("---")

    # -------------------------------
    # Dataset Statistics
    # -------------------------------

    st.subheader("📁 Dataset Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Samples",
        metrics["dataset_size"]
    )

    col2.metric(
        "Training Samples",
        metrics["train_samples"]
    )

    col3.metric(
        "Testing Samples",
        metrics["test_samples"]
    )

    st.markdown("---")

    # -------------------------------
    # Performance Metrics
    # -------------------------------

    st.subheader("📈 Model Performance")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Accuracy",
        f"{metrics['accuracy']*100:.2f}%"
    )

    c2.metric(
        "Precision",
        f"{metrics['precision']*100:.2f}%"
    )

    c3.metric(
        "Recall",
        f"{metrics['recall']*100:.2f}%"
    )

    c4.metric(
        "F1 Score",
        f"{metrics['f1']*100:.2f}%"
    )

    st.markdown("---")

    # -------------------------------
    # Model Information
    # -------------------------------

    st.subheader("🌳 Model Information")

    left, right = st.columns(2)

    with left:

        st.info(f"""
### Algorithm

**{metrics['algorithm']}**

---

**Decision Trees :** {metrics['trees']}

**MFCC Features :** {metrics['mfcc_features']}

**Sample Rate :** {metrics['sample_rate']} Hz
""")

    with right:

        st.success("### Disease Classes")

        for disease in metrics["classes"]:
            st.write("✅", disease)

    st.markdown("---")

    # -------------------------------
    # AI Pipeline
    # -------------------------------

    st.subheader("🧠 AI Pipeline")

    st.markdown("""
```text
Patient

      ↓

Cough Audio

      ↓

Librosa

      ↓

MFCC Feature Extraction

      ↓

Random Forest Classifier

      ↓

Disease Prediction

      ↓

Confidence Score

      ↓

Risk Level

      ↓

Database Storage

      ↓

PDF Report """)
st.markdown("---")

# -------------------------------
# Back Button
# -------------------------------

if st.button("⬅ Back to Dashboard"):
    st.session_state.page = "dashboard"
    st.rerun()

