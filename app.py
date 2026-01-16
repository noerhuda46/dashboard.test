"""
app.py - Main Streamlit Application
Galunggung Green Glory - Dashboard Analisis Penjualan & Big Data Analytics

Cara menjalankan:
streamlit run app.py
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from constants import *
from utils import *
from datetime import datetime

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title=PAGE_CONFIG['page_title'],
    page_icon=PAGE_CONFIG['page_icon'],
    layout=PAGE_CONFIG['layout'],
    initial_sidebar_state=PAGE_CONFIG['initial_sidebar_state']
)

# ==================== CUSTOM CSS ====================
st.markdown("""
<style>
    /* Main container */
    .main {
        padding-top: 2rem;
    }
    
    /* Header styling */
    .header-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 0.5rem;
    }
    
    .header-subtitle {
        font-size: 1.1rem;
        color: #7f8c8d;
        margin-bottom: 2rem;
    }
    
    /* Card styling */
    .metric-card {
        background: linear-gradient(135deg, #3498db 0%, #2980b9 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 12px rgba(0,0,0,0.15);
        transition: all 0.3s ease;
    }
    
    /* Section header */
    .section-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2c3e50;
        border-left: 4px solid #3498db;
        padding-left: 1rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    
    /* Table styling */
    .dataframe {
        font-size: 0.9rem;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background-color: #ecf0f1;
    }
    
    /* Success message */
    .success-box {
        background-color: #d5f4e6;
        border-left: 4px solid #27ae60;
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ==================== SIDEBAR ====================
with st.sidebar:
    st.markdown("### ☕ Galunggung Green Glory")
    st.markdown("---")
    
    # Navigation
    page = st.radio(
        "Navigasi:",
        ["📊 Dashboard", "📈 Analisis Trend", "❤️ Preferensi Customer", 
         "📋 Action Plan", "🎯 KPI & Proyeksi", "ℹ️ Tentang"]
    )
    
    st.markdown("---")
    st.markdown(SIDEBAR_INFO)
    
    # Download resources
    st.markdown("### 📥 Download Resources")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📄 Laporan PDF"):
            st.info("Link download akan disediakan")
    
    with col2:
        if st.button("📊 Data CSV"):
            st.info("Link download akan disediakan")

# ==================== MAIN APP ====================

if page == "📊 Dashboard":
    # Header
    st.markdown('<h1 class="header-title">📊 Galunggung Green Glory Dashboard</h1>', unsafe_allow_html=True)
    st.markdown('<p class="header-subtitle">Analisis Penjualan & Big Data Analytics 2025</p>', unsafe_allow_html=True)
    
    # Load data
    df_transactions = load_transaction_data()
    df_trend = load_trend_results()
    df_preference = load_preference_results()
    
    if df_transactions.empty:
        st.error("❌ Tidak bisa memuat data transaksi. Pastikan file CSV ada di folder `data/`")
        st.stop()
    
    # ===== SECTION TUJUAN TUGAS =====
    st.markdown("---")
    st.markdown("### 🎯 TUJUAN TUGAS & LATAR BELAKANG")
    
    # Tujuan Umum
    st.markdown("#### 📋 Tujuan Umum")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **📊 Menganalisis Data Penjualan**
        
        Menggunakan Big Data Analytics untuk memahami pola penjualan 6 jenis kopi dari Galunggung Green Glory selama tahun 2025.
        """)
    
    with col2:
        st.markdown("""
        **💡 Mengoptimalkan Strategi**
        
        Mengidentifikasi rising stars dan declining products untuk optimasi portfolio dan peningkatan revenue growth 20% dalam 6 bulan.
        """)
    
    with col3:
        st.markdown("""
        **🎯 Mendukung Keputusan**
        
        Menyediakan insights berbasis data untuk mendukung strategic decision-making dan ROI improvement 48% Year 1.
        """)
    
    # Pertanyaan Bisnis
    st.markdown("#### 💰 Pertanyaan Bisnis")
    
    with st.expander("💰 Q1: Bagaimana Cara Meningkatkan Value Penjualan?", expanded=True):
        st.markdown("""
        **Pertanyaan:**
        Bagaimana cara meningkatkan value penjualan Galunggung Green Glory secara signifikan dan sustainable dalam 6 bulan ke depan?
        
        **Context:**
        - Revenue baseline 2025: Rp 176.5M/bulan
        - Target 6 bulan: Rp 212M/bulan (+20% growth)
        - Investment needed: Rp 357M
        
        **Expected Answer:**
        - Fokus pada rising stars (Java Halu ⭐, Bunar ⭐)
        - Agresif marketing untuk high-potential segments
        - Optimize pricing & promotional strategy per category
        """)
    
    with st.expander("📦 Q2: Apakah Perlu Menambahkan Produk Kopi Baru?"):
        st.markdown("""
        **Pertanyaan:**
        Apakah Galunggung Green Glory perlu menambahkan produk kopi baru atau lebih baik fokus optimasi existing portfolio?
        
        **Context:**
        - Current portfolio: 6 jenis kopi (Java Halu, Bunar, Parentas, Taraju, Gunung Puntang, Regional)
        - Declining products: Taraju ↘️, Regional ↘️
        - Available budget: Rp 50-75M untuk product development
        
        **Expected Answer:**
        - Rekomendasi: Optimasi existing portfolio dulu
        - Revitalisasi declining products sebelum launch baru
        - New product launch target: Q4 2025 (setelah optimize existing)
        """)
    
    # Pertanyaan Analisis
    st.markdown("#### 📊 Pertanyaan Analisis & Metodologi")
    
    analysis_items = [
        {
            'num': '1️⃣',
            'title': 'Trend Penjualan Per Jenis Kopi',
            'description': 'Menganalisis trend penjualan untuk 6 jenis kopi menggunakan Linear Regression untuk mengidentifikasi rising stars vs declining products. Metric: Monthly slope & R-squared.',
        },
        {
            'num': '2️⃣',
            'title': 'Preferensi Pelanggan Berdasarkan Demografis',
            'description': 'Menganalisis preferensi customer per kategori (Big Cafe, Medium Cafe, Perorangan) menggunakan Logistic Regression untuk memahami buying behavior dan targeting strategy.',
        },
        {
            'num': '3️⃣',
            'title': 'Implementasi dengan Apache PySpark',
            'description': 'Processing 951 transaksi menggunakan Apache PySpark untuk parallel computation + Scikit-learn ML models + output visualization dengan interactive charts.',
        }
    ]
    
    for item in analysis_items:
        col1, col2 = st.columns([0.5, 3])
        with col1:
            st.markdown(f"### {item['num']}")
        with col2:
            st.markdown(f"**{item['title']}**")
            st.markdown(item['description'])
    
    # Teknologi & Metodologi
    st.markdown("#### ⚙️ Teknologi & Metodologi")
    
    tech_cols = st.columns(4)
    
    tech_items = [
        {
            'title': '🔧 Big Data',
            'desc': 'Apache PySpark untuk processing 951 transaksi dengan efficient parallel computation',
            'col': tech_cols[0]
        },
        {
            'title': '🤖 ML Models',
            'desc': 'Linear Regression (Trend) + Logistic Regression (Preference) + Scikit-learn',
            'col': tech_cols[1]
        },
        {
            'title': '📊 Visualization',
            'desc': 'Interactive Charts (Plotly) + Static visualizations (Matplotlib)',
            'col': tech_cols[2]
        },
        {
            'title': '📁 Output',
            'desc': 'Jupyter Notebook + Dashboard HTML + CSV Data + PNG Charts + MD Reports',
            'col': tech_cols[3]
        }
    ]
    
    for tech in tech_items:
        with tech['col']:
            st.markdown(f"**{tech['title']}**")
            st.markdown(tech['desc'])
    
    # Expected Business Impact
    st.markdown("#### 🎯 Expected Business Impact")
    
    impact_cols = st.columns(4)
    
    impact_items = [
        {
            'icon': '📈',
            'title': 'Revenue Growth',
            'current': 'Rp 176.5M/bulan',
            'target': 'Rp 212M/bulan',
            'growth': '+20%',
            'col': impact_cols[0]
        },
        {
            'icon': '🎯',
            'title': 'Portfolio Optimization',
            'current': '6 products',
            'target': '4-5 focus products',
            'growth': '+Revenue mix',
            'col': impact_cols[1]
        },
        {
            'icon': '🌍',
            'title': 'Market Strategy',
            'current': 'General approach',
            'target': 'Segmented targeting',
            'growth': '+Efficiency',
            'col': impact_cols[2]
        },
        {
            'icon': '💰',
            'title': 'ROI Investment',
            'current': 'Rp 357M invest',
            'target': 'Year 1: 48% ROI',
            'growth': 'Payback: 2.1yr',
            'col': impact_cols[3]
        }
    ]
    
    for impact in impact_items:
        with impact['col']:
            st.markdown(f"### {impact['icon']} {impact['title']}")
            st.markdown(f"**Saat ini:** {impact['current']}")
            st.markdown(f"**Target:** {impact['target']}")
            st.markdown(f"**Impact:** {impact['growth']}")
    
    # ===== KEY METRICS =====
    st.markdown("---")
    st.markdown("### 📊 KEY METRICS")
    
    metrics = calculate_metrics(df_transactions)
    
    metric_cols = st.columns(6)
    
    with metric_cols[0]:
        st.metric(
            "💰 Total Revenue",
            format_currency(metrics['total_revenue']),
            help="Total penjualan selama periode"
        )
    
    with metric_cols[1]:
        st.metric(
            "📦 Total Volume",
            format_number(metrics['total_volume']),
            help="Total unit yang terjual"
        )
    
    with metric_cols[2]:
        st.metric(
            "💵 Avg Price",
            format_currency(metrics['avg_price']),
            help="Average harga per transaksi"
        )
    
    with metric_cols[3]:
        st.metric(
            "🔢 Total Transactions",
            format_number(metrics['total_transactions']),
            help="Total jumlah transaksi"
        )
    
    with metric_cols[4]:
        st.metric(
            "📅 Period",
            metrics['date_range'],
            help="Range periode data"
        )
    
    with metric_cols[5]:
        st.metric(
            "⭐ Top Product",
            metrics['top_product'],
            help="Produk dengan volume tertinggi"
        )
    
    # Trend Analysis Section
    st.markdown("---")
    st.markdown("### 📈 TREND ANALYSIS")
    
    if not df_trend.empty:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig_trend = create_trend_chart(df_trend)
            st.plotly_chart(fig_trend, width='stretch')
        
        with col2:
            st.markdown("**📊 Trend Interpretation:**")
            for _, row in df_trend.iterrows():
                # Get slope from available columns
                slope = 0
                for col_name in ['Slope_Kg_Per_Bulan', 'Slope', 'slope']:
                    if col_name in row.index:
                        slope = float(row[col_name])
                        break
                # Get product from available columns
                product = 'N/A'
                for col_name in ['Produk', 'Product', 'produk']:
                    if col_name in row.index:
                        product = str(row[col_name])
                        break
                interpretation = get_trend_interpretation(slope)
                st.markdown(f"**{product}**  \n{interpretation}")
            
            st.markdown("**Aksi Rekomendasi:**")
            st.markdown("""
            - **Rising Stars**: Maksimalkan marketing & pricing
            - **Stable**: Maintain current strategy
            - **Declining**: Review & reposition
            """)
        
        # Detailed Trend Results
        st.markdown("#### 📋 Detailed Trend Results")
        st.dataframe(
            df_trend.style.format({
                'Slope': '{:.2f}',
                'Intercept': '{:.0f}',
                'R_squared': '{:.3f}',
                'Volume': '{:,.0f}',
                'Revenue': '{:,.0f}'
            }),
            width='stretch'
        )
    
    else:
        st.warning("⚠️ Data trend tidak tersedia")
    
    # Preference Analysis Section
    st.markdown("---")
    st.markdown("### ❤️ PREFERENCE ANALYSIS")
    
    if not df_preference.empty:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig_heatmap = create_preference_heatmap(df_preference)
            st.plotly_chart(fig_heatmap, use_container_width=True)
        
        with col2:
            st.markdown("**🔍 Key Insights:**")
            
            # Find top preferences
            if 'Preference_Percentage' in df_preference.columns:
                top_prefs = df_preference.nlargest(3, 'Preference_Percentage')
            else:
                top_prefs = df_preference.head(3)
                
            for idx, row in top_prefs.iterrows():
                product_name = row.get('Produk', row.get('Product', 'N/A')) if hasattr(row, 'get') else 'N/A'
                category = row.get('Kategori', row.get('Category', 'N/A')) if hasattr(row, 'get') else 'N/A'
                pref_pct = row.get('Preference_Percentage', 0) if hasattr(row, 'get') else 0
                st.markdown(f"""
                **{product_name}** → {category}
                - {pref_pct:.1f}% preference
                """)
            
            st.markdown("**💡 Strategy:**")
            st.markdown("""
            - Target high-preference segments
            - Customize offerings per category
            - Focus on Big Cafe & Medium Cafe
            """)
        
        # Detailed Preference Results
        st.markdown("#### 📋 Detailed Preference Results")
        
        # Check if required columns exist before sorting and formatting
        if 'Preference_Percentage' in df_preference.columns:
            sorted_df = df_preference.sort_values('Preference_Percentage', ascending=False)
            format_dict = {
                'Preference_Percentage': '{:.1f}%',
                'Transactions': '{:,.0f}',
                'Revenue_IDR': '{:,.0f}'
            }
            # Only include columns that exist in the dataframe
            available_formats = {k: v for k, v in format_dict.items() if k in sorted_df.columns}
            st.dataframe(
                sorted_df.style.format(available_formats),
                use_container_width=True
            )
        else:
            st.dataframe(df_preference, use_container_width=True)
    
    else:
        st.warning("⚠️ Data preferensi tidak tersedia")
    
    # Financial Projections
    st.markdown("---")
    st.markdown("### 💰 FINANCIAL PROJECTIONS")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        fig_projection = create_revenue_projection(
            metrics['total_revenue'],
            20,
            6
        )
        st.plotly_chart(fig_projection, use_container_width=True)
    
    with col2:
        st.markdown("**📊 Projection Details:**")
        st.markdown(f"""
        - **Base Revenue**: {format_currency(metrics['total_revenue'])}/bulan
        - **Growth Target**: 20% dalam 6 bulan
        - **Month 6 Target**: Rp 212M/bulan
        - **Investment**: Rp 357M
        - **Expected ROI**: 48% Year 1
        - **Payback Period**: 2.1 tahun
        """)

elif page == "📈 Analisis Trend":
    st.header("📈 Analisis Trend Penjualan")
    
    df_trend = load_trend_results()
    
    if df_trend.empty:
        st.error("Data trend tidak tersedia")
    else:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            fig = create_trend_chart(df_trend)
            st.plotly_chart(fig, width='stretch')
        
        with col2:
            st.markdown("### 📊 Interpretasi Trend")
            for _, row in df_trend.iterrows():
                # Get slope from available columns
                slope = 0
                for col_name in ['Slope_Kg_Per_Bulan', 'Slope', 'slope']:
                    if col_name in row.index:
                        slope = float(row[col_name])
                        break
                # Get product from available columns
                product = 'N/A'
                for col_name in ['Produk', 'Product', 'produk']:
                    if col_name in row.index:
                        product = str(row[col_name])
                        break
                st.markdown(f"**{product}** ({slope:.2f})")
                st.markdown(f"> {get_trend_interpretation(slope)}")
        
        st.markdown("---")
        st.markdown("### 📋 Detail Data")
        st.dataframe(df_trend, use_container_width=True)

elif page == "❤️ Preferensi Customer":
    st.header("❤️ Analisis Preferensi Customer")
    
    df_pref = load_preference_results()
    
    if df_pref.empty:
        st.error("Data preferensi tidak tersedia")
    else:
        fig = create_preference_heatmap(df_pref)
        st.plotly_chart(fig, width='stretch')
        
        st.markdown("---")
        st.markdown("### 📊 Top Preferences")
        
        col1, col2, col3 = st.columns(3)
        
        if 'Preference_Percentage' in df_pref.columns:
            top_3 = df_pref.nlargest(3, 'Preference_Percentage')
        else:
            top_3 = df_pref.head(3)
        
        for idx, (i, row) in enumerate(top_3.iterrows()):
            col = [col1, col2, col3][idx]
            with col:
                product_name = row.get('Produk', row.get('Product', 'N/A')) if hasattr(row, 'get') else 'N/A'
                category = row.get('Kategori', row.get('Category', 'N/A')) if hasattr(row, 'get') else 'N/A'
                pref_pct = row.get('Preference_Percentage', 0) if hasattr(row, 'get') else 0
                st.metric(
                    f"{product_name} → {category}",
                    f"{pref_pct:.1f}%"
                )
        
        st.markdown("---")
        st.markdown("### 📋 Semua Data")
        if 'Preference_Percentage' in df_pref.columns:
            sorted_df = df_pref.sort_values('Preference_Percentage', ascending=False)
        else:
            sorted_df = df_pref
            
        st.dataframe(
            sorted_df,
            width='stretch'
        )

elif page == "📋 Action Plan":
    st.header("📋 Rencana Aksi 30 Hari")
    
    st.markdown("Implementasi strategi berdasarkan insights dari Big Data Analytics")
    
    for week in range(1, 5):
        plan = get_action_plan_week(week)
        
        with st.expander(f"### {plan.get('title', f'Week {week}')}"):
            items = plan.get('items', [])
            for i, item in enumerate(items, 1):
                st.checkbox(f"{item}", key=f"week_{week}_item_{i}")

elif page == "🎯 KPI & Proyeksi":
    st.header("🎯 KPI Targets & Financial Projections")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Revenue Target (6 bulan)", "Rp 212M", "+20%")
    
    with col2:
        st.metric("Volume Increase", "15%", "+15%")
    
    with col3:
        st.metric("Market Share Target", "35%", "+5%")
    
    with col4:
        st.metric("Customer Retention", "92%", "+8%")
    
    st.markdown("---")
    
    # Financial projection
    df_trans = load_transaction_data()
    if not df_trans.empty:
        metrics = calculate_metrics(df_trans)
        fig = create_revenue_projection(metrics['total_revenue'], 20, 6)
        st.plotly_chart(fig, width='stretch')

elif page == "ℹ️ Tentang":
    st.header("ℹ️ Tentang Dashboard")
    
    st.markdown("""
    ### 📊 Galunggung Green Glory Dashboard
    
    Dashboard interaktif untuk analisis penjualan kopi Galunggung Green Glory 
    menggunakan teknologi Big Data dan Machine Learning.
    
    #### 🔧 Teknologi yang Digunakan
    - **Streamlit** - Interactive Dashboard Framework
    - **Apache PySpark** - Big Data Processing
    - **Scikit-learn** - Machine Learning Models
    - **Plotly** - Interactive Visualization
    - **Pandas** - Data Processing
    
    #### 📊 Analisis yang Dilakukan
    - **Linear Regression** - Trend Analysis
    - **Logistic Regression** - Customer Preference
    - **Heatmap Analysis** - Product-Category Correlation
    
    #### 🎯 Objektif
    - Mengidentifikasi rising stars dan declining products
    - Mengoptimalkan portfolio penjualan
    - Meningkatkan revenue 20% dalam 6 bulan
    - Mendukung strategic decision-making
    
    #### 📈 Expected Outcomes
    - Revenue Growth: Rp 176.5M → Rp 212M/bulan
    - ROI Year 1: 48%
    - Payback Period: 2.1 tahun
    - Market Share: +5% (target 35%)
    
    ---
    
    **Dashboard Version**: 2.0  
    **Last Updated**: 16 Januari 2026  
    **Status**: ✅ Production Ready
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7f8c8d; font-size: 0.9rem;">
    <p>📊 Galunggung Green Glory Dashboard | Big Data & ML Analytics</p>
    <p>Dibuat: 16 Januari 2026 | Version 2.0</p>
</div>
""", unsafe_allow_html=True)
