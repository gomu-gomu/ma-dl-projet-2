import streamlit as st
from utils import ui, ai



model = ai.load()

mammogram, threshold = ui.controls()
ui.credits()
ui.header("Faire une prédiction")

if mammogram:
    col1, col2 = st.columns([2, 1])
    
    mam_np = ai.process(mammogram)
    predictions = ai.predict(model, threshold, mam_np)
    diagnosis = "benign" if predictions["class"] == 0 else "malignant"

    with col1:
        st.image(f"assets/ui/{diagnosis}.png", use_container_width=True)
        ui.breakdown(predictions)
    with col2:
        st.image(mammogram, caption="mammographie", use_container_width=True)
        ui.chart(predictions["confidence"])
else:
    st.write("Sélectionnez une mammographie à partir du fichier d’entrée dans la barre latérale afin d’exécuter la prédiction.")

