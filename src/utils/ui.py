import numpy as np
import streamlit as st



def header(title: str):
    st.image("assets/ui/banner.png", use_container_width=True)
    st.title(title)

def controls():
    threshold = 0.5
    mammogram = st.sidebar.file_uploader("Sélectionnez une mammographie", type="png")

    if mammogram:
        threshold = st.sidebar.slider("Seuil", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

    return mammogram, threshold


def credits():
    st.sidebar.title("Credits")
    st.sidebar.markdown(
        """
            - **ESSAMADI Oussama**
            - **ZOUIR Amine**
            - **CHIBI Mohammed**
        """
    )

