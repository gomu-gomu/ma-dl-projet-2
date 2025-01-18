import os
import numpy as np
import streamlit as st

from PIL import Image
from keras.models import load_model



MODEL_PATH = os.path.join('assets', 'model', 'model.h5')

@st.cache_data
def load():
    return load_model(MODEL_PATH)

def process(mammogram):
    mam = Image.open(mammogram)
    mam = mam.resize((224, 224))
    mam_np = np.array(mam)

    if mam_np.ndim == 2:
        mam_np = np.stack([mam_np] * 3, axis=-1)
    elif mam_np.shape[2] == 1:
        mam_np = np.repeat(mam_np, 3, axis=-1)

    mam_np = mam_np / 255.0
    mam_np = np.expand_dims(mam_np, axis=0)

    return mam_np

def predict(model, threshold: float, mam_np):
    predictions = model.predict(mam_np)
    prediction = predictions[0]

    return {
        "confidence": prediction[0],
        "class": (prediction[0] > threshold).astype(int)
    }

