
import os
from datetime import datetime

import pandas as pd
import streamlit as st

# -----------------------------------------------------------------------------
# SIDEBAR AND TOP NAVIGATION
# -----------------------------------------------------------------------------

st.sidebar.markdown("### 🚀 NovaTech Solutions")
st.sidebar.markdown("*We Build Intelligent Software for a Smarter Future.*")
st.sidebar.markdown("---")

PAGES = [
    "Home",
    "About Us",
    "Services",
    "Portfolio",
    "Contact Us",
    "AI Assistant",
    "Client Dashboard",
    "Admin Dashboard",
]

if "menu" not in st.session_state:
    st.session_state.menu = "Home"


def go_to_page(page_name):
    st.session_state.menu = page_name


menu = st.sidebar.radio(
    "Navigation",
    PAGES,
    key="menu",
)

# Website ke top par clickable navigation buttons
st.markdown("---")
st.markdown("### Explore NovaTech Solutions")

nav_columns = st.columns(4)

for index, page_name in enumerate(PAGES[:4]):
    with nav_columns[index]:
        st.button(
            page_name,
            key=f"top_nav_{index}",
            use_container_width=True,
            type="primary" if menu == page_name else "secondary",
            on_click=go_to_page,
            args=(page_name,),
        )

nav_columns_2 = st.columns(4)

for index, page_name in enumerate(PAGES[4:], start=4):
    with nav_columns_2[index - 4]:
        st.button(
            page_name,
            key=f"top_nav_{index}",
            use_container_width=True,
            type="primary" if menu == page_name else "secondary",
            on_click=go_to_page,
            args=(page_name,),
        )

st.markdown("---")
