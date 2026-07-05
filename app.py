import streamlit as st

from utils.loader import load_data
from utils.filters import apply_filters
from utils.metrics import calculate_metrics
from utils.charts import (
    create_sales_trend_chart,
    create_category_sales_chart,
    create_city_sales_chart,
    create_top_products_chart
)
from utils.style import apply_style


# ----------------------------
# APPLY GLOBAL STYLE
# ----------------------------
apply_style()


# ----------------------------
# LOAD DATA
# ----------------------------
data = load_data()
df = data["fact_enriched"]


# ----------------------------
# APPLY FILTERS (SIDEBAR)
# ----------------------------
filtered_df = apply_filters(df)


# ----------------------------
# CALCULATE KPI METRICS
# ----------------------------
metrics = calculate_metrics(filtered_df)


# ----------------------------
# HEADER
# ----------------------------
st.title("📊 E-Commerce Sales Dashboard")
st.markdown("Power BI-style analytics built with Streamlit + Plotly")


# ----------------------------
# KPI CARDS
# ----------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Total Sales", f"${metrics['total_sales']:,.2f}")

with col2:
    st.metric("🧾 Total Orders", f"{metrics['total_orders']:,}")

with col3:
    st.metric("📦 Total Quantity", f"{metrics['total_quantity']:,}")

with col4:
    st.metric("📈 Avg Order Value", f"${metrics['avg_order_value']:,.2f}")


st.markdown("---")


# ----------------------------
# SALES TREND
# ----------------------------
st.subheader("📈 Sales Trend")
st.plotly_chart(
    create_sales_trend_chart(filtered_df),
    use_container_width=True
)


# ----------------------------
# SECOND ROW CHARTS
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📦 Sales by Category")
    st.plotly_chart(
        create_category_sales_chart(filtered_df),
        use_container_width=True
    )

with col2:
    st.subheader("🏙️ Sales by City")
    st.plotly_chart(
        create_city_sales_chart(filtered_df),
        use_container_width=True
    )


st.markdown("---")


# ----------------------------
# TOP PRODUCTS
# ----------------------------
st.subheader("🏆 Top Products")
st.plotly_chart(
    create_top_products_chart(filtered_df, top_n=10),
    use_container_width=True
)


# ----------------------------
# FOOTER
# ----------------------------
st.markdown(
    """
    <div style='text-align: center; color: gray; padding: 20px;'>
        E-Commerce Dashboard • Streamlit + Plotly • Power BI Style
    </div>
    """,
    unsafe_allow_html=True
)
