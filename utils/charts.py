# ==========================================================
# utils/charts.py (Part 1 of 2)
# ==========================================================

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==========================================================
# Dashboard Color Palette
# ==========================================================

COLORS = {
    "primary": "#2563EB",
    "success": "#16A34A",
    "warning": "#F59E0B",
    "danger": "#DC2626",
    "purple": "#8B5CF6",
    "cyan": "#06B6D4",

    "background": "#FFFFFF",
    "grid": "#E5E7EB",
    "text": "#111827",
    "muted": "#6B7280"
}

CATEGORY_COLORS = [
    "#2563EB",
    "#16A34A",
    "#F59E0B",
    "#8B5CF6",
    "#06B6D4",
    "#EF4444",
    "#10B981",
    "#F97316"
]

# ==========================================================
# Common Styling
# ==========================================================

def style_chart(
    fig,
    title,
    x_title="",
    y_title="",
    height=520,
    legend=False
):
    fig.update_layout(

        template="plotly_white",

        title=dict(
            text=title,
            x=0.5,
            xanchor="center",
            font=dict(
                size=22,
                color=COLORS["text"]
            )
        ),

        height=height,

        font=dict(
            family="Arial",
            size=14,
            color=COLORS["text"]
        ),

        paper_bgcolor="white",
        plot_bgcolor="white",

        margin=dict(
            l=40,
            r=40,
            t=70,
            b=40
        ),

        hovermode="x unified",

        showlegend=legend,

        legend=dict(
            bgcolor="rgba(0,0,0,0)"
        )
    )

    fig.update_xaxes(

        title=x_title,

        showgrid=False,

        zeroline=False,

        showline=False

    )

    fig.update_yaxes(

        title=y_title,

        gridcolor=COLORS["grid"],

        gridwidth=1,

        zeroline=False,

        showline=False

    )

    return fig


# ==========================================================
# Monthly Sales Trend
# ==========================================================

def create_monthly_sales_chart(df):

    monthly = (
        df.groupby("MonthYear", as_index=False)["Sales"]
        .sum()
    )

    fig = px.line(

        monthly,

        x="MonthYear",

        y="Sales",

        markers=True

    )

    fig.update_traces(

        line_color=COLORS["primary"],

        line_width=4,

        marker=dict(
            size=9,
            color=COLORS["primary"]
        ),

        hovertemplate=
        "<b>%{x}</b><br>"
        "Sales: %{y:,}<extra></extra>"

    )

    style_chart(

        fig,

        "Monthly Sales Trend",

        "Month",

        "Sales"

    )

    return fig


# ==========================================================
# Monthly Revenue Trend
# ==========================================================

def create_monthly_revenue_chart(df):

    monthly = (
        df.groupby("MonthYear", as_index=False)["Revenue"]
        .sum()
    )

    fig = px.line(

        monthly,

        x="MonthYear",

        y="Revenue",

        markers=True

    )

    fig.update_traces(

        line_color=COLORS["success"],

        line_width=4,

        marker=dict(
            size=9,
            color=COLORS["success"]
        ),

        hovertemplate=
        "<b>%{x}</b><br>"
        "Revenue: $%{y:,.2f}<extra></extra>"

    )

    style_chart(

        fig,

        "Monthly Revenue Trend",

        "Month",

        "Revenue"

    )

    return fig


# ==========================================================
# Sales by Category
# ==========================================================

def create_sales_category_chart(df):

    sales = (

        df.groupby("Category", as_index=False)["Sales"]

        .sum()

        .sort_values("Sales", ascending=False)

    )

    fig = px.bar(

        sales,

        x="Category",

        y="Sales",

        color="Category",

        color_discrete_sequence=CATEGORY_COLORS,

        text_auto=","

    )

    fig.update_traces(

        textposition="outside",

        hovertemplate=

        "<b>%{x}</b><br>"

        "Sales: %{y:,}<extra></extra>"

    )

    style_chart(

        fig,

        "Sales by Category",

        "Category",

        "Sales"

    )

    return fig


# ==========================================================
# Revenue by Category
# ==========================================================

def create_revenue_category_chart(df):

    revenue = (

        df.groupby("Category", as_index=False)["Revenue"]

        .sum()

        .sort_values("Revenue", ascending=False)

    )

    fig = px.bar(

        revenue,

        x="Category",

        y="Revenue",

        color="Category",

        color_discrete_sequence=CATEGORY_COLORS,

        text_auto=".2s"

    )

    fig.update_traces(

        textposition="outside",

        hovertemplate=

        "<b>%{x}</b><br>"

        "Revenue: $%{y:,.2f}<extra></extra>"

    )

    style_chart(

        fig,

        "Revenue by Category",

        "Category",

        "Revenue"

    )

    return fig


# ==========================================================
# Category Distribution
# ==========================================================

def create_category_donut_chart(df):

    sales = (

        df.groupby("Category", as_index=False)["Sales"]

        .sum()

    )

    fig = px.pie(

        sales,

        values="Sales",

        names="Category",

        hole=0.55,

        color_discrete_sequence=CATEGORY_COLORS

    )

    fig.update_traces(

        textinfo="percent+label",

        pull=[0.02] * len(sales),

        hovertemplate=

        "<b>%{label}</b><br>"

        "Sales: %{value:,}<br>"

        "Share: %{percent}<extra></extra>"

    )

    style_chart(

        fig,

        "Category Distribution",

        height=560,

        legend=True

    )

    return fig


# ==========================================================
# Revenue by City
# ==========================================================

