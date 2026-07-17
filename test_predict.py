from utils.predict import predict_disease

audio = "dataset/asthma/aug_noise_1_P15WheezingRL_75.wav"

disease, confidence, probs, classes = predict_disease(audio)

print("Disease :", disease)
print("Confidence :", confidence)