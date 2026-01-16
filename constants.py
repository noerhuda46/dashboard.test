"""
constants.py - Konstanta dan konfigurasi untuk Streamlit Dashboard
Galunggung Green Glory - Penjualan Kopi
"""

# ==================== COLOR SCHEME ====================
COLORS = {
    'primary': '#3498db',           # Blue
    'secondary': '#2c3e50',         # Dark blue-gray
    'success': '#27ae60',           # Green
    'warning': '#f39c12',           # Orange
    'danger': '#e74c3c',            # Red
    'light': '#ecf0f1',             # Light gray
    'dark': '#34495e',              # Dark gray
    'gradient_start': '#3498db',    # Blue
    'gradient_end': '#2980b9',      # Darker blue
}

# ==================== PRODUCT INFORMATION ====================
PRODUCTS = {
    'Java Halu': {
        'region': 'Jawa',
        'category': 'Premium Arabica',
        'description': 'Kopi premium dari dataran tinggi Jawa dengan cita rasa yang kaya',
        'trend_2025': 'Rising Star ⭐',
    },
    'Bunar': {
        'region': 'Sumatera',
        'category': 'Specialty Robusta',
        'description': 'Kopi specialty dari Sumatera dengan body yang kuat',
        'trend_2025': 'Rising Star ⭐',
    },
    'Parentas': {
        'region': 'Sumatera',
        'category': 'Premium Robusta',
        'description': 'Kopi premium dengan profil rasa yang kompleks',
        'trend_2025': 'Stable Growth →',
    },
    'Taraju': {
        'region': 'Sulawesi',
        'category': 'Single Origin',
        'description': 'Single origin dari Sulawesi dengan karakteristik unik',
        'trend_2025': 'Declining ↘️',
    },
    'Gunung Puntang': {
        'region': 'Jawa',
        'category': 'Estate Coffee',
        'description': 'Estate coffee berkualitas dari Gunung Puntang',
        'trend_2025': 'Stable Growth →',
    },
    'Regional': {
        'region': 'Mixed',
        'category': 'Blended',
        'description': 'Kopi blended dari berbagai region',
        'trend_2025': 'Declining ↘️',
    }
}

# ==================== CUSTOMER CATEGORIES ====================
CUSTOMER_CATEGORIES = {
    'Big Cafe': {
        'min_transaction': 50,
        'avg_transaction': 200,
        'description': 'Kafe besar dengan volume tinggi',
        'icon': '🏢',
    },
    'Medium Cafe': {
        'min_transaction': 20,
        'avg_transaction': 75,
        'description': 'Kafe menengah dengan regular order',
        'icon': '🏪',
    },
    'Perorangan': {
        'min_transaction': 1,
        'avg_transaction': 3,
        'description': 'Pembeli individual',
        'icon': '👤',
    }
}

# ==================== KPI TARGETS ====================
KPI_TARGETS = {
    'revenue_target_6month': 212_000_000,      # Rp 212M per bulan
    'revenue_base_2025': 176_500_000,          # Rp 176.5M current
    'growth_percentage': 20,                    # 20% growth
    'volume_increase': 15,                      # 15% volume increase
    'market_share_target': 35,                  # 35% market share
    'customer_retention': 92,                   # 92% retention rate
    'nps_target': 75,                           # Net Promoter Score
}

# ==================== FINANCIAL METRICS ====================
FINANCIAL = {
    'investment_amount': 357_000_000,           # Rp 357M investment
    'year_1_roi': 48,                           # 48% ROI in Year 1
    'payback_period_months': 2.1,              # 2.1 months payback
    'gross_margin_target': 35,                  # 35% gross margin
    'operational_cost_increase': 8,             # 8% for expansion
}

# ==================== TREND ANALYSIS ====================
TREND_CUTOFF = {
    'rising_star_threshold': 5,                 # Products with slope > 5
    'declining_threshold': -2,                  # Products with slope < -2
    'stable_range': (-2, 5),                   # Slope between -2 and 5
}

# ==================== VISUALIZATION CONFIG ====================
CHART_CONFIG = {
    'height': 500,
    'show_legend': True,
    'hovermode': 'x unified',
    'font_size': 12,
    'margin': dict(l=50, r=50, t=50, b=50),
}

HEATMAP_CONFIG = {
    'colorscale': 'Blues',
    'height': 400,
    'show_values': True,
}

# ==================== DATA FILES ====================
DATA_FILES = {
    'transactions': 'Transaksi Penjualan 2025.csv',
    'trend_results': 'trend_analysis_results.csv',
    'preference_results': 'preference_analysis_results.csv',
}

# ==================== TEXT CONTENT ====================
APP_TITLE = "📊 Dashboard Analisis Penjualan Galunggung Green Glory"
APP_SUBTITLE = "Big Data & Machine Learning Analysis | 2025"
APP_DESCRIPTION = """
Dashboard interaktif untuk analisis penjualan kopi Galunggung Green Glory 
menggunakan teknologi Big Data (Apache PySpark) dan Machine Learning.
"""

BUSINESS_OBJECTIVE = """
**Menganalisis dan mengoptimalkan strategi penjualan kopi Galunggung Green Glory** 
melalui:
- Analisis trend penjualan per jenis produk
- Analisis preferensi customer berdasarkan demografis
- Identifikasi rising stars dan declining products
- Rekomendasi strategi revenue growth
"""

ACTION_PLAN_HEADER = "📋 Rencana Aksi 30 Hari"
ACTION_PLAN_DESCRIPTION = "Implementasi strategi berdasarkan insights dari Big Data Analytics"

# ==================== SIDEBAR INFO ====================
SIDEBAR_INFO = """
### 📚 Tentang Dashboard

**Dashboard Version**: 2.0  
**Last Updated**: 16 Januari 2026  
**Data Period**: Januari - Desember 2025  

### 🔧 Teknologi yang Digunakan

- **Apache PySpark** - Big Data Processing
- **Scikit-learn** - Machine Learning Models
- **Streamlit** - Interactive Dashboard
- **Plotly** - Interactive Visualization

### 📊 Analysis Methods

- **Linear Regression** - Trend Analysis
- **Logistic Regression** - Preference Prediction
- **Heatmap Analysis** - Customer-Product Matrix

### 💾 Data Sources

- Transaksi-Penjualan-2025.csv (951 transactions)
- trend_analysis_results.csv (6 products)
- preference_analysis_results.csv (18 segments)
"""

# ==================== STATUS MESSAGES ====================
STATUS_MESSAGES = {
    'data_loaded': '✅ Data loaded successfully',
    'analysis_complete': '✅ Analysis complete',
    'error_loading': '❌ Error loading data',
    'no_data': '⚠️ No data available',
}

# ==================== PAGE CONFIG ====================
PAGE_CONFIG = {
    'page_title': 'Galunggung Coffee Dashboard',
    'page_icon': '☕',
    'layout': 'wide',
    'initial_sidebar_state': 'expanded',
}
