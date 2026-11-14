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
# Custom Styling (CSS)
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
    .hero-container {
        background: linear-gradient(145deg, #0D182E 0%, #0A1324 100%);
        border: 1px solid #1E355E;
        border-radius: 20px;
        padding: 40px;
        box-shadow: 0 0 35px rgba(56, 189, 248, 0.2);
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
    .stats-container {
        display: flex;
        justify-content: space-around;
        background: rgba(13, 24, 46, 0.7);
        border: 1px solid #1E355E;
        border-radius: 14px;
        padding: 20px;
        margin-top: 30px;
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
    .section-header {
        font-size: 1.6rem;
        font-weight: 700;
        color: #38BDF8 !important;
        border-bottom: 2px solid #1E355E;
        padding-bottom: 8px;
        margin-top: 35px;
        margin-bottom: 20px;
    }
    .skill-card {
        background: linear-gradient(145deg, #0D182E 0%, #0A1324 100%) !important;
        color: #F8FAFC !important;
        padding: 20px;
        border-radius: 14px;
        border: 1px solid #1E355E;
        box-shadow: 0 0 20px rgba(56, 189, 248, 0.12);
        margin-bottom: 15px;
        height: 100%;
    }
    .skill-card h4 {
        color: #38BDF8 !important;
        margin-bottom: 12px;
    }
    .skill-card ul li {
        color: #CBD5E1 !important;
        font-size: 0.95rem;
        margin-bottom: 6px;
    }
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
# Sidebar Navigation (طريقة الربط الأساسية)
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


# ---------------------------------------------------------
# Data Loader for Olist Project
# ---------------------------------------------------------
@st.cache_data
def get_olist_data():
    import numpy as np

    np.random.seed(42)
    n = 500
    categories = [
        "Health & Beauty",
        "Computers & Accessories",
        "Watches & Gifts",
        "Bed Table & Bath",
        "Sports & Leisure",
    ]
    payment_types = ["credit_card", "boleto", "voucher", "debit_card"]
    states = ["SP", "RJ", "MG", "RS", "PR"]

    dates = pd.date_range(start="2023-01-01", periods=n, freq="D")
    data = {
        "Order_Date": np.random.choice(dates, n),
        "Product_Category": np.random.choice(categories, n),
        "Payment_Type": np.random.choice(payment_types, n, p=[0.7, 0.15, 0.1, 0.05]),
        "Customer_State": np.random.choice(states, n, p=[0.4, 0.2, 0.2, 0.1, 0.1]),
        "Price": np.random.uniform(30, 2500, n).round(2),
        "Freight_Value": np.random.uniform(10, 150, n).round(2),
        "Review_Score": np.random.choice([1, 2, 3, 4, 5], n, p=[0.1, 0.1, 0.15, 0.3, 0.35]),
    }
    df = pd.DataFrame(data)
    df["Total_Revenue"] = df["Price"] + df["Freight_Value"]
    df["Year"] = df["Order_Date"].dt.year.astype(str)
    df["YearMonth"] = df["Order_Date"].dt.to_period("M").astype(str)
    return df


# ---------------------------------------------------------
# PAGE 1: Profile
# ---------------------------------------------------------
if page == "Profile":
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)
    col_img, col_info = st.columns([1.1, 2.4], gap="medium")

    with col_img:
        img_file = "Profile.jpg" if os.path.exists("Profile.jpg") else "profile.jpg"
        if os.path.exists(img_file):
            st.image(img_file, use_container_width=True)
        else:
            st.warning("⚠️ يرجى رفع صورة Profile.jpg")

    with col_info:
        st.markdown(
            '<div style="color: #38BDF8; font-weight: 600; font-size: 1.1rem; margin-bottom: 5px;">Hello, I\'m</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="hero-title">Mohamed Gamal</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="hero-subtitle">And I\'m a Healthcare & Business Data Analyst</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            '<div class="hero-desc">Data Analyst with over 2 years of experience in healthcare statistical management and business analytics. Specialized in leveraging Python, SQL, and Streamlit to transform complex data into actionable executive insights.</div>',
            unsafe_allow_html=True,
        )

        cv_filename = "Mohamed Gamal - Data Analyst CV.pdf"
        if os.path.exists(cv_filename):
            with open(cv_filename, "rb") as pdf_file:
                st.download_button(
                    label="📄 Download CV",
                    data=pdf_file,
                    file_name="Mohamed_Gamal_Data_Analyst_CV.pdf",
                    mime="application/pdf",
                )

    st.markdown("</div>", unsafe_allow_html=True)

    # Stats Bar
    st.markdown(
        """
        <div class="stats-container">
            <div class="stat-box">
                <div class="stat-number">2+</div>
                <div class="stat-label">Years of Experience</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">1+</div>
                <div class="stat-label">Featured Projects</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">4+</div>
                <div class="stat-label">Core Technologies</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">100%</div>
                <div class="stat-label">Data Accuracy</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Technical Skills
    st.markdown(
        '<div class="section-header">🛠️ Technical Skills & Core Competencies</div>',
        unsafe_allow_html=True,
    )
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            """
            <div class="skill-card">
                <h4>🐍 Programming</h4>
                <ul>
                    <li>Python (Pandas, NumPy)</li>
                    <li>Data Cleaning & EDA</li>
                    <li>Matplotlib & Seaborn</li>
                    <li>Plotly & Streamlit</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="skill-card">
                <h4>🗄️ Databases</h4>
                <ul>
                    <li>SQL Aggregations & Joins</li>
                    <li>Subqueries & Windows</li>
                    <li>SQL Server (SSMS)</li>
                    <li>Data Transformation</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class="skill-card">
                <h4>📊 BI & Web Apps</h4>
                <ul>
                    <li>Streamlit Dashboards</li>
                    <li>Power BI Reports</li>
                    <li>Advanced Excel</li>
                    <li>Pivot Tables</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c4:
        st.markdown(
            """
            <div class="skill-card">
                <h4>🏥 Healthcare</h4>
                <ul>
                    <li>EHR / EMR Systems</li>
                    <li>Health Statistics</li>
                    <li>Hospital KPIs</li>
                    <li>Billing Analytics</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ---------------------------------------------------------
# PAGE 2: Olist E-Commerce Analytics
# ---------------------------------------------------------
elif page == "Olist E-Commerce Analytics":
    st.markdown(
        '<div class="hero-title" style="font-size: 2.2rem !important;">🛒 Olist E-Commerce Executive Dashboard</div>',
        unsafe_allow_html=True,
    )
    st.write(
        "Comprehensive analytics platform evaluating Brazilian e-commerce performance, revenue trends, payment behavior, and customer satisfaction."
    )

    df_olist = get_olist_data()

    # Filters inside sidebar when this page is active
    st.sidebar.markdown("### 🔍 Dashboard Filters")
    selected_year = st.sidebar.multiselect(
        "Select Year:",
        sorted(df_olist["Year"].unique()),
        default=df_olist["Year"].unique(),
    )
    selected_cat = st.sidebar.multiselect(
        "Product Category:",
        df_olist["Product_Category"].unique(),
        default=df_olist["Product_Category"].unique(),
    )
    selected_pay = st.sidebar.multiselect(
        "Payment Type:",
        df_olist["Payment_Type"].unique(),
        default=df_olist["Payment_Type"].unique(),
    )

    filtered_df = df_olist[
        (df_olist["Year"].isin(selected_year))
        & (df_olist["Product_Category"].isin(selected_cat))
        & (df_olist["Payment_Type"].isin(selected_pay))
    ]

    # Metrics
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Total Revenue", f"${filtered_df['Total_Revenue'].sum():,.2f}")
    kpi2.metric("Total Orders", f"{len(filtered_df):,}")
    kpi3.metric("Avg Order Value", f"${filtered_df['Total_Revenue'].mean():,.2f}")
    kpi4.metric("Avg Review Score", f"⭐ {filtered_df['Review_Score'].mean():.2f} / 5")

    st.markdown("---")

    # Charts layout
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        monthly_rev = (
            filtered_df.groupby("YearMonth")["Total_Revenue"]
            .sum()
            .reset_index()
            .sort_values("YearMonth")
        )
        fig_trend = px.line(
            monthly_rev,
            x="YearMonth",
            y="Total_Revenue",
            title="Monthly Revenue Trajectory",
            markers=True,
            template="plotly_dark",
        )
        st.plotly_chart(fig_trend, use_container_width=True)

    with col_c2:
        pay_df = (
            filtered_df.groupby("Payment_Type")["Total_Revenue"]
            .sum()
            .reset_index()
        )
        fig_pay = px.bar(
            pay_df,
            x="Payment_Type",
            y="Total_Revenue",
            color="Payment_Type",
            title="Revenue Distribution by Payment Method",
            template="plotly_dark",
        )
        st.plotly_chart(fig_pay, use_container_width=True)
