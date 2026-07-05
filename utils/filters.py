import pandas as pd
import streamlit as st


def apply_filters(df: pd.DataFrame) -> pd.DataFrame:
    """
    Apply interactive Streamlit filters to the dataset.

    This function creates a sidebar filter panel similar to Power BI slicers.

    Parameters
    ----------
    df : pd.DataFrame
        Enriched dataset from loader.load_data()

    Returns
    -------
    pd.DataFrame
        Filtered dataset based on user selection
    """

    if df is None or df.empty:
        return df

    filtered_df = df.copy()

    st.sidebar.header("🔎 Filters")

    # ----------------------------
    # CITY FILTER
    # ----------------------------
    city_col_candidates = ["City", "city", "CityName", "city_name"]
    city_col = next((c for c in city_col_candidates if c in filtered_df.columns), None)

    if city_col:
        cities = sorted(filtered_df[city_col].dropna().unique().tolist())
        selected_cities = st.sidebar.multiselect(
            "City",
            options=cities,
            default=cities
        )

        filtered_df = filtered_df[filtered_df[city_col].isin(selected_cities)]

    # ----------------------------
    # PRODUCT FILTER
    # ----------------------------
    product_col_candidates = ["Product", "product", "ProductName", "product_name"]
    product_col = next((c for c in product_col_candidates if c in filtered_df.columns), None)

    if product_col:
        products = sorted(filtered_df[product_col].dropna().unique().tolist())
        selected_products = st.sidebar.multiselect(
            "Product",
            options=products,
            default=products
        )

        filtered_df = filtered_df[filtered_df[product_col].isin(selected_products)]

    # ----------------------------
    # DATE FILTER
    # ----------------------------
    date_col_candidates = ["Date", "date", "OrderDate", "order_date"]
    date_col = next((c for c in date_col_candidates if c in filtered_df.columns), None)

    if date_col:
        filtered_df[date_col] = pd.to_datetime(filtered_df[date_col], errors="coerce")

        min_date = filtered_df[date_col].min()
        max_date = filtered_df[date_col].max()

        if pd.notnull(min_date) and pd.notnull(max_date):
            date_range = st.sidebar.date_input(
                "Date Range",
                value=(min_date, max_date),
                min_value=min_date,
                max_value=max_date
            )

            if isinstance(date_range, tuple) and len(date_range) == 2:
                start_date, end_date = date_range

                filtered_df = filtered_df[
                    (filtered_df[date_col] >= pd.to_datetime(start_date)) &
                    (filtered_df[date_col] <= pd.to_datetime(end_date))
                ]

    # ----------------------------
    # SAFETY CLEANUP
    # ----------------------------
    filtered_df = filtered_df.dropna(how="all")

    return filtered_df
    