import os
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ---------------------------------------------------------
# 1. Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Mohamed Gamal | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------
# 2. Session State for Project Details Toggle
# ---------------------------------------------------------
if "open_pepsi" not in st.session_state:
    st.session_state.open_pepsi = False
if "open_healthcare" not in st.session_state:
    st.session_state.open_healthcare = False
if "open_olist" not in st.session_state:
    st.session_state.open_olist = False

# ---------------------------------------------------------
# 3. Custom CSS (Light, Calm & Cohesive Palette)
# ---------------------------------------------------------
st.markdown(
    """
<style>
    .stApp, .main {
        background-color: #F8FAFC !important;
        color: #0F172A !important;
    }

    /* Hide Sidebar Completely */
    [data-testid="stSidebar"],
    [data-testid="collapsedControl"] {
        display: none !important;
    }

    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
        padding-left: 1.8rem !important;
        padding-right: 1.8rem !important;
        max-width: 100% !important;
    }

    /* Hero Section Container */
    .hero-container {
        background: linear-gradient(135deg, #FFFFFF 0%, #F1F5F9 100%);
        border: 1px solid #E2E8F0;
        border-radius: 20px;
        padding: 30px 40px;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.05);
        margin-top: 0px !important;
        margin-bottom: 22px;
    }

    .hero-title {
        font-size: 2.7rem !important;
        font-weight: 800 !important;
        color: #0F172A !important;
        margin-bottom: 6px;
    }

    .hero-subtitle {
        font-size: 1.35rem !important;
        font-weight: 600 !important;
        color: #0D9488 !important;
        margin-bottom: 14px;
    }

    .hero-desc {
        font-size: 1.05rem !important;
        color: #475569 !important;
        line-height: 1.65;
        margin-bottom: 22px;
    }

    /* Stats Bar */
    .stats-container {
        display: flex;
        justify-content: space-around;
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 16px;
        padding: 20px;
        margin-top: 18px;
        box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04);
    }
    .stat-box {
        text-align: center;
    }
    .stat-number {
        font-size: 1.8rem;
        font-weight: 800;
        color: #0D9488;
    }
    .stat-label {
        font-size: 0.92rem;
        color: #64748B;
        font-weight: 600;
    }

    /* Section Headers */
    .section-header {
        font-size: 1.55rem;
        font-weight: 700;
        color: #0F172A !important;
        border-bottom: 2px solid #CBD5E1;
        padding-bottom: 8px;
        margin-top: 34px;
        margin-bottom: 18px;
    }

    /* Project Summary Card (Compact View on Scroll) */
    .project-summary-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-left: 5px solid #0D9488;
        border-radius: 16px;
        padding: 22px 26px;
        margin-bottom: 10px;
        box-shadow: 0 4px 16px rgba(15, 23, 42, 0.04);
        transition: all 0.25s ease;
    }
    .project-summary-card:hover {
        border-color: #99F6E4;
        box-shadow: 0 8px 24px rgba(13, 148, 136, 0.10);
    }
    .project-card-title {
        font-size: 1.5rem;
        font-weight: 800;
        color: #0F172A;
        margin-bottom: 6px;
    }
    .project-card-brief {
        color: #475569;
        font-size: 0.98rem;
        line-height: 1.6;
        margin-bottom: 12px;
    }
    .project-highlights {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        margin-top: 10px;
        margin-bottom: 8px;
        color: #0F766E;
        font-size: 0.88rem;
        font-weight: 700;
    }

    .tool-badge {
        display: inline-block;
        background: #F0FDFA;
        border: 1px solid #99F6E4;
        color: #0F766E;
        font-size: 0.8rem;
        font-weight: 600;
        padding: 4px 11px;
        border-radius: 999px;
        margin-right: 6px;
        margin-top: 4px;
    }

    /* Expanded Details Container */
    .project-details-box {
        background: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-radius: 16px;
        padding: 22px 24px;
        margin-top: 10px;
        margin-bottom: 24px;
        box-shadow: 0 6px 20px rgba(15, 23, 42, 0.04);
    }

    /* Filter Bar */
    .filter-bar {
        background: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 14px;
        padding: 14px 18px 6px 18px;
        margin-bottom: 14px;
    }

    /* Skill Cards */
    .skill-card {
        background: #FFFFFF !important;
        color: #0F172A !important;
        padding: 20px;
        border-radius: 14px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.04);
        margin-bottom: 15px;
        height: 100%;
        transition: all 0.25s ease;
    }
    .skill-card:hover {
        border-color: #5EEAD4;
        box-shadow: 0 8px 22px rgba(13, 148, 136, 0.09);
        transform: translateY(-2px);
    }
    .skill-card h4 {
        color: #0F766E !important;
        margin-bottom: 12px;
        font-size: 1.15rem;
    }
    .skill-card ul {
        margin-bottom: 0;
        padding-left: 18px;
    }
    .skill-card ul li {
        color: #334155 !important;
        font-size: 0.95rem;
        margin-bottom: 6px;
    }

    /* Profile Image Style */
    [data-testid="stImage"] img {
        border-radius: 50% !important;
        width: 220px !important;
        height: 220px !important;
        object-fit: cover !important;
        background-color: transparent !important;
        border: 4px solid #0D9488 !important;
        box-shadow: 0 8px 24px rgba(13, 148, 136, 0.18) !important;
        margin: 0 auto !important;
        display: block !important;
    }

    /* Compact & Centered Video Player */
    [data-testid="stVideo"] video {
        max-width: 720px !important;
        max-height: 400px !important;
        width: 100% !important;
        border-radius: 14px !important;
        border: 1px solid #CBD5E1 !important;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.10) !important;
        margin: 0 auto !important;
        display: block !important;
    }

    /* KPI Cards */
    .kpi-card {
        background: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 10px 14px;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
        display: flex;
        align-items: center;
        justify-content: space-between;
        height: 85px;
        margin-bottom: 8px;
        transition: all 0.25s ease;
    }
    .kpi-card:hover {
        border-color: #5EEAD4;
        box-shadow: 0 6px 18px rgba(13, 148, 136, 0.10);
        transform: translateY(-2px);
    }
    .kpi-content {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .kpi-title {
        color: #64748B !important;
        font-size: 12px !important;
        font-weight: 600;
        margin-bottom: 1px;
        white-space: nowrap;
        letter-spacing: 0.2px;
    }
    .kpi-value {
        color: #0F172A !important;
        font-size: 19px !important;
        font-weight: 800;
        line-height: 1.2;
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
        font-size: 30px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* Card Styling for Plotly Charts */
    div[data-testid="stPlotlyChart"] {
        background: #FFFFFF !important;
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        padding: 6px;
        box-shadow: 0 4px 14px rgba(15, 23, 42, 0.04);
        margin-bottom: 6px;
        transition: all 0.25s ease;
    }
    div[data-testid="stPlotlyChart"]:hover {
        border-color: #99F6E4;
        box-shadow: 0 6px 20px rgba(13, 148, 136, 0.09);
    }

    /* Toggle Button Styling */
    div.stButton > button {
        background: linear-gradient(90deg, #0D9488 0%, #2563EB 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        padding: 0.45rem 1.15rem !important;
        transition: all 0.2s ease !important;
    }
    div.stButton > button:hover {
        opacity: 0.94 !important;
        box-shadow: 0 6px 16px rgba(13, 148, 136, 0.25) !important;
        transform: translateY(-1px) !important;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Calm & Cohesive Light-Theme Palette
TEAL_PRIMARY = "#0D9488"
BLUE_ACCENT = "#2563EB"
SKY_SOFT = "#0284C7"
ROSE_SOFT = "#E11D48"
AMBER_SOFT = "#D97706"
LIGHT_PALETTE = [
    "#0D9488",
    "#2563EB",
    "#0284C7",
    "#4F46E5",
    "#14B8A6",
    "#6366F1",
    "#D97706",
]


def render_centered_video(video_path: str, missing_message: str):
    st.markdown(
        '<div style="color:#0F766E; font-weight:700; font-size:1.05rem; margin-bottom:8px;">🎬 عرض توضيحي للداشبورد (Dashboard Walkthrough)</div>',
        unsafe_allow_html=True,
    )
    if os.path.exists(video_path):
        _, mid_col, _ = st.columns([1, 2.2, 1])
        with mid_col:
            st.video(video_path)
    else:
        st.info(missing_message)


# ---------------------------------------------------------
# 4. Data Providers
# ---------------------------------------------------------
@st.cache_data
def load_full_data():
    np.random.seed(42)
    n = 1500
    categories = [
        "Health & Beauty",
        "Computers & Accessories",
        "Watches & Gifts",
        "Bed Table & Bath",
        "Sports & Leisure",
        "Housewares",
        "Cool Stuff",
        "Auto",
    ]
    payment_types = ["credit_card", "boleto", "voucher", "debit_card"]
    states = ["SP", "RJ", "MG", "RS", "PR", "SC", "BA"]
    statuses = ["delivered", "shipped", "processing", "invoiced"]

    dates = pd.date_range(start="2023-01-01", periods=730, freq="D")
    order_dates = np.random.choice(dates, n)

    data = {
        "order_id": [f"ord_{i:04d}" for i in range(n)],
        "order_item_id": np.random.choice([1, 2, 3], n, p=[0.8, 0.15, 0.05]),
        "price": np.random.uniform(40, 3000, n).round(2),
        "freight_value": np.random.uniform(10, 180, n).round(2),
        "customer_unique_id": [
            f"cust_{np.random.randint(1, 400)}" for _ in range(n)
        ],
        "customer_state": np.random.choice(
            states, n, p=[0.4, 0.2, 0.15, 0.1, 0.05, 0.05, 0.05]
        ),
        "customer_city": "City_Sample",
        "category": np.random.choice(categories, n),
        "seller_state": np.random.choice(states, n),
        "order_date": order_dates,
        "order_status": np.random.choice(statuses, n, p=[0.9, 0.04, 0.03, 0.03]),
        "payment_type": np.random.choice(
            payment_types, n, p=[0.74, 0.15, 0.07, 0.04]
        ),
    }
    df = pd.DataFrame(data)
    df["total_amount"] = df["price"] + df["freight_value"]
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["Year_Month"] = df["order_date"].dt.to_period("M").astype(str)
    df["Year"] = df["order_date"].dt.year.astype(str)
    df["Day_of_Week"] = df["order_date"].dt.day_name()
    df["Hour"] = np.random.randint(0, 24, n)

    df_pay = (
        df.groupby("payment_type")
        .agg(cnt=("order_id", "count"), val=("total_amount", "sum"))
        .reset_index()
    )

    rev_data = {
        "review_score": [1, 2, 3, 4, 5],
        "cnt": [
            int(n * 0.08),
            int(n * 0.06),
            int(n * 0.12),
            int(n * 0.32),
            int(n * 0.42),
        ],
    }
    df_rev = pd.DataFrame(rev_data)

    return df, df_pay, df_rev


@st.cache_data
def load_healthcare_summary_data():
    df_cond = pd.DataFrame(
        {
            "Medical_Condition": [
                "Cancer",
                "Heart Disease",
                "Alzheimer's",
                "Diabetes",
                "Hypertension",
                "Asthma",
            ],
            "Revenue_M": [245.6, 228.4, 204.8, 192.5, 178.2, 162.34],
        }
    )
    df_hosp = pd.DataFrame(
        {
            "Hospital": [
                "Hospital A",
                "Hospital B",
                "Hospital C",
                "Hospital D",
                "Hospital E",
            ],
            "Revenue_M": [278.4, 254.2, 238.9, 226.1, 214.24],
            "Doctors": [142, 128, 119, 112, 105],
        }
    )
    df_age = pd.DataFrame(
        {
            "Age_Group": ["18-30", "31-45", "46-60", "61-75", "75+"],
            "Patients": [8900, 11400, 13200, 12100, 9900],
        }
    )
    return df_cond, df_hosp, df_age


@st.cache_data
def load_pepsi_summary_data():
    df_yr = pd.DataFrame(
        {
            "Year": ["2022", "2023", "2024", "2025", "2026"],
            "Revenue_M": [0.78, 0.94, 1.08, 1.22, 1.15],
            "Net_Profit_M": [0.26, 0.32, 0.37, 0.41, 0.39],
            "Discount_K": [44.2, 52.8, 60.5, 68.1, 63.44],
        }
    )
    df_gov = pd.DataFrame(
        {
            "Governorate": [
                "Cairo",
                "Giza",
                "Alexandria",
                "Dakahlia",
                "Sharqia",
                "Gharbia",
            ],
            "Revenue_M": [1.34, 1.09, 0.88, 0.61, 0.56, 0.49],
        }
    )
    df_cat = pd.DataFrame(
        {
            "Category": [
                "Carbonated Cola",
                "Zero Sugar",
                "Flavored Sodas",
                "Energy & Juices",
            ],
            "Units_K": [138.0, 74.0, 62.0, 43.0],
        }
    )
    return df_yr, df_gov, df_cat


# ---------------------------------------------------------
# SECTION 1: Profile
# ---------------------------------------------------------
st.markdown('<div class="hero-container">', unsafe_allow_html=True)
col_img, col_info = st.columns([1.1, 2.4], gap="medium")

with col_img:
    img_file = None
    for name in [
        "Profile.jpg",
        "profile.jpg",
        "profile.png",
        "profile.jpeg",
    ]:
        if os.path.exists(name):
            img_file = name
            break

    if img_file:
        st.image(img_file, use_container_width=True)
    else:
        st.warning("⚠️ يرجى رفع صورة باسم 'Profile.jpg'")

with col_info:
    st.markdown(
        '<div style="color: #0D9488; font-weight: 700; font-size: 1.05rem; margin-bottom: 5px;">Hello, I\'m</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="hero-title">Mohamed Gamal</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="hero-subtitle">Healthcare & Business Data Analyst</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="hero-desc">Data Analyst with over 2 years of experience in healthcare statistical management and business analytics. Specialized in leveraging Python, SQL, and Streamlit to transform complex data into actionable executive insights.</div>',
        unsafe_allow_html=True,
    )

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
            <div class="stat-number">3+</div>
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


def render_kpi(title, value, delta_tuple, icon):
    delta_html, _ = delta_tuple
    st.markdown(
        f"""
        <div class="kpi-card">
            <div class="kpi-content">
                <div class="kpi-title">{title}</div>
                <div class="kpi-value">{value}</div>
                <div class="kpi-delta">{delta_html}</div>
            </div>
            <div class="kpi-icon">{icon}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def style_square_fig(fig, title, margin=dict(l=20, r=30, t=55, b=20)):
    fig.update_layout(
        autosize=True,
        title=dict(
            text=title,
            font=dict(size=16, color="#0F172A", family="sans-serif"),
            x=0.03,
            y=0.92,
        ),
        template="plotly_white",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        height=220,
        margin=margin,
        font=dict(size=13, color="#334155"),
        showlegend=False,
        coloraxis_showscale=False,
        hoverlabel=dict(
            bgcolor="#FFFFFF",
            bordercolor="#0D9488",
            font=dict(size=14, color="#0F172A", family="sans-serif"),
        ),
    )
    fig.update_xaxes(
        showgrid=False,
        linecolor="#CBD5E1",
        tickfont=dict(size=12, color="#475569"),
    )
    fig.update_yaxes(
        gridcolor="#E2E8F0",
        zerolinecolor="#CBD5E1",
        tickfont=dict(size=12, color="#475569"),
    )
    return fig


# ---------------------------------------------------------
# SECTION 2: Featured Projects (Brief Cards -> Click to Expand)
# ---------------------------------------------------------
st.markdown(
    '<div class="section-header">🚀 Featured Projects</div>',
    unsafe_allow_html=True,
)

# =========================================================
# PROJECT 1: Pepsi Egypt Sales Analytics (2022 – 2026)
# =========================================================
st.markdown(
    """
    <div class="project-summary-card">
        <div class="project-card-title">🥤 Pepsi Egypt Sales Analytics (2022 – 2026) | End-to-End BI Project</div>
        <div class="project-card-brief">
            دورة تحليل متكاملة لتحليل مبيعات Pepsi في مصر خلال 5 سنوات (بيانات تجريبية Synthetic Data تحاكي مشاكل البيانات الحقيقية) بدءاً من تنظيف الداتا بـ Python وبناء Star Schema ومراجعتها بـ SQL وصولاً لداشبورد Power BI بصفحة واحدة.
        </div>
        <div class="project-highlights">
            <span>💰 5.17M EGP Revenue</span>
            <span>•</span>
            <span>📈 1.75M EGP Net Profit</span>
            <span>•</span>
            <span>📦 317K Units</span>
            <span>•</span>
            <span>🏷️ 289.04K EGP Discounts</span>
            <span>•</span>
            <span>⭐ 4.21 Avg Rating</span>
        </div>
        <div>
            <span class="tool-badge">Python (Pandas)</span>
            <span class="tool-badge">SQL (Star Schema)</span>
            <span class="tool-badge">Power BI & DAX</span>
            <span class="tool-badge">2022 – 2026</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

pepsi_btn_label = (
    "🔽 إخفاء تفاصيل مشروع Pepsi Egypt Sales"
    if st.session_state.open_pepsi
    else "🔍 اضغط لعرض التفاصيل والفيديو التوضيحي والمؤشرات"
)
if st.button(pepsi_btn_label, key="btn_toggle_pepsi"):
    st.session_state.open_pepsi = not st.session_state.open_pepsi
    st.rerun()

if st.session_state.open_pepsi:
    st.markdown('<div class="project-details-box">', unsafe_allow_html=True)

    st.markdown(
        """
        <div style="color: #334155; font-size: 0.96rem; line-height: 1.75; margin-bottom: 16px;">
            <h4 style="color: #0F766E; margin-bottom: 8px;">🔎 مراحل العمل والمنهجية</h4>
            <ul>
                <li><b>تنظيف وتجهيز الداتا بـ Python (Pandas):</b> توحيد أسماء المدن وأحجام العبوات والفئات، وضبط التواريخ وحساب الأعمدة المالية (<b>Revenue, Cost, Discount, Net Profit</b>) بالجنيه المصري على بيانات تجريبية (<b>Synthetic Data</b>).</li>
                <li><b>تنظيم البيانات والاستعلام بـ SQL:</b> تقسيم الداتا بنظام <b>Star Schema</b> (جدول Fact للمبيعات وجداول Dimensions للمدن والتواريخ والمنتجات والأحجام) ومراجعة المجاميع والأرقام قبل ربطها بـ Power BI.</li>
                <li><b>الداشبورد التفاعلية بـ Power BI:</b> تصميم صفحة واحدة توضح الإيرادات (5.17M EGP)، صافي الربح (1.75M EGP)، الوحدات (317K)، الخصومات (289.04K EGP)، متوسط التقييم (4.21)، مقارنة المؤشرات عبر 5 سنوات، وتوزيع المحافظات (القاهرة، الجيزة، إسكندرية في الصدارة) مع فلاتر للسنة والشهر والفئة والمدينة وحجم العبوة وDate Slider.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_centered_video(
        "pepsi_demo.mp4",
        "ℹ️ ملف الفيديو `pepsi_demo.mp4` غير موجود حالياً في المجلد الرئيسي — ارفعه على GitHub بنفس الاسم ليظهر هنا تلقائياً.",
    )

    st.markdown("<div style='margin-top: 18px;'></div>", unsafe_allow_html=True)

    df_p_yr, df_p_gov, df_p_cat = load_pepsi_summary_data()

    st.markdown('<div class="filter-bar">', unsafe_allow_html=True)
    pf1, pf2, pf3 = st.columns(3)

    with pf1:
        p_year_list = ["All Years (2022–2026)"] + df_p_yr["Year"].tolist()
        selected_p_year = st.selectbox("Year:", p_year_list)

    with pf2:
        p_gov_list = ["All Governorates"] + df_p_gov["Governorate"].tolist()
        selected_p_gov = st.selectbox("Governorate:", p_gov_list)

    with pf3:
        p_cat_list = ["All Categories"] + df_p_cat["Category"].tolist()
        selected_p_cat = st.selectbox("Category:", p_cat_list)
    st.markdown("</div>", unsafe_allow_html=True)

    yr_ratio = 1.0
    if selected_p_year != "All Years (2022–2026)":
        row_v = df_p_yr.loc[
            df_p_yr["Year"] == selected_p_year, "Revenue_M"
        ].iloc[0]
        yr_ratio = row_v / df_p_yr["Revenue_M"].sum()

    gov_ratio = 1.0
    if selected_p_gov != "All Governorates":
        row_v = df_p_gov.loc[
            df_p_gov["Governorate"] == selected_p_gov, "Revenue_M"
        ].iloc[0]
        gov_ratio = row_v / df_p_gov["Revenue_M"].sum()

    cat_ratio = 1.0
    if selected_p_cat != "All Categories":
        row_v = df_p_cat.loc[
            df_p_cat["Category"] == selected_p_cat, "Units_K"
        ].iloc[0]
        cat_ratio = row_v / df_p_cat["Units_K"].sum()

    p_scale = yr_ratio * gov_ratio * cat_ratio
    p_rev_m = 5.17 * p_scale
    p_profit_m = 1.75 * p_scale
    p_units_k = 317.0 * p_scale
    p_disc_k = 289.04 * p_scale
    p_rating = 4.21

    pk1, pk2, pk3, pk4, pk5 = st.columns(5)
    with pk1:
        render_kpi(
            "Total Revenue",
            f"{p_rev_m:,.2f}M EGP",
            ("<span style='color:#0D9488;'>● 2022–2026</span>", True),
            "💵",
        )
    with pk2:
        render_kpi(
            "Net Profit",
            f"{p_profit_m:,.2f}M EGP",
            ("<span style='color:#0D9488;'>● Net</span>", True),
            "📈",
        )
    with pk3:
        render_kpi(
            "Total Units",
            f"{p_units_k:,.1f}K",
            ("<span style='color:#2563EB;'>● Volume</span>", True),
            "📦",
        )
    with pk4:
        render_kpi(
            "Discounts",
            f"{p_disc_k:,.1f}K EGP",
            ("<span style='color:#D97706;'>● Promo</span>", True),
            "🏷️",
        )
    with pk5:
        render_kpi(
            "Avg Rating",
            f"{p_rating:.2f} / 5",
            ("<span style='color:#0D9488;'>● CSAT</span>", True),
            "⭐",
        )

    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# PROJECT 2: Healthcare Analytics Dashboard (Brief + Toggle)
# =========================================================
st.markdown("<div style='margin-top: 22px;'></div>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="project-summary-card">
        <div class="project-card-title">🏥 Healthcare Analytics Dashboard | End-to-End Data Analysis Project</div>
        <div class="project-card-brief">
            تحويل بيانات الرعاية الصحية الخام إلى لوحة قياس تفاعلية لتحليل أداء المستشفيات والحالات الطبية ومؤشرات الإقامة والطوارئ لدعم القرارات الطبية والتشغيلية.
        </div>
        <div class="project-highlights">
            <span>👥 55,500 Patients</span>
            <span>•</span>
            <span>💰 1,211.84M Total Revenue</span>
            <span>•</span>
            <span>🛏️ 17.84 Avg Stay Days</span>
            <span>•</span>
            <span>🚑 31.60% Emergency Share</span>
        </div>
        <div>
            <span class="tool-badge">SQL</span>
            <span class="tool-badge">Python</span>
            <span class="tool-badge">Power BI</span>
            <span class="tool-badge">DAX</span>
            <span class="tool-badge">Interactive Demo Video</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

hc_btn_label = (
    "🔽 إخفاء تفاصيل مشروع Healthcare"
    if st.session_state.open_healthcare
    else "🔍 اضغط لعرض التفاصيل والفيديو التوضيحي والمؤشرات"
)
if st.button(hc_btn_label, key="btn_toggle_hc"):
    st.session_state.open_healthcare = not st.session_state.open_healthcare
    st.rerun()

if st.session_state.open_healthcare:
    st.markdown('<div class="project-details-box">', unsafe_allow_html=True)

    st.markdown(
        """
        <div style="color: #334155; font-size: 0.96rem; line-height: 1.75; margin-bottom: 16px;">
            <h4 style="color: #0F766E; margin-bottom: 8px;">🔎 ماذا يغطي التحليل؟</h4>
            <ul>
                <li>مقارنة الإيرادات وعدد الأطباء والمرضى حسب المستشفى (<b>Hospital</b>) والفئة العمرية (<b>Age_Group</b>) والنوع (<b>Gender</b>).</li>
                <li>تحليل الإيرادات حسب الحالة الطبية (<b>Medical Condition</b>) مثل Cancer وHeart Disease وAlzheimer's وغيرها.</li>
                <li>تتبع نسبة إيرادات الطوارئ حسب الدواء (<b>Medication</b>) وحركة الدخول حسب أيام الأسبوع (<b>Admission_Day_Name</b>).</li>
                <li>فلاتر تفاعلية (<b>Slicers</b>) لتصفية البيانات حسب الحالة الطبية، الفئة العمرية، السنة، الشهر، والمستشفى مع زر إعادة تعيين بضغطة واحدة.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

    render_centered_video(
        "healthcare_demo.mp4",
        "ℹ️ ملف الفيديو `healthcare_demo.mp4` غير موجود حالياً في المجلد الرئيسي — تأكد من إتمام حفظ التغييرات (Commit) على GitHub.",
    )

    st.markdown("<div style='margin-top: 18px;'></div>", unsafe_allow_html=True)

    df_hc_cond, df_hc_hosp, df_hc_age = load_healthcare_summary_data()

    st.markdown('<div class="filter-bar">', unsafe_allow_html=True)
    hf1, hf2, hf3 = st.columns(3)

    with hf1:
        hc_cond_list = ["All Conditions"] + df_hc_cond["Medical_Condition"].tolist()
        selected_hc_cond = st.selectbox("Medical Condition:", hc_cond_list)

    with hf2:
        hc_hosp_list = ["All Hospitals"] + df_hc_hosp["Hospital"].tolist()
        selected_hc_hosp = st.selectbox("Hospital:", hc_hosp_list)

    with hf3:
        hc_age_list = ["All Age Groups"] + df_hc_age["Age_Group"].tolist()
        selected_hc_age = st.selectbox("Age Group:", hc_age_list)
    st.markdown("</div>", unsafe_allow_html=True)

    cond_ratio = 1.0
    if selected_hc_cond != "All Conditions":
        row_val = df_hc_cond.loc[
            df_hc_cond["Medical_Condition"] == selected_hc_cond, "Revenue_M"
        ].iloc[0]
        cond_ratio = row_val / df_hc_cond["Revenue_M"].sum()

    hosp_ratio = 1.0
    if selected_hc_hosp != "All Hospitals":
        row_val = df_hc_hosp.loc[
            df_hc_hosp["Hospital"] == selected_hc_hosp, "Revenue_M"
        ].iloc[0]
        hosp_ratio = row_val / df_hc_hosp["Revenue_M"].sum()

    age_ratio = 1.0
    if selected_hc_age != "All Age Groups":
        row_val = df_hc_age.loc[
            df_hc_age["Age_Group"] == selected_hc_age, "Patients"
        ].iloc[0]
        age_ratio = row_val / df_hc_age["Patients"].sum()

    scale = cond_ratio * hosp_ratio * age_ratio
    hc_patients = int(round(55500 * scale))
    hc_revenue_m = 1211.84 * scale
    hc_avg_stay = 17.84
    hc_emergency_pct = 31.60
    hc_avg_billing = 21835 * (0.92 + 0.08 * scale) if scale < 1 else 21835

    hk1, hk2, hk3, hk4, hk5 = st.columns(5)
    with hk1:
        render_kpi(
            "Total Patients",
            f"{hc_patients:,}",
            ("<span style='color:#0D9488;'>● Cohort</span>", True),
            "🩺",
        )
    with hk2:
        render_kpi(
            "Avg Stay Days",
            f"{hc_avg_stay:.2f} d",
            ("<span style='color:#2563EB;'>● LOS</span>", True),
            "🛏️",
        )
    with hk3:
        render_kpi(
            "Total Revenue",
            f"{hc_revenue_m:,.2f}M",
            ("<span style='color:#0D9488;'>● Gross</span>", True),
            "💰",
        )
    with hk4:
        render_kpi(
            "Emergency Rev %",
            f"{hc_emergency_pct:.2f}%",
            ("<span style='color:#D97706;'>● ER Share</span>", True),
            "🚑",
        )
    with hk5:
        render_kpi(
            "Avg Billing",
            f"{hc_avg_billing:,.0f}",
            ("<span style='color:#0D9488;'>● / Case</span>", True),
            "🧾",
        )

    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# PROJECT 3: Olist E-Commerce Executive Dashboard (Full Original)
# =========================================================
st.markdown("<div style='margin-top: 22px;'></div>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="project-summary-card">
        <div class="project-card-title">🛒 Olist E-Commerce Executive Dashboard</div>
        <div class="project-card-brief">
            لوحة قياس تنفيذية تفاعلية لتحليل أداء المبيعات والإيرادات وتكلفة الشحن وطرق الدفع ومعدلات إتمام الطلبات عبر الولايات والفئات والفترات الزمنية.
        </div>
        <div class="project-highlights">
            <span>🛍️ 1,500+ Orders Sampled</span>
            <span>•</span>
            <span>📊 7 Executive KPIs</span>
            <span>•</span>
            <span>📈 9 Interactive Visuals</span>
            <span>•</span>
            <span>🎛️ Multi-Dimensional Filters</span>
        </div>
        <div>
            <span class="tool-badge">Python</span>
            <span class="tool-badge">SQL</span>
            <span class="tool-badge">Streamlit</span>
            <span class="tool-badge">Plotly</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

olist_btn_label = (
    "🔽 إخفاء تفاصيل مشروع Olist E-Commerce"
    if st.session_state.open_olist
    else "🔍 اضغط لعرض التفاصيل والداشبورد التفاعلي"
)
if st.button(olist_btn_label, key="btn_toggle_olist"):
    st.session_state.open_olist = not st.session_state.open_olist
    st.rerun()

if st.session_state.open_olist:
    st.markdown('<div class="project-details-box">', unsafe_allow_html=True)

    df_raw, _, df_reviews = load_full_data()

    st.markdown('<div class="filter-bar">', unsafe_allow_html=True)
    f1, f2, f3, f4 = st.columns(4)

    with f1:
        state_list = ["All States"] + sorted(
            df_raw["customer_state"].dropna().unique().tolist()
        )
        selected_state = st.selectbox("Customer State:", state_list)

    with f2:
        cat_list = ["All Categories"] + sorted(
            df_raw["category"].dropna().unique().tolist()
        )
        selected_cat = st.selectbox("Product Category:", cat_list)

    with f3:
        pay_list = ["All Payment Types"] + sorted(
            df_raw["payment_type"].dropna().unique().tolist()
        )
        selected_pay = st.selectbox("Payment Type:", pay_list)

    with f4:
        year_list = ["All Years"] + sorted(
            [y for y in df_raw["Year"].dropna().unique().tolist() if y != "nan"]
        )
        selected_year = st.selectbox("Order Year:", year_list)
    st.markdown("</div>", unsafe_allow_html=True)

    df = df_raw.copy()
    if selected_state != "All States":
        df = df[df["customer_state"] == selected_state]
    if selected_cat != "All Categories":
        df = df[df["category"] == selected_cat]
    if selected_pay != "All Payment Types":
        df = df[df["payment_type"] == selected_pay]
    if selected_year != "All Years":
        df = df[df["Year"] == selected_year]

    df_payments = (
        df.groupby("payment_type")
        .agg(cnt=("order_id", "count"), val=("total_amount", "sum"))
        .reset_index()
    )

    def get_mom_delta(monthly_series):
        s = monthly_series.sort_index()
        if len(s) >= 2 and s.iloc[-2] > 0:
            pct = ((s.iloc[-1] - s.iloc[-2]) / s.iloc[-2]) * 100
            if pct >= 0:
                return f"<span style='color:#0D9488;'>▲ +{pct:.1f}% mo</span>", True
            else:
                return f"<span style='color:#E11D48;'>▼ {pct:.1f}% mo</span>", False
        return "<span style='color:#64748B;'>— 0.0% mo</span>", True

    total_revenue = df["total_amount"].sum()
    total_product_sales = df["price"].sum()
    total_freight = df["freight_value"].sum()
    total_orders = df["order_id"].nunique()
    total_customers = df["customer_unique_id"].nunique()
    aov = total_revenue / total_orders if total_orders > 0 else 0
    freight_pct = (
        (total_freight / total_revenue * 100) if total_revenue > 0 else 0
    )
    avg_items = len(df) / total_orders if total_orders > 0 else 0

    m_rev = df.groupby("Year_Month")["total_amount"].sum()
    m_sales = df.groupby("Year_Month")["price"].sum()
    m_orders = df.groupby("Year_Month")["order_id"].nunique()
    m_aov = (m_rev / m_orders).fillna(0)
    m_cust = df.groupby("Year_Month")["customer_unique_id"].nunique()
    m_freight = df.groupby("Year_Month")["freight_value"].sum()
    m_items = (
        df.groupby("Year_Month")["order_id"].count() / m_orders
    ).fillna(0)

    st.markdown(
        f"<span style='color:#64748B; font-size:13px;'>Active Filter: State = <b style='color:#0F766E'>{selected_state}</b> | Category = <b style='color:#2563EB'>{selected_cat}</b> | Payment = <b style='color:#4F46E5'>{selected_pay}</b> | Year = <b style='color:#0F766E'>{selected_year}</b></span>",
        unsafe_allow_html=True,
    )
    st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)

    k1, k2, k3, k4, k5, k6, k7 = st.columns(7)
    with k1:
        render_kpi(
            "Total Revenue",
            f"${total_revenue / 1e3:.1f}K",
            get_mom_delta(m_rev),
            "💵",
        )
    with k2:
        render_kpi(
            "Net Sales",
            f"${total_product_sales / 1e3:.1f}K",
            get_mom_delta(m_sales),
            "📦",
        )
    with k3:
        render_kpi(
            "Total Orders", f"{total_orders:,}", get_mom_delta(m_orders), "🛍️"
        )
    with k4:
        render_kpi(
            "Avg Order (AOV)", f"${aov:,.2f}", get_mom_delta(m_aov), "📈"
        )
    with k5:
        render_kpi(
            "Customers", f"{total_customers:,}", get_mom_delta(m_cust), "👥"
        )
    with k6:
        render_kpi(
            "Total Freight",
            f"${total_freight / 1e3:.1f}K",
            get_mom_delta(m_freight),
            "🚚",
        )
    with k7:
        render_kpi(
            "Items / Order", f"{avg_items:.2f}", get_mom_delta(m_items), "⚖️"
        )

    st.markdown("<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True)

    # ROW 1
    r1_c1, r1_c2, r1_c3 = st.columns(3)

    with r1_c1:
        monthly = (
            df.groupby("Year_Month")["total_amount"]
            .sum()
            .reset_index()
            .sort_values("Year_Month")
        )
        fig1 = px.area(
            monthly,
            x="Year_Month",
            y="total_amount",
            markers=True,
            color_discrete_sequence=[TEAL_PRIMARY],
        )
        fig1.update_traces(
            line=dict(color=TEAL_PRIMARY, width=3, shape="spline"),
            fillcolor="rgba(13, 148, 136, 0.14)",
        )
        st.plotly_chart(
            style_square_fig(fig1, "1. Monthly Revenue Trend ($)"),
            use_container_width=True,
        )

    with r1_c2:
        comp_df = pd.DataFrame(
            {
                "Component": ["Product Sales", "Freight Cost"],
                "Amount": [total_product_sales, total_freight],
            }
        )
        fig2 = px.pie(
            comp_df,
            names="Component",
            values="Amount",
            hole=0.58,
            color_discrete_sequence=[TEAL_PRIMARY, BLUE_ACCENT],
        )
        fig2.update_traces(
            textinfo="percent+label",
            textfont=dict(size=13, color="#0F172A", weight="bold"),
        )
        fig2.add_annotation(
            text=f"Freight<br>{freight_pct:.1f}%",
            x=0.5,
            y=0.5,
            font_size=13,
            showarrow=False,
            font_color="#0F172A",
        )
        st.plotly_chart(
            style_square_fig(
                fig2,
                "2. Revenue vs. Freight Split",
                margin=dict(l=20, r=20, t=65, b=20),
            ),
            use_container_width=True,
        )

    with r1_c3:
        top_states = (
            df.groupby("customer_state")["total_amount"]
            .sum()
            .nlargest(7)
            .reset_index()
        )
        fig3 = px.bar(
            top_states,
            x="total_amount",
            y="customer_state",
            orientation="h",
            text="total_amount",
            color="total_amount",
            color_continuous_scale=["#99F6E4", "#0D9488", "#1E3A8A"],
        )
        fig3.update_traces(
            texttemplate="%{text:,.0f}$",
            textposition="outside",
            cliponaxis=False,
            textfont=dict(size=13, color="#0F172A", weight="bold"),
        )
        fig3.update_yaxes(categoryorder="total ascending")
        st.plotly_chart(
            style_square_fig(
                fig3,
                "3. Top 7 States by Revenue",
                margin=dict(l=20, r=85, t=55, b=20),
            ),
            use_container_width=True,
        )

    # ROW 2
    r2_c1, r2_c2, r2_c3 = st.columns(3)

    with r2_c1:
        top_cats = (
            df.groupby("category")["price"].sum().nlargest(8).reset_index()
        )
        top_cats["short_cat"] = top_cats["category"].str.slice(0, 15)
        fig4 = px.treemap(
            top_cats,
            path=["short_cat"],
            values="price",
            color="price",
            color_continuous_scale=["#CCFBF1", "#2DD4BF", "#0284C7", "#1E3A8A"],
        )
        fig4.update_traces(
            textinfo="label+value",
            texttemplate="<b>%{label}</b><br>$%{value:,.0f}",
            textfont=dict(size=13, color="#0F172A"),
        )
        st.plotly_chart(
            style_square_fig(
                fig4,
                "4. Top Categories Share (Treemap)",
                margin=dict(l=10, r=10, t=55, b=10),
            ),
            use_container_width=True,
        )

    with r2_c2:
        df_pay_sorted = df_payments[df_payments["val"] > 0].sort_values(
            "val", ascending=True
        )
        fig5 = px.bar(
            df_pay_sorted,
            x="val",
            y="payment_type",
            orientation="h",
            text="val",
            color="payment_type",
            color_discrete_sequence=LIGHT_PALETTE,
        )
        fig5.update_traces(
            texttemplate="%{text:,.0f}$",
            textposition="outside",
            cliponaxis=False,
            textfont=dict(size=13, color="#0F172A", weight="bold"),
        )
        st.plotly_chart(
            style_square_fig(
                fig5,
                "5. Payment Methods Allocation",
                margin=dict(l=20, r=85, t=55, b=20),
            ),
            use_container_width=True,
        )

    with r2_c3:
        fig6 = px.bar(
            df_reviews,
            x="review_score",
            y="cnt",
            text="cnt",
            color="review_score",
            color_continuous_scale=["#FECDD3", "#F59E0B", "#0D9488"],
        )
        fig6.update_traces(
            texttemplate="%{text:,}",
            textposition="outside",
            cliponaxis=False,
            textfont=dict(size=13, color="#0F172A", weight="bold"),
        )
        fig6.update_xaxes(title="Stars (1-5)")
        st.plotly_chart(
            style_square_fig(
                fig6,
                "6. Customer Review Scores",
                margin=dict(l=20, r=25, t=55, b=20),
            ),
            use_container_width=True,
        )

    # ROW 3
    r3_c1, r3_c2, r3_c3 = st.columns(3)

    with r3_c1:
        days_order = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        dow = (
            df.groupby("Day_of_Week")["order_id"]
            .nunique()
            .reindex(days_order)
            .reset_index()
        )
        dow["Day_Short"] = dow["Day_of_Week"].str.slice(0, 3)
        fig7 = px.bar(
            dow,
            x="Day_Short",
            y="order_id",
            text="order_id",
            color="order_id",
            color_continuous_scale=["#99F6E4", "#0284C7"],
        )
        fig7.update_traces(
            texttemplate="%{text:,}",
            textposition="outside",
            cliponaxis=False,
            textfont=dict(size=13, color="#0F172A", weight="bold"),
        )
        st.plotly_chart(
            style_square_fig(
                fig7,
                "7. Orders Volume by Day",
                margin=dict(l=20, r=25, t=55, b=20),
            ),
            use_container_width=True,
        )

    with r3_c2:
        hourly = df.groupby("Hour")["order_id"].nunique().reset_index()
        fig8 = px.area(
            hourly,
            x="Hour",
            y="order_id",
            color_discrete_sequence=[BLUE_ACCENT],
        )
        fig8.update_traces(
            line=dict(color=BLUE_ACCENT, width=3, shape="spline"),
            fillcolor="rgba(37, 99, 235, 0.14)",
        )
        fig8.update_xaxes(title="Hour (0-23)")
        st.plotly_chart(
            style_square_fig(fig8, "8. Peak Shopping Hours Flow"),
            use_container_width=True,
        )

    with r3_c3:
        status_df = (
            df.groupby("order_status")["order_id"]
            .nunique()
            .nlargest(5)
            .reset_index()
            .sort_values("order_id", ascending=False)
        )
        fig9 = go.Figure(
            go.Funnel(
                y=status_df["order_status"],
                x=status_df["order_id"],
                textinfo="value+percent initial",
                textfont=dict(size=13, color="#0F172A", weight="bold"),
                marker=dict(
                    color=[
                        TEAL_PRIMARY,
                        SKY_SOFT,
                        BLUE_ACCENT,
                        AMBER_SOFT,
                        ROSE_SOFT,
                    ]
                ),
            )
        )
        st.plotly_chart(
            style_square_fig(
                fig9,
                "9. Order Fulfillment Funnel (Top 5)",
                margin=dict(l=20, r=25, t=55, b=20),
            ),
            use_container_width=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)
