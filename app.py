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
# 2. Custom CSS (Finovate Theme & Clean Spacing)
# ---------------------------------------------------------
st.markdown(
    """
<style>
    .stApp, .main {
        background-color: #060B19 !important;
    }

    /* Hide Sidebar Completely */
    [data-testid="stSidebar"],
    [data-testid="collapsedControl"] {
        display: none !important;
    }

    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 1.5rem !important;
        padding-left: 1.5rem !important;
        padding-right: 1.5rem !important;
        max-width: 100% !important;
    }

    /* Hero Section Container with Neon Glow & Zero Top Gap */
    .hero-container {
        background: linear-gradient(145deg, #0D182E 0%, #0A1324 100%);
        border: 1px solid #1E355E;
        border-radius: 20px;
        padding: 30px 40px;
        box-shadow: 0 0 35px rgba(56, 189, 248, 0.2), inset 0 1px 1px rgba(255, 255, 255, 0.1);
        margin-top: 0px !important;
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

    /* Stats Bar */
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

    /* Project Showcase Banner */
    .project-banner {
        background: linear-gradient(145deg, #0D182E 0%, #0A1324 100%);
        border: 1px solid #1E355E;
        border-radius: 16px;
        padding: 20px 26px;
        margin-top: 15px;
        margin-bottom: 18px;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.16);
    }

    /* Filter Bar */
    .filter-bar {
        background: rgba(13, 24, 46, 0.75);
        border: 1px solid #1E355E;
        border-radius: 14px;
        padding: 14px 18px 6px 18px;
        margin-bottom: 14px;
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

    /* Profile Image Style */
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

    /* KPI Cards */
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
# 3. Data Provider
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
# SECTION 2: Featured Projects (Scrollable Flow)
# ---------------------------------------------------------
st.markdown(
    '<div class="section-header">🚀 Featured Projects</div>',
    unsafe_allow_html=True,
)

df_raw, _, df_reviews = load_full_data()

st.markdown(
    """
    <div class="project-banner">
        <div class="hero-title" style="font-size: 2.1rem !important; margin-bottom: 6px;">🛒 Olist E-Commerce Executive Dashboard</div>
        <div style="color: #94A3B8; font-size: 0.98rem;">
            End-to-end interactive sales, revenue, freight, payment, and fulfillment performance analysis across states, product categories, and time periods.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Horizontal Filters Bar
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

# Filter application
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
            return f"<span style='color:#00E5B0;'>▲ +{pct:.1f}% mo</span>", True
        else:
            return f"<span style='color:#F43F5E;'>▼ {pct:.1f}% mo</span>", False
    return "<span style='color:#8A99B5;'>— 0.0% mo</span>", True


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
    f"<span style='color:#8A99B5; font-size:13px;'>Active Filter: State = <b style='color:#00E5B0'>{selected_state}</b> | Category = <b style='color:#38BDF8'>{selected_cat}</b> | Payment = <b style='color:#A855F7'>{selected_pay}</b> | Year = <b style='color:#00E5B0'>{selected_year}</b></span>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True
)


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


# Row 0: 7 KPI Cards
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

st.markdown(
    "<div style='margin-bottom: 10px;'></div>", unsafe_allow_html=True
)


def style_square_fig(fig, title, margin=dict(l=20, r=30, t=55, b=20)):
    fig.update_layout(
        autosize=True,
        title=dict(
            text=title,
            font=dict(size=17, color="#FFFFFF", family="sans-serif"),
            x=0.03,
            y=0.92,
        ),
        template="plotly_dark",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        height=215,
        margin=margin,
        font=dict(size=14, color="#E2E8F0"),
        showlegend=False,
        coloraxis_showscale=False,
        hoverlabel=dict(
            bgcolor="#0A1324",
            bordercolor="#38BDF8",
            font=dict(size=16, color="#FFFFFF", family="sans-serif"),
        ),
    )
    fig.update_xaxes(
        showgrid=False,
        linecolor="#1E355E",
        tickfont=dict(size=13, color="#CBD5E1"),
    )
    fig.update_yaxes(
        gridcolor="#162645",
        zerolinecolor="#162645",
        tickfont=dict(size=13, color="#CBD5E1"),
    )
    return fig


# ROW 1: Monthly Trend | Revenue Split | Top States
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
        color_discrete_sequence=[MINT_GREEN],
    )
    fig1.update_traces(
        line=dict(color=MINT_GREEN, width=3, shape="spline"),
        fillcolor="rgba(0, 229, 176, 0.18)",
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
        color_discrete_sequence=[MINT_GREEN, VIOLET_PURPLE],
    )
    fig2.update_traces(
        textinfo="percent+label",
        textfont=dict(size=15, color="#FFFFFF", weight="bold"),
    )
    fig2.add_annotation(
        text=f"Freight<br>{freight_pct:.1f}%",
        x=0.5,
        y=0.5,
        font_size=14,
        showarrow=False,
        font_color="#FFFFFF",
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
        color_continuous_scale=[VIOLET_PURPLE, CYAN_BLUE, MINT_GREEN],
    )
    fig3.update_traces(
        texttemplate="%{text:,.0f}$",
        textposition="outside",
        cliponaxis=False,
        textfont=dict(size=14, color="#FFFFFF", weight="bold"),
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

# ROW 2: Top Categories | Payment Methods | Reviews
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
        color_continuous_scale=[
            VIOLET_PURPLE,
            ROYAL_BLUE,
            CYAN_BLUE,
            MINT_GREEN,
        ],
    )
    fig4.update_traces(
        textinfo="label+value",
        texttemplate="<b>%{label}</b><br>$%{value:,.0f}",
        textfont=dict(size=14, color="#FFFFFF"),
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
        color_discrete_sequence=FINOVATE_PALETTE,
    )
    fig5.update_traces(
        texttemplate="%{text:,.0f}$",
        textposition="outside",
        cliponaxis=False,
        textfont=dict(size=14, color="#FFFFFF", weight="bold"),
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
        color_continuous_scale=[CORAL_RED, VIOLET_PURPLE, MINT_GREEN],
    )
    fig6.update_traces(
        texttemplate="%{text:,}",
        textposition="outside",
        cliponaxis=False,
        textfont=dict(size=14, color="#FFFFFF", weight="bold"),
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

# ROW 3: Orders by Day | Peak Hours | Fulfillment Funnel
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
