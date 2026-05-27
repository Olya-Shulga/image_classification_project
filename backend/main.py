from fastapi import FastAPI, File, UploadFile
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import io
import json

app = FastAPI()

model = load_model("models/best_model_final.keras")

with open("models/class_names.json", "r", encoding="utf-8") as f:
    class_names = json.load(f)["classes"]

with open("models/model_meta.json", "r", encoding="utf-8") as f:
    IMG_SIZE = json.load(f)["img_size"]


def preprocess_image(image):
    image = image.resize((IMG_SIZE, IMG_SIZE))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image


@app.get("/")
def home():
    return {"message": "Image Classification API работает"}


@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()

    image = Image.open(io.BytesIO(contents)).convert("RGB")

    processed = preprocess_image(image)

    prediction = model.predict(processed)

    probs = prediction[0]

    predicted_class = class_names[np.argmax(probs)]
    confidence = float(np.max(probs))

    probabilities = {
        class_names[i]: float(probs[i])
        for i in range(len(class_names))
    }

    return {
        "class": predicted_class,
        "confidence": confidence,
        "probabilities": probabilities
    }