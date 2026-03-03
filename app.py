import streamlit as st
from src.data_loader import load_data
from src.metrics import *
from src.charts import *

st.set_page_config(page_title="E-Commerce Dashboard", layout="wide", page_icon="🛒")

# Chargement des données
@st.cache_data
def get_data():
    return load_data()

df = get_data()

# Sidebar
st.sidebar.title("🛒 E-Commerce Dashboard")
page = st.sidebar.radio("Navigation", ["Vue générale", "Clients", "Produits & Pays", "Tendances"])

# ─── PAGE 1 : Vue générale ───
if page == "Vue générale":
    st.title("📊 Vue générale")

    kpis = get_kpis(df)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("💰 CA Total", f"£{kpis['total_revenue']:,.0f}")
    col2.metric("📦 Commandes", f"{kpis['total_orders']:,}")
    col3.metric("🛒 Panier moyen", f"£{kpis['avg_basket']:,.0f}")
    col4.metric("👥 Clients", f"{kpis['total_customers']:,}")

    st.plotly_chart(chart_revenue_by_month(get_revenue_by_month(df)), use_container_width=True)

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(chart_orders_by_month(get_orders_by_month(df)), use_container_width=True)
    with col2:
        st.plotly_chart(chart_avg_basket_by_month(get_avg_basket_by_month(df)), use_container_width=True)

    st.plotly_chart(chart_revenue_by_weekday(get_revenue_by_weekday(df)), use_container_width=True)
    st.plotly_chart(chart_heatmap(df), use_container_width=True)

# ─── PAGE 2 : Clients ───
elif page == "Clients":
    st.title("👥 Analyse Clients")

    retention = get_retention(df)
    col1, col2 = st.columns(2)
    col1.metric("🆕 Nouveaux clients", f"{retention['new_customers']:,}")
    col2.metric("🔄 Clients récurrents", f"{retention['returning_customers']:,}")

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(chart_retention(retention), use_container_width=True)
    with col2:
        st.plotly_chart(chart_top_customers(get_top_customers(df)), use_container_width=True)

# ─── PAGE 3 : Produits & Pays ───
elif page == "Produits & Pays":
    st.title("📦 Produits & Pays")

    st.plotly_chart(chart_top_products(get_top_products(df)), use_container_width=True)
    st.plotly_chart(chart_world_map(get_top_countries(df, n=50)), use_container_width=True)
    st.plotly_chart(chart_top_countries(get_top_countries(df)), use_container_width=True)

# ─── PAGE 4 : Tendances ───
elif page == "Tendances":
    st.title("📈 Tendances")

    st.plotly_chart(chart_scatter(df), use_container_width=True)