def create_city_revenue_chart(df):

    city = (

        df.groupby("CityName", as_index=False)["Revenue"]

        .sum()

        .sort_values("Revenue", ascending=False)

        .head(10)

    )

    fig = px.bar(

        city,

        x="Revenue",

        y="CityName",

        orientation="h",

        color="Revenue",

        color_continuous_scale="Blues",

        text_auto=".2s"

    )

    fig.update_layout(

        coloraxis_showscale=False

    )

    fig.update_traces(

        textposition="outside",

        hovertemplate=

        "<b>%{y}</b><br>"

        "Revenue: $%{x:,.2f}<extra></extra>"

    )

    fig.update_yaxes(

        categoryorder="total ascending"

    )

    style_chart(

        fig,

        "Top 10 Cities by Revenue",

        "Revenue",

        ""

    )

    return fig

    # ==========================================================
# Top 10 Products by Sales
# ==========================================================

def create_top_products_chart(df):

    products = (
        df.groupby("ProductName", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(10)
    )

    fig = px.bar(
        products,
        x="Sales",
        y="ProductName",
        orientation="h",
        color="Sales",
        color_continuous_scale="Viridis",
        text_auto=","
    )

    fig.update_layout(
        coloraxis_showscale=False
    )

    fig.update_traces(
        textposition="outside",
        hovertemplate=
        "<b>%{y}</b><br>"
        "Sales: %{x:,}<extra></extra>"
    )

    fig.update_yaxes(
        categoryorder="total ascending"
    )

    style_chart(
        fig,
        "Top 10 Products by Sales",
        "Sales",
        ""
    )

    return fig


# ==========================================================
# Top 10 Cities by Sales
# ==========================================================

def create_top_cities_chart(df):

    cities = (
        df.groupby("CityName", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(10)
    )

    fig = px.bar(
        cities,
        x="Sales",
        y="CityName",
        orientation="h",
        color="Sales",
        color_continuous_scale="Teal",
        text_auto=","
    )

    fig.update_layout(
        coloraxis_showscale=False
    )

    fig.update_traces(
        textposition="outside",
        hovertemplate=
        "<b>%{y}</b><br>"
        "Sales: %{x:,}<extra></extra>"
    )

    fig.update_yaxes(
        categoryorder="total ascending"
    )

    style_chart(
        fig,
        "Top 10 Cities by Sales",
        "Sales",
        ""
    )

    return fig


# ==========================================================
# Sales vs Rating
# ==========================================================

def create_sales_rating_chart(df):

    fig = px.scatter(
        df,
        x="Rating",
        y="Sales",
        color="Category",
        size="Sales",
        hover_name="ProductName",
        opacity=0.80,
        color_discrete_sequence=CATEGORY_COLORS
    )

    fig.update_traces(

        marker=dict(
            line=dict(
                width=1,
                color="white"
            )
        ),

        hovertemplate=
        "<b>%{hovertext}</b><br>"
        "Rating: %{x:.1f}<br>"
        "Sales: %{y:,}<extra></extra>"
    )

    style_chart(
        fig,
        "Sales vs Product Rating",
        "Rating",
        "Sales",
        legend=True,
        height=600
    )

    return fig


# ==========================================================
# Discount vs Revenue
# ==========================================================

def create_discount_revenue_chart(df):

    fig = px.scatter(
        df,
        x="Discount",
        y="Revenue",
        color="Category",
        size="Sales",
        opacity=0.75,
        color_discrete_sequence=CATEGORY_COLORS
    )

    fig.update_traces(

        marker=dict(
            line=dict(
                width=1,
                color="white"
            )
        ),

        hovertemplate=
        "Discount: %{x:.0%}<br>"
        "Revenue: $%{y:,.2f}<extra></extra>"
    )

    style_chart(
        fig,
        "Discount vs Revenue",
        "Discount",
        "Revenue",
        legend=True,
        height=600
    )

    return fig


# ==========================================================
# Stock by Category
# ==========================================================

def create_stock_chart(df):

    stock = (
        df.groupby("Category", as_index=False)["StockQuantity"]
        .sum()
        .sort_values("StockQuantity", ascending=False)
    )

    fig = px.bar(
        stock,
        x="Category",
        y="StockQuantity",
        color="Category",
        color_discrete_sequence=CATEGORY_COLORS,
        text_auto=","
    )

    fig.update_traces(
        textposition="outside",
        hovertemplate=
        "<b>%{x}</b><br>"
        "Stock: %{y:,}<extra></extra>"
    )

    style_chart(
        fig,
        "Available Stock by Category",
        "Category",
        "Stock Quantity"
    )

    return fig


# ==========================================================
# Rating Distribution
# ==========================================================

def create_rating_distribution_chart(df):

    fig = px.histogram(
        df,
        x="Rating",
        nbins=20,
        color_discrete_sequence=[COLORS["warning"]]
    )

    fig.update_traces(
        hovertemplate=
        "Rating: %{x}<br>"
        "Count: %{y}<extra></extra>"
    )

    style_chart(
        fig,
        "Product Rating Distribution",
        "Rating",
        "Frequency"
    )

    return fig


# ==========================================================
# Correlation Heatmap
# ==========================================================

def create_correlation_heatmap(df):

    corr = df[
        [
            "Price",
            "Sales",
            "Revenue",
            "Discount",
            "Rating",
            "StockQuantity",
            "NumReviews"
        ]
    ].corr()

    fig = px.imshow(
        corr,
        text_auto=".2f",
        color_continuous_scale="RdBu_r",
        aspect="auto"
    )

    fig.update_layout(

        template="plotly_white",

        title=dict(
            text="Correlation Matrix",
            x=0.5,
            font=dict(
                size=22,
                color=COLORS["text"]
            )
        ),

        paper_bgcolor="white",
        plot_bgcolor="white",

        font=dict(
            family="Arial",
            size=13,
            color=COLORS["text"]
        ),

        margin=dict(
            l=40,
            r=40,
            t=70,
            b=40
        ),

        height=650
    )

    return fig

    