import streamlit as st
from utils import ui



ui.credits()
ui.header("Application de détection du cancer du sein à partir de la mammographie")
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
    st.page_link("https://file.notion.so/f/f/492b307c-3e4f-4fae-8af2-5d5cf0ee5e3a/d5d95761-c1db-4fe6-9e99-e4d47d09d8c7/Dtection_du_cancer_du_sein__partir_de_la_mammographie_par_lutilisation_de_lIA.pdf?table=block&id=181d9994-81b3-800d-a9c1-c88d656cc79d&spaceId=492b307c-3e4f-4fae-8af2-5d5cf0ee5e3a&expirationTimestamp=1737439200000&signature=tva78g6wNV3pp1x22DekPhTmnEfjAUiI4vpseks1txg&downloadName=D%C3%A9tection+du+cancer+du+sein+%C3%A0+partir+de+la+mammographie+par+l%27utilisation+de+l%E2%80%99IA.pdf", label="Article Scientifique", icon="📄", help="Téléchargez l'article scientifique", use_container_width=True)
    st.page_link("https://www.kaggle.com/datasets/eoussama/breast-cancer-mammograms", label="Dataset", icon="🗃️", help="Accéder dataset utilisé", use_container_width=True)
    st.page_link("https://github.com/gomu-gomu/ma-dl-projet-2", label="Code source", icon="🔢", help="Accéder au code source de cette démo", use_container_width=True)
    st.page_link("https://github.com/gomu-gomu/ma-dl-projet-1", label="Modèle de prédiction", icon="🧠", help="Accès au modèle utilisé", use_container_width=True)

