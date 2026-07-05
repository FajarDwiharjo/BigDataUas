import streamlit as st


def apply_style():
    """
    Apply global Streamlit styling for a Power BI-like dashboard UI.

    This includes:
    - Dark professional theme
    - Card-like containers
    - Consistent spacing
    - Clean typography
    - Metric highlight styling
    """

    st.set_page_config(
        page_title="E-Commerce Dashboard",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.markdown(
        """
        <style>

        /* ----------------------------
        GLOBAL BACKGROUND
        ---------------------------- */
        .stApp {
            background-color: #0E1117;
            color: #E6E6E6;
        }

        /* ----------------------------
        SIDEBAR STYLE
        ---------------------------- */
        section[data-testid="stSidebar"] {
            background-color: #111827;
            border-right: 1px solid #2A2F3A;
        }

        /* Sidebar text */
        .stSidebar label, .stSidebar span {
            color: #E6E6E6 !important;
        }

        /* ----------------------------
        METRIC CARDS
        ---------------------------- */
        div[data-testid="metric-container"] {
            background-color: #111827;
            border: 1px solid #2A2F3A;
            padding: 16px;
            border-radius: 10px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.3);
        }

        div[data-testid="metric-container"] label {
            color: #9CA3AF !important;
            font-size: 13px;
        }

        div[data-testid="metric-container"] div {
            color: #FFFFFF !important;
            font-size: 22px;
            font-weight: 600;
        }

        /* ----------------------------
        DATAFRAME STYLE
        ---------------------------- */
        .stDataFrame {
            border-radius: 10px;
            overflow: hidden;
            border: 1px solid #2A2F3A;
        }

        /* ----------------------------
        HEADERS
        ---------------------------- */
        h1, h2, h3 {
            color: #FFFFFF !important;
            font-weight: 600;
        }

        /* ----------------------------
        BUTTON STYLE
        ---------------------------- */
        .stButton > button {
            background-color: #2563EB;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 8px 16px;
            font-weight: 500;
        }

        .stButton > button:hover {
            background-color: #1D4ED8;
            color: white;
        }

        /* ----------------------------
        REMOVE STREAMLIT DEFAULT SPACING
        ---------------------------- */
        .block-container {
            padding-top: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
    