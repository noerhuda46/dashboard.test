"""
utils.py - Utility functions untuk Streamlit Dashboard
Berisi helper functions untuk data loading, processing, dan visualization
"""

import pandas as pd
import numpy as np
import streamlit as st
from datetime import datetime, timedelta
from constants import DATA_FILES, PRODUCTS, COLORS
try:
    import plotly.graph_objects as go
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except ImportError:
    print("Warning: plotly is not installed. Some visualizations may not work. Install it using 'pip install plotly'")
    PLOTLY_AVAILABLE = False
    go = None
    px = None

# ==================== DATA LOADING ====================

@st.cache_data(ttl=3600)
def load_transaction_data():
    """Load data transaksi dari CSV"""
    try:
        df = pd.read_csv(DATA_FILES['transactions'], sep=';')
        # Clean and rename columns
        df.columns = df.columns.str.strip()
        # Ensure date column - try different column names
        if 'Bulan' in df.columns:
            df['Tanggal'] = pd.to_datetime(df['Bulan'], format='%b-%Y', errors='coerce')
        elif 'Tanggal' in df.columns:
            df['Tanggal'] = pd.to_datetime(df['Tanggal'])
        return df
    except FileNotFoundError:
        st.error(f"File tidak ditemukan: {DATA_FILES['transactions']}")
        return pd.DataFrame()

@st.cache_data(ttl=3600)
def load_trend_results():
    """Load hasil trend analysis"""
    try:
        # Try reading with semicolon first
        df = pd.read_csv(DATA_FILES['trend_results'], sep=';')
        df.columns = df.columns.str.strip()
        
        # If there's only one column, it means columns are separated by comma in the cell
        if len(df.columns) == 1:
            # Re-read with comma separator
            df = pd.read_csv(DATA_FILES['trend_results'], sep=',')
            df.columns = df.columns.str.strip()
        
        return df
    except FileNotFoundError:
        st.error(f"File tidak ditemukan: {DATA_FILES['trend_results']}")
        return pd.DataFrame()

@st.cache_data(ttl=3600)
def load_preference_results():
    """Load hasil preference analysis"""
    try:
        # Try reading with semicolon first
        df = pd.read_csv(DATA_FILES['preference_results'], sep=';')
        df.columns = df.columns.str.strip()
        
        # If there's only one column, it means columns are separated by comma in the cell
        if len(df.columns) == 1:
            # Re-read with comma separator
            df = pd.read_csv(DATA_FILES['preference_results'], sep=',')
            df.columns = df.columns.str.strip()
        
        return df
    except FileNotFoundError:
        st.error(f"File tidak ditemukan: {DATA_FILES['preference_results']}")
        return pd.DataFrame()

# ==================== DATA PROCESSING ====================

def calculate_metrics(df):
    """Hitung key metrics dari transaction data"""
    if df.empty:
        return {
            'total_revenue': 0,
            'total_volume': 0,
            'avg_price': 0,
            'total_transactions': 0,
            'date_range': 'N/A',
            'top_product': 'N/A'
        }
    
    metrics = {
        'total_revenue': df['Jumlah'].sum() if 'Jumlah' in df.columns else 0,
        'total_volume': df['Qty Kg'].sum() if 'Qty Kg' in df.columns else 0,
        'avg_price': df['Harga Per Kg'].mean() if 'Harga Per Kg' in df.columns else 0,
        'total_transactions': len(df),
        'date_range': 'Januari - Desember 2025',
        'top_product': df['Nama Produk'].value_counts().index[0] if 'Nama Produk' in df.columns and len(df) > 0 else 'N/A'
    }
    return metrics

def get_monthly_trend(df):
    """Get monthly revenue trend"""
    if df.empty or 'Bulan' not in df.columns or 'Jumlah' not in df.columns:
        return pd.DataFrame()
    
    # Group by Bulan and sum Jumlah
    df_monthly = df.groupby('Bulan')['Jumlah'].sum().reset_index()
    df_monthly.columns = ['Month', 'Revenue']
    return df_monthly

