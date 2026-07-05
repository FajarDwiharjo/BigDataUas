import pandas as pd
import streamlit as st
from pathlib import Path


DATA_PATH = Path("data")


@st.cache_data
def load_data():
    """
    Load all e-commerce datasets and build an enriched fact table.

    Returns
    -------
    dict
        {
            "fact_raw": original fact table,
            "dim_city": city dimension,
            "dim_date": date dimension,
            "dim_product": product dimension,
            "fact_enriched": merged fact table with all dimensions
        }
    """

    # ----------------------------
    # Load CSV files
    # ----------------------------
    dim_city = pd.read_csv(DATA_PATH / "dim_city.csv")
    dim_date = pd.read_csv(DATA_PATH / "dim_date.csv")
    dim_product = pd.read_csv(DATA_PATH / "dim_product.csv")
    fact = pd.read_csv(DATA_PATH / "fact_product_sales.csv")

    # ----------------------------
    # Basic cleaning (safe defaults)
    # ----------------------------
    dim_city.columns = dim_city.columns.str.strip()
    dim_date.columns = dim_date.columns.str.strip()
    dim_product.columns = dim_product.columns.str.strip()
    fact.columns = fact.columns.str.strip()

    # Try parse date if possible
    date_col_candidates = ["Date", "date", "OrderDate", "order_date"]
    for col in date_col_candidates:
        if col in dim_date.columns:
            dim_date[col] = pd.to_datetime(dim_date[col], errors="coerce")

    # ----------------------------
    # Merge logic (star schema style)
    # ----------------------------

    fact_enriched = fact.copy()

    # Merge with product dimension
    if "ProductKey" in fact_enriched.columns and "ProductKey" in dim_product.columns:
        fact_enriched = fact_enriched.merge(dim_product, on="ProductKey", how="left")

    # Merge with city dimension
    if "CityKey" in fact_enriched.columns and "CityKey" in dim_city.columns:
        fact_enriched = fact_enriched.merge(dim_city, on="CityKey", how="left")

    # Merge with date dimension
    if "DateKey" in fact_enriched.columns and "DateKey" in dim_date.columns:
        fact_enriched = fact_enriched.merge(dim_date, on="DateKey", how="left")

    # ----------------------------
    # Final cleanup
    # ----------------------------
    fact_enriched.columns = fact_enriched.columns.str.strip()

    return {
        "fact_raw": fact,
        "dim_city": dim_city,
        "dim_date": dim_date,
        "dim_product": dim_product,
        "fact_enriched": fact_enriched,
    }