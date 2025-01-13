import os
from io import BytesIO

from PIL import Image
import streamlit as st

import numpy as np
import tensorflow as tf
from keras.models import load_model


MODEL_PATH = os.path.join('assets', 'model', 'model.h5')

def load():
  return load_model(MODEL_PATH)

def preprocess_image(image_path):
  # Open the image file
  img = Image.open(image_path)

  # Resize the image to match the input shape of the model (224x224 for example)
  img = img.resize((224, 224))

  # Convert the image to a numpy array
  img_array = np.array(img)

  if img_array.ndim == 2:  # Grayscale image case
    img_array = np.stack([img_array] * 3, axis=-1)  # Convert to 3 channels
  elif img_array.shape[2] == 1:  # If the image has only 1 channel (e.g., grayscale)
    img_array = np.repeat(img_array, 3, axis=-1)  # Repeat grayscale to 3 channels

  # Normalize the image if the model was trained with normalized data
  img_array = img_array / 255.0  # Normalize if the model uses values between 0 and 1

  # Expand the dimensions to match the batch shape (1, 224, 224, 3)
  img_array = np.expand_dims(img_array, axis=0)

  return img_array

def predict(image_path, model):
  # Preprocess the image before making a prediction
  processed_image = preprocess_image(image_path)
  
  # Predict using the model (this returns probabilities)
  predictions = model.predict(processed_image)

  # Convert probabilities to class (binary prediction, 0 or 1)
  prediction_class = (predictions > 0.5).astype(int)  # Assuming binary classification with a sigmoid output
  print(prediction_class)
  # Return the prediction
  return "Malignant" if prediction_class[0] == 1 else "Benign"

def main():
  st.set_page_config(page_title="Breast Cancer Detection", layout="centered", page_icon="😷")

  st.title("Détection du cancer du sein à partir de la mammographie par l'utilisation de l'IA")
  st.image("assets/banner.png")

  st.markdown(
    "**Credits:**\n" +
    "1. ESSAMADI Oussama\n" +
    "2. ZOUIR Amine\n" +
    "3. CHIBI Mohammed"
  )

  uploaded_file = st.file_uploader("Télécharger une image de mammographie (PNG)", type=["png"])

  if uploaded_file is not None:
    # Save uploaded image temporarily
    image_path = os.path.join("assets/tmp", uploaded_file.name)
    os.makedirs("assets/tmp", exist_ok=True)
    with open(image_path, "wb") as temp_file:
      temp_file.write(uploaded_file.getbuffer())

    # Display uploaded image
    st.image(Image.open(uploaded_file), caption="Uploaded Mammogram")

    # Load model
    model = load()

    # Predict button
    if st.button("Predict Cancer Status"):
      result = predict(image_path, model)
      st.success(f"Prediction: {result}")

if __name__ == "__main__":
  main()