# ==================== VISUALIZATION ====================

def create_metric_card(label, value, unit=""):
    """Create a metric card with HTML/CSS styling"""
    formatted_value = f"{value:,.0f}" if isinstance(value, (int, float)) else str(value)
    
    card_html = f"""
    <div style="
        background: linear-gradient(135deg, {COLORS['primary']} 0%, {COLORS['gradient_end']} 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin: 10px;
    ">
        <p style="margin: 0; font-size: 14px; opacity: 0.9;">{label}</p>
        <h3 style="margin: 10px 0 0 0; font-size: 28px;">{formatted_value}</h3>
        <p style="margin: 5px 0 0 0; font-size: 12px; opacity: 0.8;">{unit}</p>
    </div>
    """
    return card_html

def create_trend_chart(trend_results):
    """Create interactive trend chart"""
    if not PLOTLY_AVAILABLE:
        return None
    
    if trend_results.empty:
        return go.Figure()
    
    try:
        fig = go.Figure()
        
        # Determine column names
        product_col = None
        slope_col = None
        
        for col in trend_results.columns:
            col_lower = col.lower()
            if 'produk' in col_lower or 'product' in col_lower:
                product_col = col
            if 'slope' in col_lower:
                slope_col = col
        
        if not product_col or not slope_col:
            # Use first two columns as fallback
            product_col = trend_results.columns[0]
            slope_col = trend_results.columns[1] if len(trend_results.columns) > 1 else None
        
        if slope_col:
            for idx, row in trend_results.iterrows():
                product_name = str(row[product_col]) if product_col else f'Product {idx}'
                slope_value = float(row[slope_col]) if slope_col else 0
                
                fig.add_trace(go.Bar(
                    x=[product_name],
                    y=[slope_value],
                    name=product_name,
                    marker_color=COLORS['success'] if slope_value > 0 else COLORS['danger'],
                    hovertemplate='<b>%{x}</b><br>Slope: %{y:.2f}<extra></extra>'
                ))
        
        fig.update_layout(
            title="📈 Trend Analysis - Monthly Slope per Product",
            xaxis_title="Product",
            yaxis_title="Slope (Units/Month)",
            height=400,
            showlegend=False,
            hovermode='x unified',
            plot_bgcolor='rgba(240,240,240,0.5)',
            paper_bgcolor='white'
        )
        
        return fig
    except Exception as e:
        return go.Figure()

def create_preference_heatmap(preference_results):
    """Create preference heatmap visualization"""
    if not PLOTLY_AVAILABLE:
        return None
    
    if preference_results.empty:
        return go.Figure()
    
    try:
        # Cek kolom yang ada
        if 'Product' in preference_results.columns and 'Category' in preference_results.columns:
            pivot_data = preference_results.pivot_table(
                index='Product',
                columns='Category',
                values='Preference_Percentage',
                aggfunc='first'
            )
        else:
            # Fallback - gunakan kolom pertama sebagai rows dan kedua sebagai columns
            return go.Figure()
        
        fig = go.Figure(data=go.Heatmap(
            z=pivot_data.values,
            x=pivot_data.columns,
            y=pivot_data.index,
            colorscale='Blues',
            hovertemplate='<b>%{y}</b><br>%{x}: %{z:.1f}%<extra></extra>'
        ))
        
        fig.update_layout(
            title="🔥 Customer Preference Heatmap - Product × Category",
            xaxis_title="Customer Category",
            yaxis_title="Product",
            height=400,
            plot_bgcolor='white',
            paper_bgcolor='white'
        )
        
        return fig
    except Exception as e:
        return go.Figure()

