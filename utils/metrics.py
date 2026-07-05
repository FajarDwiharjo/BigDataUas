import pandas as pd
import plotly.express as px


# ----------------------------
# SALES TREND (LINE CHART)
# ----------------------------
def create_sales_trend_chart(df: pd.DataFrame):
    """
    Monthly/temporal sales trend line chart.
    """

    if df is None or df.empty:
        return px.line(title="No data available")

    date_col_candidates = ["Date", "date", "OrderDate", "order_date"]
    sales_col_candidates = ["Sales", "sales", "TotalSales", "revenue", "Revenue", "amount"]

    date_col = next((c for c in date_col_candidates if c in df.columns), None)
    sales_col = next((c for c in sales_col_candidates if c in df.columns), None)

    if not date_col or not sales_col:
        return px.line(title="Missing required columns")

    temp = df.copy()
    temp[date_col] = pd.to_datetime(temp[date_col], errors="coerce")
    temp = temp.dropna(subset=[date_col])

    grouped = (
        temp.groupby(temp[date_col].dt.to_period("M"))[sales_col]
        .sum()
        .reset_index()
    )

    grouped["date"] = grouped[date_col].astype(str)

    fig = px.line(
        grouped,
        x="date",
        y=sales_col,
        markers=True,
        title="📈 Sales Trend Over Time"
    )

    fig.update_layout(
        template="plotly_dark",
        height=400,
        margin=dict(l=20, r=20, t=40, b=20)
    )

    return fig


# ----------------------------
# CATEGORY SALES (BAR)
# ----------------------------
def create_category_sales_chart(df: pd.DataFrame):
    """
    Sales by product category.
    """

    if df is None or df.empty:
        return px.bar(title="No data available")

    sales_col_candidates = ["Sales", "sales", "TotalSales", "revenue", "Revenue", "amount"]
    category_col_candidates = ["Category", "category", "ProductCategory", "product_category"]

    sales_col = next((c for c in sales_col_candidates if c in df.columns), None)
    category_col = next((c for c in category_col_candidates if c in df.columns), None)

    if not sales_col or not category_col:
        return px.bar(title="Missing required columns")

    grouped = (
        df.groupby(category_col)[sales_col]
        .sum()
        .reset_index()
        .sort_values(sales_col, ascending=False)
    )

    fig = px.bar(
        grouped,
        x=category_col,
        y=sales_col,
        color=sales_col,
        text_auto=True,
        title="📦 Sales by Category"
    )

    fig.update_layout(
        template="plotly_dark",
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
        showlegend=False
    )

    return fig


# ----------------------------
# CITY SALES (BAR)
# ----------------------------
def create_city_sales_chart(df: pd.DataFrame):
    """
    Sales performance by city.
    """

    if df is None or df.empty:
        return px.bar(title="No data available")

    sales_col_candidates = ["Sales", "sales", "TotalSales", "revenue", "Revenue", "amount"]
    city_col_candidates = ["City", "city", "CityName", "city_name"]

    sales_col = next((c for c in sales_col_candidates if c in df.columns), None)
    city_col = next((c for c in city_col_candidates if c in df.columns), None)

    if not sales_col or not city_col:
        return px.bar(title="Missing required columns")

    grouped = (
        df.groupby(city_col)[sales_col]
        .sum()
        .reset_index()
        .sort_values(sales_col, ascending=False)
    )

    fig = px.bar(
        grouped,
        x=city_col,
        y=sales_col,
        color=sales_col,
        text_auto=True,
        title="🏙️ Sales by City"
    )

    fig.update_layout(
        template="plotly_dark",
        height=400,
        margin=dict(l=20, r=20, t=40, b=20),
        showlegend=False
    )

    return fig


# ----------------------------
# TOP PRODUCTS (HORIZONTAL BAR)
# ----------------------------
def create_top_products_chart(df: pd.DataFrame, top_n: int = 10):
    """
    Top N products by sales.
    """

    if df is None or df.empty:
        return px.bar(title="No data available")

    sales_col_candidates = ["Sales", "sales", "TotalSales", "revenue", "Revenue", "amount"]
    product_col_candidates = ["Product", "product", "ProductName", "product_name"]

    sales_col = next((c for c in sales_col_candidates if c in df.columns), None)
    product_col = next((c for c in product_col_candidates if c in df.columns), None)

    if not sales_col or not product_col:
        return px.bar(title="Missing required columns")

    grouped = (
        df.groupby(product_col)[sales_col]
        .sum()
        .reset_index()
        .sort_values(sales_col, ascending=False)
        .head(top_n)
    )

    fig = px.bar(
        grouped,
        x=sales_col,
        y=product_col,
        orientation="h",
        text_auto=True,
        title=f"🏆 Top {top_n} Products by Sales"
    )

    fig.update_layout(
        template="plotly_dark",
        height=500,
        margin=dict(l=20, r=20, t=40, b=20),
        yaxis=dict(autorange="reversed")
    )

    return fig
    