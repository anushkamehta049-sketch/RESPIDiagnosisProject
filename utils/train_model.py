import warnings
import joblib
import librosa
import numpy as np

from pathlib import Path
from collections import Counter

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

warnings.filterwarnings("ignore")

# -------------------------------
# PATH SETUP (IMPORTANT FIX)
# -------------------------------

# utils/ → go 1 level up to project root
BASE_DIR = Path(__file__).resolve().parent.parent

DATASET_PATH = BASE_DIR / "dataset"
MODEL_PATH = BASE_DIR / "model"

MODEL_PATH.mkdir(exist_ok=True)

print("Dataset Path:", DATASET_PATH)
print("Model Path:", MODEL_PATH)

# -------------------------------
# CHECK DATASET
# -------------------------------

if not DATASET_PATH.exists():
    raise FileNotFoundError(f"Dataset not found: {DATASET_PATH}")

X, y = [], []

print("\nLoading dataset...\n")

# -------------------------------
# LOAD AUDIO DATA
# -------------------------------

for class_folder in sorted(DATASET_PATH.iterdir()):

    if not class_folder.is_dir():
        continue

    print(f"Reading class: {class_folder.name}")

    count = 0

    for file_path in class_folder.iterdir():

        if file_path.suffix.lower() == ".wav":

            try:
                audio, sr = librosa.load(file_path, sr=22050)

                mfcc = librosa.feature.mfcc(
                    y=audio,
                    sr=sr,
                    n_mfcc=40
                )

                feature = np.mean(mfcc.T, axis=0)

                X.append(feature)
                y.append(class_folder.name)

                count += 1

            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    print(f"Files loaded: {count}\n")

print("\nDataset Loaded Successfully\n")
print("Total samples:", len(X))

# -------------------------------
# ENCODE LABELS
# -------------------------------

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

print("\nClasses:", encoder.classes_)

# -------------------------------
# TRAIN TEST SPLIT
# -------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42,
    stratify=y_encoded
)

print("\nTrain samples:", len(X_train))
print("Test samples:", len(X_test))

# -------------------------------
# TRAIN MODEL
# -------------------------------

print("\nTraining model...\n")

model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

print("Training completed!")

# -------------------------------
# EVALUATION
# -------------------------------

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)
precision = precision_score(y_test, prediction, average="weighted")
recall = recall_score(y_test, prediction, average="weighted")
f1 = f1_score(y_test, prediction, average="weighted")

cm = confusion_matrix(y_test, prediction)

print("\nAccuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# -------------------------------
# METRICS (SAFE & CLEAN)
# -------------------------------

metrics = {
    "accuracy": float(accuracy),
    "precision": float(precision),
    "recall": float(recall),
    "f1": float(f1),

    "confusion_matrix": cm.tolist(),

    "classes": encoder.classes_.tolist(),

    "dataset_distribution": dict(Counter(y)),

    "train_samples": int(len(X_train)),
    "test_samples": int(len(X_test)),
    "dataset_size": int(len(X)),

    "sample_rate": 22050,
    "mfcc_features": 40,

    "algorithm": "Random Forest",
    "trees": 300
}

# -------------------------------
# SAVE FILES (FIXED PATH)
# -------------------------------

model_file = MODEL_PATH / "cough_classifier.pkl"
encoder_file = MODEL_PATH / "label_encoder.pkl"
metrics_file = MODEL_PATH / "metrics.pkl"

print("\nSaving files...\n")

joblib.dump(model, model_file)
print("Model saved")

joblib.dump(encoder, encoder_file)
print("Encoder saved")

joblib.dump(metrics, metrics_file)
print("Metrics saved")

print("\nFINAL FILE LOCATIONS:")
print("Model   :", model_file.resolve())
print("Encoder :", encoder_file.resolve())
print("Metrics :", metrics_file.resolve())

print("\nALL FILES SAVED SUCCESSFULLY ✔")