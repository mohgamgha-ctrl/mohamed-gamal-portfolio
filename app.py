import os
from PIL import Image
import pandas as pd
import plotly.express as px
import streamlit as st

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Mohamed Gamal | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------
# Custom Styling (CSS) - Modern Dark Neon Hero & Finovate Theme
# ---------------------------------------------------------
st.markdown(
    """
    <style>
    /* Main App Background */
    .stApp, .main {
        background-color: #060B19 !important;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #091124 !important;
        border-right: 1px solid #18294A;
        padding-top: 1.5rem;
    }
    [data-testid="stSidebar"] * {
        color: #E2E8F0 !important;
    }
    
    /* Hero Section Container with Neon Glow */
    .hero-container {
        background: linear-gradient(145deg, #0D182E 0%, #0A1324 100%);
        border: 1px solid #1E355E;
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 0 35px rgba(56, 189, 248, 0.2), inset 0 1px 1px rgba(255, 255, 255, 0.1);
        margin-bottom: 30px;
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
        margin-top: 30px;
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
    
    /* إزالة أي خلفية بيضاء وضبط الصورة الدائرية بإطار نيون متناسق */
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
    </style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Select Section:",
    [
        "Profile",
        "Healthcare Billing Analytics",
        "AdventureWorks Sales Analytics",
    ],
)
st.sidebar.markdown("---")


# ---------------------------------------------------------
# Data Loaders
# ---------------------------------------------------------
@st.cache_data
def get_healthcare_data():
    import numpy as np

    np.random.seed(42)
    n = 300
    specialties = ["Inpatient", "Outpatient", "Emergency", "Surgery", "ICU"]
    insurance_providers = [
        "Medicare",
        "Medicaid",
        "Private Insurance",
        "Self-Pay",
    ]

    dates = pd.date_range(start="2025-01-01", periods=n, freq="D")
    data = {
        "Admission_Date": np.random.choice(dates, n),
        "Specialty": np.random.choice(specialties, n, p=[0.3, 0.3, 0.2, 0.1, 0.1]),
        "Insurance_Provider": np.random.choice(insurance_providers, n),
        "Billing_Amount": np.random.uniform(500, 15000, n).round(2),
        "LOS_Days": np.random.randint(1, 15, n),
    }
    df = pd.DataFrame(data)
    df["YearMonth"] = df["Admission_Date"].dt.to_period("M").astype(str)
    return df


@st.cache_data
def get_sales_data():
    import numpy as np

    np.random.seed(101)
    n = 400
    categories = ["Bikes", "Components", "Clothing", "Accessories"]
    regions = ["North America", "Europe", "Pacific"]
