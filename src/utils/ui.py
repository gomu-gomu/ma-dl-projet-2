import numpy as np
import pandas as pd
import altair as alt
import streamlit as st



def header(title: str):
    st.image("assets/ui/banner.png", use_container_width=True)
    st.title(title)

def controls():
    threshold = 0.50
    mammogram = st.sidebar.file_uploader("Sélectionnez une mammographie", type="png")

    if mammogram:
        threshold = st.sidebar.slider("Seuil", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

    return mammogram, threshold

def chart(confidence: float):
    benign = 1 - confidence
    malignant = confidence

    data = pd.DataFrame({
        "classes": ["Bénigne", "Maligne"],
        "colors": ["#3AB76B", "#C43835"],
        "values": np.array([benign, malignant]) * 100
    })

    chart = alt.Chart(data).mark_bar().encode(
        x=alt.X("classes", title="Catégorie"),
        y=alt.Y("values", title="Confidences", scale=alt.Scale(domain=[0, 100])),
        color=alt.Color("colors:N", scale=None, legend=None)  # Use custom colors
    ).properties(
        width=400,
        height=300
    )

    st.altair_chart(chart, use_container_width=True)

def breakdown(predictions: dict):
    diagnosis = "Bénigne" if predictions["class"] == 0 else "Maligne"
    confidence = predictions["confidence"] * 100 if predictions["class"] == 1 else (1 - predictions["confidence"]) * 100

    st.markdown(
    f"""
        ## Résultat de la Prédiction

        Le modèle de classification a analysé la mammographie fournie et a déterminé qu'elle appartient à la classe `{diagnosis}` avec un niveau de confiance de `{confidence}%`. Ce résultat est obtenu grâce à un réseau de neurones convolutif (CNN) formé sur des milliers de mammographies, conçu pour identifier les motifs complexes associés aux anomalies malignes dans les images médicales. Bien que le modèle ait une grande précision globale, il est important de noter que la confiance du modèle est une mesure probabiliste, et non une certitude absolue. Par conséquent, un niveau de confiance de `{confidence}%` indique une forte probabilité mais n'exclut pas complètement d'autres possibilités.

        Il est recommandé de ne pas utiliser ce résultat comme un diagnostic final, mais plutôt comme un outil de soutien pour les professionnels de santé. Les modèles d'apprentissage automatique, bien qu'efficaces, peuvent être influencés par des facteurs tels que la qualité de l'image, les caractéristiques spécifiques des données de formation, ou des cas rares non représentés dans le dataset. Une interprétation médicale experte est essentielle pour valider ou approfondir cette prédiction. En cas de doute, une analyse supplémentaire, telle qu'une biopsie ou une imagerie complémentaire, peut être nécessaire. L'objectif principal de cette prédiction est de fournir un aperçu préliminaire et d'aider les professionnels à prioriser les examens nécessitant une attention immédiate.
    """)
   
def credits():
    st.sidebar.title("Credits")
    st.sidebar.markdown(
        """
            - **ESSAMADI Oussama**
            - **ZOUIR Amine**
            - **CHIBI Mohammed**
        """
    )

