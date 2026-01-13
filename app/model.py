from tensorflow.keras.models import load_model

model = load_model("model/modelo_cnn90valAcc.h5")

EMOTIONS = ["angry", "disgust", "fear", "happy", "sad", "surprise", "neutral"]
