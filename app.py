import os
from PIL import Image
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sqlalchemy import create_engine
import streamlit as st

# ---------------------------------------------------------
# 1. Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Mohamed Gamal | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# 2. Custom CSS (Finovate Theme, Neon Glow & Bento Charts)
# ---------------------------------------------------------
st.markdown(
    """
<style>
    .stApp, .main {
        background-color: #060B19 !important;
    }
    
    [data-testid="stSidebar"] {
        background-color: #091124 !important;
        border-right: 1px solid #18294A;
        padding-top: 1.5rem;
    }
    [data-testid="stSidebar"] * {
        color: #E2E8F0 !important;
    }
    [data-testid="stSidebar"] h1 {font-size: 22px !important; color: #FFFFFF !important;}
    [data-testid="stSidebar"] h3 {font-size: 15px !important; color: #38BDF8 !important;}
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 0.5rem !important;
        padding-left: 1.2rem !important;
        padding-right: 1.2rem !important;
    }
    
    /* Hero Section Container with Neon Glow */
    .hero-container {
        background: linear-gradient(145deg, #0D182E 0%, #0A1324 100%);
        border: 1px solid #1E355E;
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 0 35px rgba(56, 189, 248, 0.2), inset 0 1px 1px rgba(255, 255, 255, 0.1);
        margin-bottom: 25px;
    }
    
    .hero-title {
        font-size: 2.8rem !important;
        font-weight: 800 !important;
        color: #FFFFFF !important;
        margin-bottom: 5px;
        text-shadow: 0 2px 12px rgba(56, 189, 248, 0.4);
    }
    
    .hero-subtitle {
        font-size: 1.4rem !important;
        font-weight: 600 !important;
        color: #38BDF8 !important;
        margin-bottom: 15px;
    }
    
    .hero-desc {
        font-size: 1.05rem !important;
        color: #94A3B8 !important;
        line-height: 1.6;
        margin-bottom: 25px;
    }
    
    /* Stats Bar (Bottom of Hero) */
    .stats-container {
        display: flex;
        justify-content: space-around;
        background: rgba(13, 24, 46, 0.7);
        border: 1px solid #1E355E;
        border-radius: 14px;
        padding: 20px;
        margin-top: 25px;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.1);
    }
    .stat-box {
        text-align: center;
    }
    .stat-number {
        font-size: 1.8rem;
        font-weight: 800;
        color: #00E5B0;
    }
    .stat-label {
        font-size: 0.9rem;
        color: #94A3B8;
        font-weight: 500;
    }

    /* Section Headers */
    .section-header {
        font-size: 1.6rem;
        font-weight: 700;
        color: #38BDF8 !important;
        border-bottom: 2px solid #1E355E;
        padding-bottom: 8px;
        margin-top: 35px;
        margin-bottom: 20px;
    }
    
    /* Skill Cards */
    .skill-card {
        background: linear-gradient(145deg, #0D182E 0%, #0A1324 100%) !important;
        color: #F8FAFC !important;
        padding: 20px;
        border-radius: 14px;
        border: 1px solid #1E355E;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.12);
        margin-bottom: 15px;
        height: 100%;
        transition: all 0.3s ease;
    }
    .skill-card:hover {
        border-color: #38BDF8;
        box-shadow: 0 0 30px rgba(56, 189, 248, 0.35);
        transform: translateY(-3px);
    }
    .skill-card h4 {
        color: #38BDF8 !important;
        margin-bottom: 12px;
        font-size: 1.15rem;
    }
    .skill-card ul {
        margin-bottom: 0;
        padding-left: 18px;
    }
    .skill-card ul li {
        color: #CBD5E1 !important;
        font-size: 0.95rem;
        margin-bottom: 6px;
    }
    
    /* إطار الصورة الدائرية وتأثير النيون */
    [data-testid="stImage"] img {
        border-radius: 50% !important;
        width: 230px !important;
        height: 230px !important;
        object-fit: cover !important;
        background-color: transparent !important;
        border: 4px solid #38BDF8 !important;
        box-shadow: 0 0 30px rgba(56, 189, 248, 0.5) !important;
        margin: 0 auto !important;
        display: block !important;
    }

    /* Enlarged & Filled KPI Card Layout for Dashboard */
    .kpi-card {
        background: linear-gradient(145deg, #0D182E 0%, #0A1324 100%);
        border: 1px solid #1E355E;
        border-radius: 12px;
        padding: 10px 14px;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.22), inset 0 1px 1px rgba(255, 255, 255, 0.12);
        display: flex;
        align-items: center;
        justify-content: space-between;
        height: 85px;
        transition: all 0.3s ease;
    }
    .kpi-card:hover {
        border-color: #38BDF8;
        box-shadow: 0 0 35px rgba(56, 189, 248, 0.5);
        transform: translateY(-2px);
    }
    .kpi-content {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .kpi-title {
        color: #8A99B5 !important;
        font-size: 12px !important;
        font-weight: 600;
        margin-bottom: 1px;
        white-space: nowrap;
        letter-spacing: 0.3px;
    }
    .kpi-value {
        color: #FFFFFF !important;
        font-size: 19px !important;
        font-weight: 800;
        line-height: 1.2;
        letter-spacing: 0.2px;
    }
    .kpi-delta {
        font-size: 11px !important;
        font-weight: 700;
        margin-top: 3px;
        display: flex;
        align-items: center;
        gap: 3px;
    }
    .kpi-icon {
        font-size: 32px;
        display: flex;
        align-items: center;
        justify-content: center;
        filter: drop-shadow(0 0 10px rgba(56,189,248,0.7));
    }

    /* Bento Box Styling for Plotly Charts */
    div[data-testid="stPlotlyChart"] {
        background: linear-gradient(145deg, #0D182E 0%, #0A1324 100%) !important;
        border: 1px solid #1E355E;
        border-radius: 12px;
        padding: 6px;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.18), inset 0 1px 1px rgba(255, 255, 255, 0.1);
        margin-bottom: 6px;
        transition: all 0.3s ease;
    }
    div[data-testid="stPlotlyChart"]:hover {
        border-color: #38BDF8;
        box-shadow: 0 0 40px rgba(56, 189, 248, 0.4);
    }
</style>
""",
    unsafe_allow_html=True,
)

# Color Palette
MINT_GREEN = "#00E5B0"
CYAN_BLUE = "#38BDF8"
ROYAL_BLUE = "#3B82F6"
VIOLET_PURPLE = "#8B5CF6"
CORAL_RED = "#F43F5E"
FINOVATE_PALETTE = [
    "#00E5B0",
    "#38BDF8",
    "#3B82F6",
    "#8B5CF6",
    "#6366F1",
    "#2DD4BF",
    "#A855F7",
]

# ---------------------------------------------------------
# 3. Sidebar Navigation & Data Loader
# ---------------------------------------------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Select Section:",
    [
        "Profile",
        "Olist E-Commerce Analytics",
    ],
)
st.sidebar.markdown("---")


@st.cache_data(ttl=600)
def load_full_data():
    server = "DESKTOP-P4GO8F9\\SQLEXPRESS"
    database = "Olist_Ecommerce_DB"
    driver = "ODBC Driver 17 for SQL Server"
    engine = create_engine(
        f"mssql+pyodbc://@{server}/{database}?
