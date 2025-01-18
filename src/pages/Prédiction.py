import streamlit as st
from utils import ui, ai


mammogram = st.sidebar.file_uploader("Sélectionnez une mammographie", type="png")
model = ai.load()

ui.credits()
ui.header("Faire une prédiction")
col1, col2 = st.columns([2, 1])

if mammogram is not None:
    mam_np = ai.process(mammogram)
    predictions = ai.predict(model, mam_np)
    diagnosis = "benign" if predictions["class"] == 0 else "malignant"

    with col1:
        st.image(f"assets/ui/{diagnosis}.png", use_container_width=True)
        st.write("<breakdown>")

    with col2:
        st.image(mammogram, caption="mammographie", use_container_width=True)
        st.write("<chart>")
        st.write("<confidence>")
else:
    st.write("Sélectionnez une mammographie à partir du fichier d’entrée dans la barre latérale afin d’exécuter la prédiction.")

