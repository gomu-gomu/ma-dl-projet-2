import streamlit as st
from utils import ui



ui.header()
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
        ### Ensemble de données
        Pour construire notre modèle de détection du cancer du sein, nous avons utilisé un ensemble de **7 632 mammographies**. Ces images ont été divisées en trois ensembles : **3 816 pour l'entraînement**, **1 908 pour la validation**, et **1 908 pour les tests**. Chaque image a été normalisée pour garantir une cohérence dans les données, ce qui permet au modèle de mieux apprendre les motifs distinctifs des cas bénins et malins.
        ### Architecture du modèle
        Nous avons conçu un CNN avec des blocs de convolution, max-pooling, et une couche sigmoïde pour prédire si une mammographie est bénigne ou maligne.
""")

with col2:
    st.image("assets/ui/side.png", use_container_width=True)
    st.page_link("pages/Prédiction.py", label="Faire une prédiction", icon="🌟", help="Faire un diagnostic en direct", use_container_width=True)
    st.page_link("https://google.com", label="Article scientifique", icon="📄", help="Téléchargez l'article scientifique", use_container_width=True)
    st.page_link("https://github.com/gomu-gomu/ma-dl-projet-2", label="Code source", icon="🗃️", help="Accéder au code source de cette démo", use_container_width=True)
    st.page_link("https://github.com/gomu-gomu/ma-dl-projet-1", label="Modèle de prédiction", icon="🧠", help="Accès au modèle utilisé", use_container_width=True)

