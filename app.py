import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import os

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------
st.set_page_config(
    page_title="Mohamed Gamal | Data Analyst",
    page_icon="📊",
    layout="wide"
)

# Custom Styling (Dark Mode Friendly)
st.markdown("""
    <style>
    .main-title { font-size: 2.2rem; font-weight: 700; color: #38BDF8; margin-bottom: 0.2rem; }
    .sub-title { font-size: 1.1rem; color: #94A3B8; margin-bottom: 1.5rem; }
    .section-header { font-size: 1.4rem; font-weight: 600; color: #38BDF8; border-bottom: 2px solid #0284C7; padding-bottom: 0.3rem; margin-top: 1.5rem; margin-bottom: 1rem; }
    
    .skill-card {
        background-color: #1E293B;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #38BDF8;
        margin-bottom: 1rem;
    }
    .skill-card h4 { color: #38BDF8; margin-bottom: 0.5rem; }
    .skill-card ul { padding-left: 1.2rem; margin-bottom: 0; }
    .skill-card li { color: #CBD5E1; font-size: 0.9rem; }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to:",
    ["Profile", "Healthcare Billing", "AdventureWorks Sales"]
)

# ---------------------------------------------------------
# Data Loaders
# ---------------------------------------------------------
@st.cache_data
def load_healthcare_data():
    import numpy as np
    np.random.seed(42)
    n = 300
    dates = pd.date_range(start='2025-01-01', periods=n, freq='D')
    
    df = pd.DataFrame({
        'Admission_Date': np.random.choice(dates, n),
        'Specialty': np.random.choice(['Inpatient', 'Outpatient', 'Emergency', 'Surgery', 'ICU'], n, p=[0.3, 0.3, 0.2, 0.1, 0.1]),
        'Insurance_Provider': np.random.choice(['Medicare', 'Medicaid', 'Private Insurance', 'Self-Pay'], n),
        'Billing_Amount': np.random.uniform(500, 15000, n).round(2),
        'LOS_Days': np.random.randint(1, 15, n)
    })
    df['YearMonth'] = df['Admission_Date'].dt.to_period('M').astype(str)
    return df

@st.cache_data
def load_sales_data():
    import numpy as np
    np.random.seed(101)
    n = 400
    dates = pd.date_range(start='2024-01-01', periods=n, freq='D')
    
    df = pd.DataFrame({
        'OrderDate': np.random.choice(dates, n),
        'Category': np.random.choice(['Bikes', 'Components', 'Clothing', 'Accessories'], n, p=[0.4, 0.2, 0.2, 0.2]),
        'Region': np.random.choice(['North America', 'Europe', 'Pacific'], n),
        'SalesAmount': np.random.uniform(20, 3500, n).round(2),
        'OrderQuantity': np.random.randint(1, 8, n)
    })
    df['YearMonth'] = df['OrderDate'].dt.to_period('M').astype(str)
    return df

# ---------------------------------------------------------
# Page 1: Profile
# ---------------------------------------------------------
if page == "Profile":
    col1, col2 = st.columns([1, 3])
    
    with col1:
        img_path = "profile.jpg.jpg" if os.path.exists("profile.jpg.jpg") else "profile.jpg"
        if os.path.exists(img_path):
            st.image(Image.open(img_path), use_container_width=True)
        else:
            st.info("📷 Profile Image")

    with col2:
        st.markdown('<div class="main-title">Mohamed Gamal</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-title">Healthcare & Business Data Analyst</div>', unsafe_allow_html=True)
        st.write("""
        Data Analyst at the Egyptian Ministry of Health with experience transforming clinical, financial, and operational datasets into interactive dashboards and actionable business insights.
        """)
        
        cv_path = "Mohamed_gamal_mahmoud_Ebrahim_Naukrigulf_CV_09Oct2026.pdf"
        if os.path.exists(cv_path):
            with open(cv_path, "rb") as f:
                st.download_button("📄 Download CV", f, file_name="Mohamed_Gamal_CV.pdf", mime="application/pdf")

    st.markdown('<div class="section-header">🛠️ Technical Skills</div>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown("""
        <div class="skill-card">
            <h4>Python Analytics</h4>
            <ul>
                <li>Pandas & NumPy</li>
                <li>Matplotlib & Seaborn</li>
                <li>Data Cleaning & Transformation</li>
                <li>Streamlit & Plotly</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with c2:
        st.markdown("""
        <div class="skill-card">
            <h4>SQL & Databases</h4>
            <ul>
                <li>Complex Queries & Aggregations</li>
                <li>Window Functions & Joins</li>
                <li>SQL Server (SSMS)</li>
                <li>Data Modeling</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="skill-card">
            <h4>Business Intelligence</h4>
            <ul>
                <li>Interactive Dashboards</li>
                <li>Power BI Reports</li>
                <li>EHR / EMR Data Systems</li>
                <li>KPI Tracking</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">💼 Work Experience</div>', unsafe_allow_html=True)
    st.write("""
    **Statistical & Data Technician — Ministry of Health & Population (2023 - Present)**
    - Clean and validate EMR data across hospital departments.
    - Analyze length of stay (LOS), bed occupancy rates, and monthly throughput.
    - Generate statistical reports for healthcare managers to improve operational efficiency.
    """)

# ---------------------------------------------------------
# Page 2: Healthcare Dashboard
# ---------------------------------------------------------
elif page == "Healthcare Billing":
    st.markdown('<div class="main-title">🏥 Healthcare Billing Dashboard</div>', unsafe_allow_html=True)
    
    df = load_healthcare_data()
    
    # Filters
    st.sidebar.subheader("Filters")
    spec = st.sidebar.multiselect("Specialty:", df['Specialty'].unique(), default=df['Specialty'].unique())
    ins = st.sidebar.multiselect("Insurance:", df['Insurance_Provider'].unique(), default=df['Insurance_Provider'].unique())
    
    filtered_df = df[(df['Specialty'].isin(spec)) & (df['Insurance_Provider'].isin(ins))]
    
    # KPIs
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Total Patients", f"{len(filtered_df):,}")
    k2.metric("Total Billing", f"${filtered_df['Billing_Amount'].sum():,.2f}")
    k3.metric("Avg Length of Stay", f"{filtered_df['LOS_Days'].mean():.1f} days")
    k4.metric("Avg Billing", f"${filtered_df['Billing_Amount'].mean():,.2f}")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        fig1 = px.pie(filtered_df, names='Specialty', values='Billing_Amount', title="Billing by Specialty", hole=0.4, template="plotly_dark")
        st.plotly_chart(fig1, use_container_width=True)
        
    with col2:
        df_ins = filtered_df.groupby('Insurance_Provider')['Billing_Amount'].sum().reset_index()
        fig2 = px.bar(df_ins, x='Insurance_Provider', y='Billing_Amount', color='Insurance_Provider', title="Billing by Insurance Provider", template="plotly_dark")
        st.plotly_chart(fig2, use_container_width=True)

# ---------------------------------------------------------
# Page 3: Sales Dashboard
# ---------------------------------------------------------
elif page == "AdventureWorks Sales":
    st.markdown('<div class="main-title">🛒 AdventureWorks Sales Dashboard</div>', unsafe_allow_html=True)
    
    df = load_sales_data()
    
    # Filters
    st.sidebar.subheader("Filters")
    cat = st.sidebar.multiselect("Category:", df['Category'].unique(), default=df['Category'].unique())
    reg = st.sidebar.multiselect("Region:", df['Region'].unique(), default=df['Region'].unique())
    
    filtered_df = df[(df['Category'].isin(cat)) & (df['Region'].isin(reg))]
    
    # KPIs
    s1, s2, s3
