import os
import numpy as np
import streamlit as st

from PIL import Image
from keras.models import load_model



MODEL_PATH = os.path.join('assets', 'model', 'model.h5')

@st.cache_data
def load():
    return load_model(MODEL_PATH)

def process(image):
    img = Image.open(image)
    img = img.resize((224, 224))
    img_array = np.array(img)

    if img_array.ndim == 2:
        img_array = np.stack([img_array] * 3, axis=-1)
    elif img_array.shape[2] == 1:
        img_array = np.repeat(img_array, 3, axis=-1)

    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    return img_array

