import streamlit as st
import pages.home
import pages.about

# Page mapping: file/module names to custom display names
PAGES = {
    "Home": pages.home,
    "About Us": pages.about,
}

# Sidebar navigation
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", list(PAGES.keys()))

# Display the selected page
page = PAGES[selected_page]
page.app()

