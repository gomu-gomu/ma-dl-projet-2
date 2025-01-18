import streamlit as st



def header(title: str):
    st.image("assets/ui/banner.png", use_container_width=True)
    st.title(title)

def credits():
    st.sidebar.title("Credits")
    st.sidebar.markdown(
        """
            - **ESSAMADI Oussama**
            - **ZOUIR Amine**
            - **CHIBI Mohammed**
        """
    )

