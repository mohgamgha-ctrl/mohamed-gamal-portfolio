import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
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
# Custom Styling (CSS) - Dark/Light Mode Compatible
# ---------------------------------------------------------
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        padding-top: 1.5rem;
    }
    [data-testid="stSidebar"] label {
        font-size: 1.35rem !important;
        font-weight: 700 !important;
        margin-bottom: 10px !important;
    }
    .sidebar-title {
        font-size: 1.8rem !important;
        font-weight: 800 !important;
        color: #38BDF8 !important;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid #334155;
        padding-bottom: 10px;
    }
    .main-title {
        font-size: 2.6rem;
        font-weight: 800;
        color: #38BDF8 !important;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #94A3B8 !important;
        margin-bottom: 20px;
    }
    .section-header {
        font-size: 1.7rem;
        font-weight: 700;
        color: #38BDF8 !important;
        border-bottom: 2px solid #0284C7;
        padding-bottom: 8px;
        margin-top: 25px;
        margin-bottom: 20px;
    }
    /* Kpis & Skill Cards Styling */
    .skill-card {
        background-color: #1E293B !important;
        color: #F8FAFC !important;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #38BDF8;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
        margin-bottom: 15px;
    }
    .skill-card h4 {
        color: #38BDF8 !important;
        margin-bottom: 10px;
    }
    .skill-card ul {
        margin-bottom: 0;
        padding-left: 20px;
    }
    .skill-card ul li {
        color: #CBD5E1 !important;
        font-size: 0.95rem;
        margin-bottom: 5px;
    }
    .metric-card {
        background-color: #1E293B !important;
        color: #38BDF8 !important;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #334155;
    }
    .metric-card-health {
        background-color: #064E3B !important;
        color: #34D399 !important;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #065F46;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Navigation & Filters
# ---------------------------------------------------------
st.sidebar.markdown('<div class="sidebar-title">📌 التنقل والإعدادات</div>', unsafe_allow_html=True)

page = st.sidebar.radio(
    "الانتقال إلى القسم / Select Page:",
    ["👤 الملف الشخصي (Profile)", "🏥 Healthcare Billing Analytics", "🛒 AdventureWorks Sales Analytics"]
)

st.sidebar.markdown("---")

# ---------------------------------------------------------
# Sample Data Generators (for Dashboards)
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
if page == "👤 الملف الشخصي (Profile)":
    col_img, col_info = st.columns([1, 2.5])
    
    with col_img:
        # فحص جلب الصورة بأحد الاسمين
        img_path = "profile.jpg.jpg" if os.path.exists("profile.jpg.jpg") else "profile.jpg"
        if os.path.exists(img_path):
            img = Image.open(img_path)
            st.image(img, use_container_width=True)
        else:
            st.info("📷 [Profile Image Placeholder]")

    with col_info:
        st.markdown('<div class="main-title">محمد جمال | Mohamed Gamal</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-title">أخصائي تحليل البيانات ورعاية صحية | Healthcare & Business Data Analyst</div>', unsafe_allow_html=True)
        st.write("""
        أخصائي إحصاء وتسجيل طبي بوزارة الصحة المصرية، أمتلك خبرة عمل تحليلي وتطبيقية في تحويل البيانات المعقدة (السريرية، والمالية، والمبيعات) إلى رؤى استراتيجية تفاعلية تدعم اتخاذ القرارات وإدارة مؤشرات الأداء (KPIs).
        """)
        
        # CV Download Button
        cv_filename = "Mohamed_gamal_mahmoud_Ebrahim_Naukrigulf_CV_09Oct2026.pdf"
        if os.path.exists(cv_filename):
            with open(cv_filename, "rb") as pdf_file:
                st.download_button(
                    label="📄 تحميل السيرة الذاتية (Download CV)",
                    data=pdf_file,
                    file_name="Mohamed_Gamal_CV.pdf",
                    mime="application/pdf"
                )

    st.markdown('<div class="section-header">🛠️ المهارات والتقنيات (Skills & Technologies)</div>', unsafe_allow_html=True)
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
            <h4>📊 Business & Healthcare BI</h4>
            <ul>
                <li>Interactive Dashboards</li>
                <li>Power BI Reports</li>
                <li>EHR / EMR Data Systems</li>
                <li>KPIs & Trend Analysis</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">💼 الخبرة المهنية (Professional Experience)</div>', unsafe_allow_html=True)
    st.write("""
    * **فني إحصاء وتسجيل طبي - وزارة الصحة والسكان المصرية (2023 - الحالي):**
      * تحسين جودة البيانات الطبية والإحصائية وإعداد التظلمات والتقارير الشهرية للمستشفيات.
      * تحليل معدلات الإشغال ومتوسط فترات الإقامة بالمستشفى لتطوير الكفاءة التشغيلية.
    """)

# ---------------------------------------------------------
# PAGE 2: Healthcare Billing Analytics
# ---------------------------------------------------------
elif page == "🏥 Healthcare Billing Analytics":
    st.markdown('<div class="main-title">🏥 Healthcare Billing & Patient Dashboard</div>', unsafe_allow_html=True)
    st.write("لوحة تحكم تفاعلية لتحليل بيانات الفواتير الطبية، توزيع التخصصات، وإشعارات التأمين.")
    
    df_health = get_healthcare_data()
    
    # Sidebar Filters
    st.sidebar.markdown("### 🔍 الفلاتر (Healthcare Filters)")
    selected_spec = st.sidebar.multiselect("التخصص الطبي (Specialty):", df_health['Specialty'].unique(), default=df_health['Specialty'].unique())
    selected_ins = st.sidebar.multiselect("شركة التأمين (Insurance):", df_health['Insurance_Provider'].unique(), default=df_health['Insurance_Provider'].unique())
    
    filtered_health = df_health[(df_health['Specialty'].isin(selected_spec)) & (df_health['Insurance_Provider'].isin(selected_ins))]
    
    # KPIs
    kpi1, kpi2, kpi3, kpi4 = st.columns(4)
    kpi1.metric("إجمالي المرضى (Patients)", f"{len(filtered_health):,}")
    kpi2.metric("إجمالي المطالبات (Billing)", f"${filtered_health['Billing_Amount'].sum():,.2f}")
    kpi3.metric("متوسط الإقامة (Avg LOS)", f"{filtered_health['LOS_Days'].mean():.1f} أيام")
    kpi4.metric("متوسط الفاتورة (Avg Bill)", f"${filtered_health['Billing_Amount'].mean():,.2f}")
    
    st.markdown("---")
    
    col_h1, col_h2 = st.columns(2)
    with col_h1:
        fig_spec = px.pie(filtered_health, names='Specialty', values='Billing_Amount', title="توزيع الفواتير حسب التخصص الطبي", hole=0.4, template="plotly_dark")
        st.plotly_chart(fig_spec, use_container_width=True)
        
    with col_h2:
        fig_ins = px.bar(filtered_health.groupby('Insurance_Provider')['Billing_Amount'].sum().reset_index(), 
                         x='Insurance_Provider', y='Billing_Amount', color='Insurance_Provider',
                         title="إجمالي المطالبات حسب جهة التأمين", template="plotly_dark")
        st.plotly_chart(fig_ins, use_container_width=True)

# ---------------------------------------------------------
# PAGE 3: AdventureWorks Sales Analytics
# ---------------------------------------------------------
elif page == "🛒 AdventureWorks Sales Analytics":
    st.markdown('<div class="main-title">🛒 AdventureWorks Sales Dashboard</div>', unsafe_allow_html=True)
    st.write("لوحة تحكم المبيعات لتحليل الأداء التجاري، اتجاهات الإيرادات، وتوزيع الأقاليم.")
    
    df_sales = get_sales_data()
    
    # Sidebar Filters
    st.sidebar.markdown("### 🔍 الفلاتر (Sales Filters)")
    selected_cat = st.sidebar.multiselect("فئة المنتج (Category):", df_sales['Category'].unique(), default=df_sales['Category'].unique())
    selected_reg = st.sidebar.multiselect("الإقليم (Region):", df_sales['Region'].unique(), default=df_sales['Region'].unique())
    
    filtered_sales = df_sales[(df_sales['Category'].isin(selected_cat)) & (df_sales['Region'].isin(selected_reg))]
    
    # KPIs
    s1, s2, s3 = st.columns(3)
    s1.metric("إجمالي الإيرادات (Total Revenue)", f"${filtered_sales['SalesAmount'].sum():,.2f}")
    s2.metric("عدد الطلبات (Total Orders)", f"{len(filtered_sales):,}")
    s3.metric("متوسط قيمة الطلب (Avg Order Value)", f"${filtered_sales['SalesAmount'].mean():,.2f}")
    
    st.markdown("---")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        monthly_sales = filtered_sales.groupby('YearMonth')['SalesAmount'].sum().reset_index().sort_values('YearMonth')
        fig_trend = px.line(monthly_sales, x='YearMonth', y='SalesAmount', title="اتجاه المبيعات الشهري", markers=True, template="plotly_dark")
        st.plotly_chart(fig_trend, use_container_width=True)
        
    with col_s2:
        fig_reg = px.bar(filtered_sales.groupby('Region')['SalesAmount'].sum().reset_index(), 
                         x='Region', y='SalesAmount', color='Region', title="المبيعات حسب الإقليم الجغرافي", template="plotly_dark")
        st.plotly_chart(fig_reg, use_container_width=True)
