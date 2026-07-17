import os
import joblib
import librosa
import numpy as np

# -----------------------
# Paths
# -----------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "model")

MODEL_FILE = os.path.join(MODEL_PATH, "cough_classifier.pkl")
ENCODER_FILE = os.path.join(MODEL_PATH, "label_encoder.pkl")

# -----------------------
# Load Model
# -----------------------

model = joblib.load(MODEL_FILE)
encoder = joblib.load(ENCODER_FILE)


# -----------------------
# Feature Extraction
# -----------------------

def extract_features(audio_path):
    """
    Extract MFCC features from an audio file.
    """

    audio, sr = librosa.load(audio_path, sr=22050)

    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sr,
        n_mfcc=40
    )

    feature = np.mean(mfcc.T, axis=0)

    return feature.reshape(1, -1)


# -----------------------
# Prediction Function
# -----------------------

def predict_disease(audio_path):
    """
    Predict respiratory disease from cough audio.
    """

    features = extract_features(audio_path)

    prediction = model.predict(features)[0]

    disease = encoder.inverse_transform([prediction])[0]

    probabilities = model.predict_proba(features)[0]

    confidence = float(np.max(probabilities) * 100)

    return disease, confidence, probabilities, encoder.classes_