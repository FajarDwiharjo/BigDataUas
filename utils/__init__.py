"""
Utils package for E-Commerce Streamlit Dashboard.

This package provides modular components for:
- Data loading from CSV sources (loader)
- Filtering logic for dashboard interaction (filters)
- KPI/metrics computation (metrics)
- Plotly-based visualizations (charts)
- UI styling and theme configuration (style)

Data Sources:
- data/dim_city.csv
- data/dim_date.csv
- data/dim_product.csv
- data/fact_product_sales.csv
"""

from .loader import load_data
from .filters import apply_filters
from .metrics import calculate_metrics
from .charts import (
    create_sales_trend_chart,
    create_category_sales_chart,
    create_city_sales_chart,
    create_top_products_chart
)
from .style import apply_style

__all__ = [
    "load_data",
    "apply_filters",
    "calculate_metrics",
    "create_sales_trend_chart",
    "create_category_sales_chart",
    "create_city_sales_chart",
    "create_top_products_chart",
    "apply_style",
]
