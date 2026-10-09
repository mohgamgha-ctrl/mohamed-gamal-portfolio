import streamlit as st
import plotly.express as px
import pandas as pd
import os
from PIL import Image

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="محمد جمال | Mohamed Gamal Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Custom Styling (CSS)
# ---------------------------------------------------------
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        padding-top: 1.5rem;
    }
    [data-testid="stSidebar"] label {
        font-size: 1.35rem !important;
        font-weight: 700 !important;
        color: #0D47A1 !important;
        margin-bottom: 10px !important;
    }
    .sidebar-title {
        font-size: 1.8rem !important;
        font-weight: 800 !important;
        color: #1565C0;
        margin-bottom: 1.5rem;
        border-bottom: 2px solid #E0E0E0;
        padding-bottom: 10px;
    }
    .main-title {
        font-size: 2.6rem;
        font-weight: 800;
        color: #0D47A1;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #1976D2;
        margin-bottom: 20px;
    }
    .section-header {
        font-size: 1.7rem;
        font-weight: 700;
        color: #0D47A1;
        border-bottom: 2px solid #BBDEFB;
        padding-bottom: 8px;
        margin-top: 25px;
        margin-bottom: 20px;
    }
    .skill-card {
        background-color: #F5F9FF;
        padding: 20px;
        border-radius: 12px;
        border-left: 5px solid #1976D2;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
    }
    .metric-card {
        background-color: #E3F2FD;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #90CAF9;
    }
    .metric-card-health {
        background-color: #E8F5E9;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        border: 1px solid #A5D6A7;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
st.sidebar.markdown('<p class="sidebar-title">📌 NAVIGATION</p>', unsafe_allow_html=True)
page = st.sidebar.radio("", ["🏠  عنّي (About Me)", "🚀  المشاريع (Projects)", "📬  التواصل (Contact)"])

# ---------------------------------------------------------
# PAGE 1: ABOUT ME
# ---------------------------------------------------------
if page == "🏠  عنّي (About Me)":
    col1, col2 = st.columns([2.5, 1.2])
    
    with col1:
        st.markdown('<p class="main-title">أهلاً بك 👋 | Mohamed Gamal</p>', unsafe_allow_html=True)
        st.markdown('<p class="sub-title">أخصائي بيانات ومعلوماتية طبية | Data Analyst & Healthcare Specialist</p>', unsafe_allow_html=True)
        
        st.write("""
        أعمل كـ **محلل بيانات (Data Analyst)** مع خبرة متخصصة في تحليل **البيانات الصحية والطبية وسجلات المستشفيات**، بالإضافة إلى تحليلات الأعمال والمبيعات[cite: 1].
        متخصص في معالجة وتنظيف البيانات المعقدة وتحويلها إلى رؤى عملية (Actionable Insights) ولوحات تحكم تفاعلية متكاملة باستخدام **Python**, **SQL**, **Power BI**, و **Excel** لدعم اتخاذ القرارات وإدارة مؤشرات الأداء (KPIs)[cite: 1].
        """)
        
        # Resume Download Button
        cv_path = "Mohamed_gamal_mahmoud_Ebrahim_Naukrigulf_CV_09Oct2026.pdf"
        if os.path.exists(cv_path):
            with open(cv_path, "rb") as pdf_file:
                st.download_button(
                    label="📄 تحميل السيرة الذاتية (Download CV)",
                    data=pdf_file,
                    file_name="Mohamed_Gamal_Data_Analyst_CV.pdf",
                    mime="application/pdf"
                )

    with col2:
        image_displayed = False
        for img_name in ["profile.jpg", "profile.png", "profile.jpeg"]:
            if os.path.exists(img_name):
                try:
                    img = Image.open(img_name)
                    st.image(img, use_container_width=True)
                    image_displayed = True
                    break
                except Exception:
                    continue
        
        if not image_displayed:
            st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=180)

    st.markdown('<p class="section-header">🛠️ المهارات والتقنيات (Skills & Technologies)</p>', unsafe_allow_html=True)
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown("""
        <div class="skill-card">
            <h4>🐍 Python Analytics</h4>
            <ul>
                <li>Pandas & NumPy</li>
                <li>Matplotlib & Seaborn</li>
                <li>Data Cleaning & Transformation</li>
                <li>Streamlit & Plotly Apps</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col_b:
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
        
    with col_c:
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

    st.markdown('<p class="section-header">💼 الخبرة المهنية (Professional Experience)</p>', unsafe_allow_html=True)
    st.markdown("""
    * **محلل بيانات | مستشفى البساتين / وحدة بساتين دمياط الصحية** *(أكتوبر 2024 - الحالي)*[cite: 1]
      * إدارة وتحليل السجلات الصحية والطبية وإعداد التقارير الإحصائية للأقسام[cite: 1].
      * معالجة البيانات وتنظيفها باستخدام Python و SQL للرفع من دقة التحليلات ومؤشرات الأداء[cite: 1].
    """)

# ---------------------------------------------------------
# PAGE 2: PROJECTS
# ---------------------------------------------------------
elif page == "🚀  المشاريع (Projects)":
    st.markdown('<p class="main-title">معرض المشاريع (Projects Showcase)</p>', unsafe_allow_html=True)
    st.write("تصفح المشاريع التفاعلية المدمجة أدناه:")

    category = st.selectbox("تصفية المشاريع (Filter Domain):", ["جميع المشاريع (All)", "تحليلات صحية (Healthcare)", "مبيعات وأعمال (Sales & Business)"])

    # --- PROJECT 1: Healthcare Analytics Dashboard ---
    if category in ["جميع المشاريع (All)", "تحليلات صحية (Healthcare)"]:
        with st.expander("🏥 1. لوحة تحليل الفواتير والبيانات الصحية (Healthcare Billing & Admission Dashboard)", expanded=True):
            st.write("""
            **وصف المشروع:** لوحة تحكم تفاعلية متكاملة لرصد وحساب إحصائيات المستشفى، تشمل توزيع إقامات المرضى حسب التخصصات الطبية، متوسط أيام الإقامة (LOS)، ونوع التأمين الطبي وتكاليف العلاج[cite: 1].
            """)
            st.markdown("**التقنيات المستخدمة:** `Python`, `Pandas`, `Plotly Express`, `Streamlit`, `EHR Data`")
            
            st.markdown("---")
            st.subheader("🏥 Healthcare Interactive Dashboard")

            # Filters for Healthcare Project
            h_col1, h_col2 = st.columns(2)
            with h_col1:
                selected_admission = st.selectbox("نوع الدخول (Admission Type):", ["الكل (All Types)", "Emergency", "Elective", "Urgent"])
            with h_col2:
                selected_gender = st.selectbox("الجنس (Gender):", ["الكل (All Genders)", "Male", "Female"])

            # Healthcare Simulated Data
            df_health_full = pd.DataFrame({
                "Specialty": ["Cardiology", "Neurology", "Orthopedics", "Pediatrics", "Oncology", "Cardiology", "Neurology", "Orthopedics"],
                "Admission_Type": ["Emergency", "Elective", "Urgent", "Emergency", "Elective", "Urgent", "Emergency", "Elective"],
                "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"],
                "Patients": [120, 85, 95, 140, 60, 110, 90, 80],
                "Avg_LOS_Days": [6.2, 4.5, 7.1, 3.2, 12.4, 5.8, 4.1, 6.9],
                "Avg_Charge": [4500, 5200, 3800, 2100, 6800, 4800, 5100, 3900]
            })

            # Filtering
            filtered_health = df_health_full.copy()
            if selected_admission != "الكل (All Types)":
                filtered_health = filtered_health[filtered_health["Admission_Type"] == selected_admission]
            if selected_gender != "الكل (All Genders)":
                filtered_health = filtered_health[filtered_health["Gender"] == selected_gender]

            # KPI Cards for Healthcare
            hkpi1, hkpi2, hkpi3 = st.columns(3)
            with hkpi1:
                st.markdown(f"<div class='metric-card-health'><h4>إجمالي المرضى</h4><h3>{filtered_health['Patients'].sum():,}</h3></div>", unsafe_allow_html=True)
            with hkpi2:
                st.markdown(f"<div class='metric-card-health'><h4>متوسط أيام الإقامة (LOS)</h4><h3>{round(filtered_health['Avg_LOS_Days'].mean(), 1)} أيام</h3></div>", unsafe_allow_html=True)
            with hkpi3:
                st.markdown(f"<div class='metric-card-health'><h4>متوسط تكلفة العلاج</h4><h3>${int(filtered_health['Avg_Charge'].mean()):,}</h3></div>", unsafe_allow_html=True)

            st.write("")

            # Charts for Healthcare
            h_chart1, h_chart2 = st.columns(2)
            with h_chart1:
                fig_h1 = px.bar(
                    filtered_health, x="Specialty", y="Patients", color="Specialty",
                    title="توزيع أعداد المرضى حسب التخصص",
                    color_discrete_sequence=px.colors.qualitative.Bold,
                    text_auto=True
                )
                st.plotly_chart(fig_h1, use_container_width=True)

            with h_chart2:
                fig_h2 = px.scatter(
                    filtered_health, x="Avg_LOS_Days", y="Avg_Charge", size="Patients", color="Specialty",
                    title="العلاقة بين متوسط أيام الإقامة والتكلفة الفعالة",
                    labels={"Avg_LOS_Days": "أيام الإقامة", "Avg_Charge": "التكلفة ($)"}
                )
                st.plotly_chart(fig_h2, use_container_width=True)

    # --- PROJECT 2: AdventureWorks Sales Dashboard ---
    if category in ["جميع المشاريع (All)", "مبيعات وأعمال (Sales & Business)"]:
        with st.expander("🛍️ 2. لوحة مبيعات AdventureWorks التفاعلية (AdventureWorks Sales Dashboard)", expanded=True):
            st.write("""
            **وصف المشروع:** لوحة تحكم تفاعلية متكاملة لتحليل بيانات مبيعات شركة **AdventureWorks**، تتيح متابعة إجمالي الإيرادات، الأرباح، فئات المنتجات الأعلى مبيعاً، والتوزيع الجغرافي للمبيعات.
            """)
            st.markdown("**التقنيات المستخدمة:** `Python`, `Pandas`, `Plotly Express`, `Streamlit`, `SQL Server (SSMS)`")
            
            st.markdown("---")
            st.subheader("📊 AdventureWorks Interactive Dashboard")

            # Filter Controls
            col_f1, col_f2 = st.columns(2)
            with col_f1:
                selected_year = st.selectbox("اختر السنة (Select Year):", ["الكل (All Years)", "2023", "2024"])
            with col_f2:
                selected_region = st.selectbox("اختر الإقليم (Select Region):", ["جميع الأقاليم (All Regions)", "North America", "Europe", "Pacific"])

            # Dummy/Simulated Data for AdventureWorks
            aw_sales = pd.DataFrame({
                "Year": ["2023", "2023", "2023", "2023", "2024", "2024", "2024", "2024"],
                "Month": ["Jan", "Feb", "Mar", "Apr", "Jan", "Feb", "Mar", "Apr"],
                "Category": ["Bikes", "Accessories", "Clothing", "Components", "Bikes", "Accessories", "Clothing", "Components"],
                "Region": ["North America", "Europe", "Pacific", "North America", "North America", "Europe", "Pacific", "Europe"],
                "Revenue": [45000, 12000, 8000, 15000, 58000, 16000, 11000, 19000],
                "Orders": [150, 320, 210, 180, 190, 410, 280, 220]
            })

            # Filter Logic
            filtered_df = aw_sales.copy()
            if selected_year != "الكل (All Years)":
                filtered_df = filtered_df[filtered_df["Year"] == selected_year]
            if selected_region != "جميع الأقاليم (All Regions)":
                filtered_df = filtered_df[filtered_df["Region"] == selected_region]

            # KPI Cards
            kpi1, kpi2, kpi3 = st.columns(3)
            with kpi1:
                st.markdown(f"<div class='metric-card'><h4>إجمالي المبيعات</h4><h3>${filtered_df['Revenue'].sum():,}</h3></div>", unsafe_allow_html=True)
            with kpi2:
                st.markdown(f"<div class='metric-card'><h4>إجمالي الطلبات</h4><h3>{filtered_df['Orders'].sum():,}</h3></div>", unsafe_allow_html=True)
            with kpi3:
                st.markdown(f"<div class='metric-card'><h4>متوسط قيمة الطلب</h4><h3>${int(filtered_df['Revenue'].sum() / filtered_df['Orders'].sum()):,}</h3></div>", unsafe_allow_html=True)

            st.write("")
            
            # Dashboard Charts
            ch1, ch2 = st.columns(2)
            
            with ch1:
                fig_cat = px.pie(
                    filtered_df, values="Revenue", names="Category",
                    title="توزيع الإيرادات حسب فئة المنتج (Revenue by Category)",
                    hole=0.4, color_discrete_sequence=px.colors.qualitative.Set2
                )
                st.plotly_chart(fig_cat, use_container_width=True)

            with ch2:
                fig_trend = px.bar(
                    filtered_df, x="Month", y="Revenue", color="Category",
                    title="المبيعات حسب الشهر والفئة (Monthly Revenue Trend)",
                    barmode="group",
                    color_discrete_sequence=px.colors.qualitative.Set1,
                    text_auto=True
                )
                st.plotly_chart(fig_trend, use_container_width=True)

# ---------------------------------------------------------
# PAGE 3: CONTACT
# ---------------------------------------------------------
elif page == "📬  التواصل (Contact)":
    st.markdown('<p class="main-title">تواصل معي (Get in Touch)</p>', unsafe_allow_html=True)
    st.write("سعيد دائماً بالتواصل للفرص المهنية والمشاريع المشتركة:")

    col_c1, col_c2 = st.columns(2)
    
    with col_c1:
        with st.form("contact_form"):
            name = st.text_input("الاسم (Your Name):")
            email = st.text_input("البريد الإلكتروني (Your Email):")
            message = st.text_area("الرسالة (Message):")
            submitted = st.form_submit_button("إرسال (Send) ✉️")
            
            if submitted:
                st.success(f"شكراً لك يا {name}! تم استلام رسالتك بنجاح.")

    with col_c2:
        st.markdown("""
        ### معلومات التواصل
        * **البريد الإلكتروني:** `mohgamgha@gmail.com`[cite: 1]
        * **الهاتف:** `+20 1127075974`[cite: 1]
        * **الموقع:** دمياط، مصر[cite: 1]
        * **LinkedIn:** [Mohamed Gamal Profile](https://linkedin.com)[cite: 1]
        * **GitHub:** [GitHub Repositories](https://github.com)
        """)