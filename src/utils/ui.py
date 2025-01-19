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

def credits():
    st.sidebar.title("Credits")
    st.sidebar.markdown(
        """
            - **ESSAMADI Oussama**
            - **ZOUIR Amine**
            - **CHIBI Mohammed**
        """
    )

