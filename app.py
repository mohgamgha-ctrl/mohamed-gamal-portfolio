import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import os

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Mohamed Gamal | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Custom Styling (CSS) - Dark & Light Mode Compatible
# ---------------------------------------------------------
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        padding-top: 1.5rem;
    }
    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #38BDF8 !important;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #94A3B8 !important;
        margin-bottom: 20px;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: #38BDF8 !important;
        border-bottom: 2px solid #0284C7;
        padding-bottom: 8px;
        margin-top: 25px;
        margin-bottom: 15px;
    }
    .skill-card {
        background-color: #1E293B !important;
        color: #F8FAFC !important;
        padding: 18px;
        border-radius: 10px;
        border-left: 4px solid #38BDF8;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
        margin-bottom: 15px;
    }
    .skill-card h4 {
        color: #38BDF8 !important;
        margin-bottom: 10px;
    }
    .skill-card ul {
        margin-bottom: 0;
        padding-left: 18px;
    }
    .skill-card ul li {
        color: #CBD5E1 !important;
        font-size: 0.95rem;
        margin-bottom: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Select Section:",
    ["Profile", "Healthcare Billing Analytics", "AdventureWorks Sales Analytics"]
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
    specialties = ['Inpatient', 'Outpatient', 'Emergency', 'Surgery', 'ICU']
    insurance_providers = ['Medicare', 'Medicaid', 'Private Insurance', 'Self-Pay']
    
    dates = pd.date_range(start='2025-01-01', periods=n, freq='D')
    data = {
        'Admission_Date': np.random.choice(dates, n),
        'Specialty': np.random.choice(specialties, n, p=[0.3, 0.3, 0.2, 0.1, 0.1]),
        'Insurance_Provider': np.random.choice(insurance_providers, n),
        'Billing_Amount': np.random.uniform(500, 15000, n).round(2),
        'LOS_Days': np.random.randint(1, 15, n)
    }
    df = pd.DataFrame(data)
    df['YearMonth'] = df['Admission_Date'].dt.to_period('M').astype(str)
    return df

@st.cache_data
def get_sales_data():
    import numpy as np
    np.random.seed(101)
    n = 400
    categories = ['Bikes', 'Components', 'Clothing', 'Accessories']
    regions = ['North America', 'Europe', 'Pacific']
    
    dates = pd.date_range(start='2024-01-01', periods=n, freq='D')
    data = {
        'OrderDate': np.random.choice(dates, n),
        'Category': np.random.choice(categories, n, p=[0.4, 0.2, 0.2, 0.2]),
        'Region': np.random.choice(regions, n),
        'SalesAmount': np.random.uniform(20, 3500, n).round(2),
        'OrderQuantity': np.random.randint(1, 8, n)
    }
    df = pd.DataFrame(data)
    df['YearMonth'] = df['OrderDate'].dt.to_period('M').astype(str)
    return df

# ---------------------------------------------------------
# PAGE 1: Profile
# ---------------------------------------------------------
if page == "Profile":
    col_img, col_info = st.columns([1, 2.5])
    
    with col_img:
        img_path = "profile.jpg.jpg" if os.path.exists("profile.jpg.jpg") else "profile.jpg"
        if os.path.exists(img_path):
            img = Image.open(img_path)
            st.image(img, use_container_width=True)
        else:
            st.info("📷 Profile Image")

    with col_info:
        st.markdown('<div class="main-title">Mohamed Gamal</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-title">Healthcare & Business Data Analyst</div>', unsafe_allow_html=True)
        st.write("""
        Data Analyst at the Egyptian Ministry of Health with hands-on experience in converting complex medical, clinical, billing, and sales data into strategic interactive dashboards to drive data-informed decision-making and track core KPIs.
        """)
        
        cv_filename = "Mohamed_gamal_mahmoud_Ebrahim_Naukrigulf_CV_09Oct2026.pdf"
        if os.path.exists(cv_filename):
            with open(cv_filename, "rb") as pdf_file:
                st.download_button(
                    label="📄 Download CV",
                    data=pdf_file,
                    file_name="Mohamed_Gamal_CV.pdf",
                    mime="application/pdf"
                )

    st.markdown('<div class="section-header">🛠️ Technical Skills</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="skill-card">
            <h4>🐍 Python Analytics</h4>
            <ul>
                <li>Pandas & NumPy</li>
                <li>Matplotlib & Seaborn</li>
                <li>Data Cleaning & Transformation</li>
                <li>Streamlit & Plotly Web Apps</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="skill-card">
            <h4>🗄️ SQL & Databases</h4>
            <ul>
                <li>SQL Queries & Aggregations</li>
                <li>Window Functions & Joins</li>
                <li>Relational DBs (SSMS)</li>
                <li>Data Modeling</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="skill-card">
            <h4>📊 Business Intelligence</h4>
            <ul>
                <li>Interactive Dashboards</li>
                <li>Power BI Reports</li>
                <li>EHR / EMR Data Systems</li>
                <li>KPIs & Trend Analysis</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">💼 Professional Experience</div>', unsafe_allow_html=True)
    st.write("""
    * **Statistical & Medical Records Technician — Ministry of Health & Population (2023 - Present):**
      * Clean and validate EMR data across hospital departments.
      * Analyze bed occupancy rates, average length of stay (LOS), and patient throughput.
      * Prepare monthly statistical reports for hospital management to optimize operational efficiency.
    """)

# ---------------------------------------------------------
# PAGE 2: Healthcare Billing Analytics
# ---------------------------------------------------------
elif page == "Healthcare Billing Analytics":
    st.markdown('<div class="main-title">🏥 Healthcare Billing Dashboard</div>', unsafe_allow_html=True)
    st.write("Interactive analytics for medical billing, specialty distribution, and insurance claims.")
    
    df_health = get_healthcare_data()
    
    st.sidebar.markdown("### 🔍 Filters")
    selected_spec = st.sidebar.multiselect("Specialty:", df_health['Specialty'].unique(), default=df_health['Specialty'].unique())
    selected_ins = st.sidebar.multiselect("Insurance Provider:", df_health['Insurance_Provider'].unique(), default=df_health['Insurance_Provider'].unique())
    
    filtered_health = df_health[(df_health['Specialty'].isin(selected_spec)) & (df_health['Insurance_Provider'].isin(selected_ins))]
    
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("Total Patients", f"{len(filtered_health):,}")
    kpi2.metric("Total Billing Amount", f"${filtered_health['Billing_Amount'].sum():,.2f}")
    kpi3.metric("Avg Length of Stay", f"{filtered_health['LOS_Days'].mean():.1f} Days")
    kpi4.metric("Avg Bill Amount", f"${filtered_health['Billing_Amount'].mean():,.2f}")
    
    st.markdown("---")
    
    col_h1, col_h2 = st.columns(2)
    with col_h1:
        fig_spec = px.pie(filtered_health, names='Specialty', values='Billing_Amount', title="Billing Breakdown by Specialty", hole=0.4, template="plotly_dark")
        st.plotly_chart(fig_spec, use_container_width=True)
        
    with col_h2:
        df_ins = filtered_health.groupby('Insurance_Provider')['Billing_Amount'].sum().reset_index()
        fig_ins = px.bar(df_ins, x='Insurance_Provider', y='Billing_Amount', color='Insurance_Provider', title="Claims by Insurance Provider", template="plotly_dark")
        st.plotly_chart(fig_ins, use_container_width=True)

# ---------------------------------------------------------
# PAGE 3: AdventureWorks Sales Analytics
# ---------------------------------------------------------
elif page == "AdventureWorks Sales Analytics":
    st.markdown('<div class="main-title">🛒 AdventureWorks Sales Dashboard</div>', unsafe_allow_html=True)
    st.write("Sales analytics dashboard for evaluating commercial performance, revenue trends, and regional distributions.")
    
    df_sales = get_sales_data()
    
    st.sidebar.markdown("### 🔍 Filters")
    selected_cat = st.sidebar.multiselect("Product Category:", df_sales['Category'].unique(), default=df_sales['Category'].unique())
    selected_reg = st.sidebar.multiselect("Region:", df_sales['Region'].unique(), default=df_sales['Region'].unique())
    
    filtered_sales = df_sales[(df_sales['Category'].isin(selected_cat)) & (df_sales['Region'].isin(selected_reg))]
    
    s1, s2, s3 = st.columns(3)
    s1.metric("Total Revenue", f"${filtered_sales['SalesAmount'].sum():,.2f}")
    s2.metric("Total Orders", f"{len(filtered_sales):,}")
    s3.metric("Avg Order Value", f"${filtered_sales['SalesAmount'].mean():,.2f}")
    
    st.markdown("---")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        monthly_sales = filtered_sales.groupby('YearMonth')['SalesAmount'].sum().reset_index().sort_values('YearMonth')
        fig_trend = px.line(monthly_sales, x='YearMonth', y='SalesAmount', title="Monthly Sales Trend", markers=True, template="plotly_dark")
        st.plotly_chart(fig_trend, use_container_width=True)
        
    with col_s2:
        df_reg = filtered_sales.groupby('Region')['SalesAmount'].sum().reset_index()
        fig_reg = px.bar(df_reg, x='Region', y='SalesAmount', color='Region', title="Revenue by Geographic Region", template="plotly_dark")
        st.plotly_chart(fig_reg, use_container_width=True)
