import streamlit as st
from utils import ui



mammogram = st.sidebar.file_uploader("Sélectionnez une mammographie", type="png")

ui.credits()
ui.header("Faire une prédiction")
col1, col2 = st.columns([2, 1])

if mammogram:
    with col1:
        st.image("assets/ui/benign.png", use_container_width=True)
        st.write("<breakdown>")

    with col2:
        st.image(mammogram, use_container_width=True)
        st.write("<chart>")
        st.write("<confidence>")

