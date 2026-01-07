import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # silence TF warnings

import streamlit as st
import tensorflow as tf
import keras
import numpy as np
from PIL import Image

# Cache the model so it loads only once
@st.cache_resource
def load_model():
    return keras.models.load_model("models/cat_dog.h5")

model = load_model()

st.title("🐶🐱 Cat vs Dog Classifier")
st.write("Upload an image and the model will predict whether it is a **cat** or a **dog**.")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

def preprocess_image(image):
    image = image.convert("RGB")
    image = image.resize((224, 224))  # MUST match training
    image = np.array(image)
    image = keras.applications.efficientnet.preprocess_input(image)
    image = np.expand_dims(image, axis=0)
    return image

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Predict"):
        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)[0][0]

        confidence = float(prediction)
        if confidence > 0.5:
            st.success(f"🐶 **Dog** — confidence: {confidence:.2%}")
        else:
            st.success(f"🐱 **Cat** — confidence: {(1 - confidence):.2%}")