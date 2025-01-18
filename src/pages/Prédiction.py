import streamlit as st
from utils import ui



ui.header()
col1, col2 = st.columns([2, 1])

with col1:
    st.image("assets/ui/benign.png", use_container_width=True)
    st.write("<breakdown>")

with col2:
    st.image("assets/mammograms/benign.png", use_container_width=True)
    st.write("<chart>")
    st.write("<confidence>")

