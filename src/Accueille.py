import streamlit as st


st.image("assets/banner.png", use_container_width=True)
st.title("Application de détection du cancer du sein à partir de la mammographie")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
        ### Ensemble de données
        Pour construire notre modèle de détection du cancer du sein, nous avons utilisé un ensemble de **7 632 mammographies**. Ces images ont été divisées en trois ensembles : **3 816 pour l'entraînement**, **1 908 pour la validation**, et **1 908 pour les tests**. Chaque image a été normalisée pour garantir une cohérence dans les données, ce qui permet au modèle de mieux apprendre les motifs distinctifs des cas bénins et malins.
        ### Architecture du modèle
        Nous avons conçu un CNN avec des blocs de convolution, max-pooling, et une couche sigmoïde pour prédire si une mammographie est bénigne ou maligne.
""")

with col2:
    st.image("assets/side.jpg", use_container_width=True)
    if st.button("Mammographie diagnostique"):
        st.write("Predict!")
