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
    server = r"DESKTOP-P4GO8F9\SQLEXPRESS"
    database = "Olist_Ecommerce_DB"
    driver = "ODBC Driver 17 for SQL Server"
    
    conn_str = f"mssql+pyodbc://@{server}/{database}?driver={driver}&trusted_connection=yes"
    engine = create_engine(conn_str)

    cols_orders = pd.read_sql(
        "SELECT TOP 1 * FROM stg_orders", engine
    ).columns.tolist()

    date_col = (
        "o.order_purchase_timestamp"
        if "order_purchase_timestamp" in cols_orders
        else "GETDATE()"
    )
    status_col = (
        "o.order_status" if "order_status" in cols_orders else "'delivered'"
    )

    query = f"""
    SELECT 
        f.order_id,
        f.order_item_id,
        f.price,
        f.freight_value,
        (f.price + f.freight_value) AS total_amount,
        c.customer_unique_id,
        c.customer_state,
        c.customer_city,
        ISNULL(p.product_category_name, 'Uncategorized') AS category,
        s.seller_state,
        CAST({date_col} AS DATETIME) AS order_date,
        {status_col} AS order_status,
        ISNULL(pay.payment_type, 'unknown') AS payment_type
    FROM Fact_Order_Items f
    LEFT JOIN Dim_Customers c ON f.customer_id = c.customer_id
    LEFT JOIN Dim_Products p ON f.product_id = p.product_id
    LEFT JOIN Dim_Sellers s ON f.seller_id = s.seller_id
    LEFT JOIN stg_orders o ON f.order_id = o.order_id
    LEFT JOIN (
        SELECT order_id, payment_type, 
               ROW_NUMBER() OVER(PARTITION BY order_id ORDER BY payment_value DESC) as rn
        FROM stg_order_payments
    ) pay ON f.order_id = pay.order_id AND pay.rn = 1
    """
    df = pd.read_sql(query, engine)
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["Year_Month"] = df["order_date"].dt.to_period("M").astype(str)
    df["Year"] = df["order_date"].dt.year.astype(str)
    df["Day_of_Week"] = df["order_date"].dt.day_name()
    df["Hour"] = df["order_date"].dt.hour

    df_pay = pd.read_sql(
        "SELECT payment_type, COUNT(*) AS cnt, SUM(CAST(payment_value AS FLOAT)) AS val FROM stg_order_payments GROUP BY payment_type",
        engine,
    )
    df_rev = pd.read_sql(
        "SELECT review_score, COUNT(*) AS cnt FROM stg_order_reviews GROUP BY review_score ORDER BY review_score",
        engine,
    )

    return df, df_pay, df_rev


# ---------------------------------------------------------
# PAGE 1: Profile
# ---------------------------------------------------------
if page == "Profile":
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

    # Stats Bar Section
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
# PAGE 2: Olist E-Commerce Analytics (Dashboard)
# ---------------------------------------------------------
elif page == "Olist E-Commerce Analytics":
    df_raw, df_payments, df_reviews = load_full_data()

    # Sidebar Filters specific for Olist Dashboard
    st.sidebar.markdown("### 🔍 Dashboard Filters")

    state_list = ["All States"] + sorted(
        df_raw["customer_state"].dropna().unique().tolist()
    )
    selected_state = st.sidebar.selectbox("Customer State:", state_list)

    cat_list = ["All Categories"] + sorted(
        df_raw["category"].dropna().unique().tolist()
    )
    selected_cat = st.sidebar.selectbox("Product Category:", cat_list)

    pay_list = ["All Payment Types"] + sorted(
        df_raw["payment_type"].dropna().unique().tolist()
    )
    selected_pay = st.sidebar.selectbox("Payment Type:", pay_list)

    year_list = ["All Years"] + sorted(
        [y for y in df_raw["Year"].dropna().unique().tolist() if y != "nan"]
    )
    selected_year = st.sidebar.selectbox("Order Year:", year_list)

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

    # Calculate MoM Deltas
    def get_mom_delta(monthly_series):
        s = monthly_series.sort_index()
        if len(s) >= 3 and s.iloc[-1] < (s.iloc[-2] * 0.2):
            s = s.iloc[:-1]
        if len(s) >= 2 and s.iloc[-2] > 0:
            pct = ((s.iloc[-1] - s.iloc[-2]) / s.iloc[-2]) * 100
            if pct >= 0:
                return (
                    f"<span style='color:#00E5B0;'>▲ +{pct:.1f}% mo</span>",
                    True,
                )
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

    # Header
    st.markdown(
        '<div class="hero-title" style="font-size: 2.2rem !important;">🛒 Olist E-Commerce Executive Dashboard</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<span style='color:#8A99B5; font-size:13px;'>Active Filter: State = <b style='color:#00E5B0'>{selected_state}</b> | Category = <b style='color:#38BDF8'>{selected_cat}</b> | Payment = <b style='color:#A855F7'>{selected_pay}</b> | Year = <b style='color:#00E5B0'>{selected_year}</b></span>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div style='margin-bottom: 8px;'></div>", unsafe_allow_html=True
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

    # Row 0: ALL 7 Custom KPI Cards Side-by-Side
    c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
    with c1:
        render_kpi(
            "Total Revenue",
            f"${total_revenue / 1e6:.2f}M",
            get_mom_delta(m_rev),
            "💵",
        )
    with c2:
        render_kpi(
            "Net Sales",
            f"${total_product_sales / 1e6:.2f}M",
            get_mom_delta(m_sales),
            "📦",
        )
    with c3:
        render_kpi(
            "Total Orders", f"{total_orders:,}", get_mom_delta(m_orders), "🛍️"
        )
    with c4:
        render_kpi(
            "Avg Order (AOV)", f"${aov:,.2f}", get_mom_delta(m_aov), "📈"
        )
    with c5:
        render_kpi(
            "Customers", f"{total_customers:,}", get_mom_delta(m_cust), "👥"
        )
    with c6:
        render_kpi(
            "Total Freight",
            f"${total_freight / 1e6:.2f}M",
            get_mom_delta(m_freight),
            "🚚",
        )
    with c7:
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
            style_square_
