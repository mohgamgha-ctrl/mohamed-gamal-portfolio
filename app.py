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

    dates = pd.date_range(start="2024-01-01", periods=n, freq="D")
    data = {
        "OrderDate": np.random.choice(dates, n),
        "Category": np.random.choice(categories, n, p=[0.4, 0.2, 0.2, 0.2]),
        "Region": np.random.choice(regions, n),
        "SalesAmount": np.random.uniform(20, 3500, n).round(2),
        "OrderQuantity": np.random.randint(1, 8, n),
    }
    df = pd.DataFrame(data)
    df["YearMonth"] = df["OrderDate"].dt.to_period("M").astype(str)
    return df


# ---------------------------------------------------------
# PAGE 1: Profile
# ---------------------------------------------------------
if page == "Profile":
    # Hero Section Box
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)

    col_img, col_info = st.columns([1.1, 2.4], gap="medium")

    with col_img:
        img_file = None
        for name in [
            "profile.png",
            "profile.jpg",
            "profile.jpeg",
            "Profile.jpg",
        ]:
            if os.path.exists(name):
                img_file = name
                break

        if img_file:
            # تم تعديل السطر لضمان عرض الصورة بأعلى جودة ودون ضغط
            st.image(img_file, use_container_width=True)
        else:
            st.warning("⚠️ يرجى رفع صورة باسم 'profile.jpg' أو 'Profile.jpg'")

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

        # Download CV Button inside Hero
        cv_filename = "Mohamed Gamal - Data Analyst CV.pdf"
        if not os.path.exists(cv_filename):
            cv_filename = (
                "Mohamed_gamal_mahmoud_Ebrahim_Naukrigulf_CV_09Oct2026.pdf"
            )

        if os.path.exists(cv_filename):
            with open(cv_filename, "rb") as pdf_file:
                st.download_button(
                    label="📄 Download CV",
                    data=pdf_file,
                    file_name="Mohamed_Gamal_Data_Analyst_CV.pdf",
                    mime="application/pdf",
                )

    st.markdown("</div>", unsafe_allow_html=True)  # End of Hero Container

    # Stats Bar Section
    st.markdown(
        """
        <div class="stats-container">
            <div class="stat-box">
                <div class="stat-number">2+</div>
                <div class="stat-label">Years of Experience</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">15+</div>
                <div class="stat-label">Projects Completed</div>
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

    # Technical Skills Section
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

    # Professional Experience
    st.markdown(
        '<div class="section-header">💼 Professional Experience</div>',
        unsafe_allow_html=True,
    )
    st.write("""
        * **Statistical & Medical Records Technician / Data Analyst — Ministry of Health (Oct 2024 - Present | Damietta, Egypt):**
          * Manage and maintain EHR/EMR databases, ensuring high data accuracy and integrity across patient medical records.
          * Extract and analyze monthly operational hospital metrics (patient volume, length of stay, bed occupancy rates).
          * Develop data visualizations and statistical reports to facilitate data-driven decisions for healthcare administrative teams.

        * **Data Analytics Specialist (Healthcare Unit) — Basatin Health Unit (Mar 2023 - Oct 2024 | Damietta, Egypt):**
          * Handled health statistics, patient intake record validation, and data cleaning for regional primary care operations.
          * Optimized reporting efficiency by building automated data consolidation workflows using Python and Advanced Excel.
        """)

    col_edu, col_lang = st.columns(2)
    with col_edu:
        st.markdown(
            '<div class="section-header">🎓 Education</div>',
            unsafe_allow_html=True,
        )
        st.write("""
            * **Diploma in Medical Informatics & Health Records Management**  
              *Technical Institute of Health — Port Said, Egypt (Graduated: 2023)*
            """)

    with col_lang:
        st.markdown(
            '<div class="section-header">🌐 Languages</div>',
            unsafe_allow_html=True,
        )
        st.write("""
            * **Arabic:** Native  
            * **English:** Professional Working Proficiency
            """)

# ---------------------------------------------------------
# PAGE 2: Healthcare Billing Analytics
# ---------------------------------------------------------
elif page == "Healthcare Billing Analytics":
    st.markdown(
        '<div class="hero-title" style="font-size: 2.2rem !important;">🏥 Healthcare Billing Dashboard</div>',
        unsafe_allow_html=True,
    )
    st.write(
        "Interactive analytics for medical billing, specialty distribution, and insurance claims."
    )

    df_health = get_healthcare_data()

    st.sidebar.markdown("### 🔍 Filters")
    selected_spec = st.sidebar.multiselect(
        "Specialty:",
        df_health["Specialty"].unique(),
        default=df_health["Specialty"].unique(),
    )
    selected_ins = st.sidebar.multiselect(
        "Insurance Provider:",
        df_health["Insurance_Provider"].unique(),
        default=df_health["Insurance_Provider"].unique(),
    )

    filtered_health = df_health[
        (df_health["Specialty"].isin(selected_spec))
        & (df_health["Insurance_Provider"].isin(selected_ins))
    ]

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Total Patients", f"{len(filtered_health):,}")
    kpi2.metric(
        "Total Billing Amount", f"${filtered_health['Billing_Amount'].sum():,.2f}"
    )
    kpi3.metric(
        "Avg Length of Stay", f"{filtered_health['LOS_Days'].mean():.1f} Days"
    )
    kpi4.metric(
        "Avg Bill Amount", f"${filtered_health['Billing_Amount'].mean():,.2f}"
    )

    st.markdown("---")

    col_h1, col_h2 = st.columns(2)
    with col_h1:
        fig_spec = px.pie(
            filtered_health,
            names="Specialty",
            values="Billing_Amount",
            title="Billing Breakdown by Specialty",
            hole=0.4,
            template="plotly_dark",
        )
        st.plotly_chart(fig_spec, use_container_width=True)

    with col_h2:
        df_ins = (
            filtered_health.groupby("Insurance_Provider")["Billing_Amount"]
            .sum()
            .reset_index()
        )
        fig_ins = px.bar(
            df_ins,
            x="Insurance_Provider",
            y="Billing_Amount",
            color="Insurance_Provider",
            title="Claims by Insurance Provider",
            template="plotly_dark",
        )
        st.plotly_chart(fig_ins, use_container_width=True)

# ---------------------------------------------------------
# PAGE 3: AdventureWorks Sales Analytics
# ---------------------------------------------------------
elif page == "AdventureWorks Sales Analytics":
    st.markdown(
        '<div class="hero-title" style="font-size: 2.2rem !important;">🛒 AdventureWorks Sales Dashboard</div>',
        unsafe_allow_html=True,
    )
    st.write(
        "Sales analytics dashboard for evaluating commercial performance, revenue trends, and regional distributions."
    )

    df_sales = get_sales_data()

    st.sidebar.markdown("### 🔍 Filters")
    selected_cat = st.sidebar.multiselect(
        "Product Category:",
        df_sales["Category"].unique(),
        default=df_sales["Category"].unique(),
    )
    selected_reg = st.sidebar.multiselect(
        "Region:",
        df_sales["Region"].unique(),
        default=df_sales["Region"].unique(),
    )

    filtered_sales = df_sales[
        (df_sales["Category"].isin(selected_cat))
        & (df_sales["Region"].isin(selected_reg))
    ]

    s1, s2, s3 = st.columns(3)
    s1.metric("Total Revenue", f"${filtered_sales['SalesAmount'].sum():,.2f}")
    s2.metric("Total Orders", f"{len(filtered_sales):,}")
    s3.metric("Avg Order Value", f"${filtered_sales['SalesAmount'].mean():,.2f}")

    st.markdown("---")

    col_s1, col_s2 = st.columns(2)
    with col_s1:
        monthly_sales = (
            filtered_sales.groupby("YearMonth")["SalesAmount"]
            .sum()
            .reset_index()
            .sort_values("YearMonth")
        )
        fig_trend = px.line(
            monthly_sales,
            x="YearMonth",
            y="SalesAmount",
            title="Monthly Sales Trend",
            markers=True,
            template="plotly_dark",
        )
        st.plotly_chart(fig_trend, use_container_width=True)

    with col_s2:
        df_reg = (
            filtered_sales.groupby("Region")["SalesAmount"]
            .sum()
            .reset_index()
        )
        fig_reg = px.bar(
            df_reg,
            x="Region",
            y="SalesAmount",
            color="Region",
            title="Revenue by Geographic Region",
            template="plotly_dark",
        )
        st.plotly_chart(fig_reg, use_container_width=True)
