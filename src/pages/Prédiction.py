import streamlit as st
from utils import ui



ui.header()
col1, col2 = st.columns([2, 1])

with col1:
    st.image("assets/ui/malignant.png", use_container_width=True)

with col2:
    pass