def create_revenue_projection(base_revenue, growth_rate, months=6):
    """Create revenue projection chart"""
    if not PLOTLY_AVAILABLE:
        return None
    
    months_range = np.arange(0, months + 1)
    projected_revenue = base_revenue * (1 + growth_rate/100) ** months_range
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=months_range,
        y=projected_revenue,
        mode='lines+markers',
        name='Projected Revenue',
        line=dict(color=COLORS['success'], width=3),
        marker=dict(size=8),
        fill='tozeroy',
        fillcolor=f'rgba(39, 174, 96, 0.2)'
    ))
    
    fig.update_layout(
        title="💰 6-Month Revenue Projection (20% Growth)",
        xaxis_title="Month",
        yaxis_title="Revenue (IDR)",
        height=400,
        hovermode='x unified',
        plot_bgcolor='rgba(240,240,240,0.5)',
        paper_bgcolor='white'
    )
    
    return fig

# ==================== FORMATTING ====================

def format_currency(value):
    """Format value sebagai currency IDR"""
    if isinstance(value, (int, float)):
        if value >= 1_000_000:
            return f"Rp {value/1_000_000:.1f}M"
        elif value >= 1_000:
            return f"Rp {value/1_000:.0f}K"
        else:
            return f"Rp {value:.0f}"
    return str(value)

def format_percentage(value, decimals=1):
    """Format value sebagai percentage"""
    if isinstance(value, (int, float)):
        return f"{value:.{decimals}f}%"
    return str(value)

def format_number(value):
    """Format number dengan separator ribuan"""
    if isinstance(value, (int, float)):
        return f"{value:,.0f}"
    return str(value)

# ==================== TEXT CONTENT ====================

def get_product_description(product_name):
    """Get detailed description untuk product"""
    if product_name in PRODUCTS:
        return PRODUCTS[product_name]['description']
    return "Produk tidak ditemukan"

def get_trend_interpretation(slope):
    """Interpret trend based on slope value"""
    if slope > 5:
        return "📈 Rising Star - Pertumbuhan signifikan, fokus untuk maksimalkan"
    elif slope > 0:
        return "→ Stable Growth - Pertumbuhan konsisten, maintain strategi"
    elif slope > -2:
        return "⚠️ Slight Decline - Perlu perhatian, review strategi"
    else:
        return "↘️ Declining - Penurunan tajam, perlu action plan urgently"

# ==================== ACTION PLAN ====================

def get_action_plan_week(week_number):
    """Get action plan items for specific week"""
    action_plans = {
        1: {
            'title': '🎯 Week 1: Analysis & Planning',
            'items': [
                'Review trend analysis results dan identify opportunities',
                'Analyze customer preference patterns by category',
                'Create detailed action roadmap untuk 6 bulan',
                'Align dengan stakeholder tentang targets dan resources'
            ]
        },
        2: {
            'title': '🚀 Week 2: Market Activation',
            'items': [
                'Launch marketing campaign untuk rising stars (Java Halu, Bunar)',
                'Prepare promotional materials dan pricing strategies',
                'Brief sales team tentang new talking points',
                'Monitor initial market response'
            ]
        },
        3: {
            'title': '📊 Week 3: Portfolio Optimization',
            'items': [
                'Evaluate declining products (Taraju, Regional)',
                'Decide apakah perlu product discontinuation atau revamp',
                'Plan relaunch strategy untuk struggling products',
                'Update inventory berdasarkan new demand forecast'
            ]
        },
        4: {
            'title': '🎉 Week 4: Review & Adjust',
            'items': [
                'Measure Week 1-3 results vs targets',
                'Analyze customer feedback dan market response',
                'Make course corrections untuk Month 2-3',
                'Report findings ke management dengan recommendations'
            ]
        }
    }
    
    return action_plans.get(week_number, {})

# ==================== VALIDATION ====================

def validate_data(df, required_columns):
    """Validate if dataframe has required columns"""
    if df.empty:
        return False, "Data kosong"
    
    missing_columns = set(required_columns) - set(df.columns)
    if missing_columns:
        return False, f"Kolom yang hilang: {', '.join(missing_columns)}"
    
    return True, "Data valid"
