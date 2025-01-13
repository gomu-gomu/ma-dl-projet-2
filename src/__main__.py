import os
import pickle
from PIL import Image
import streamlit as st



MODEL_PATH = os.path.join('assets', 'model', 'X_test.pkl')
X_TEST_PATH = os.path.join('assets', 'model', 'X_test.pkl')
Y_TEST_PATH = os.path.join('assets', 'model', 'y_test.pkl')

def load_model():
  with open(MODEL_PATH, 'rb') as model_file:
    return pickle.load(model_file)

def predict(image_path, model):
    # Placeholder: Replace with your actual image preprocessing and prediction logic
    return model.predict(image_path)

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
    model = load_model()

    # Predict button
    if st.button("Predict Cancer Status"):
      result = predict(image_path, model)
      st.success(f"Prediction: {result}")

if __name__ == "__main__":
  main()