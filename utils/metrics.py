import pandas as pd


def calculate_metrics(df: pd.DataFrame) -> dict:
    """
    Calculate dashboard KPI metrics.

    Parameters
    ----------
    df : pd.DataFrame
        Filtered dataset.

    Returns
    -------
    dict
        Dictionary containing KPI values.
    """

    if df is None or df.empty:
        return {
            "total_sales": 0,
            "total_orders": 0,
            "total_quantity": 0,
            "avg_order_value": 0.0,
        }

    # ----------------------------
    # Detect columns automatically
    # ----------------------------

    sales_col = next(
        (
            c
            for c in [
                "Sales",
                "sales",
                "Revenue",
                "revenue",
                "TotalSales",
                "amount",
            ]
            if c in df.columns
        ),
        None,
    )

    quantity_col = next(
        (
            c
            for c in [
                "Quantity",
                "quantity",
                "Qty",
                "qty",
            ]
            if c in df.columns
        ),
        None,
    )

    order_col = next(
        (
            c
            for c in [
                "OrderID",
                "OrderId",
                "OrderKey",
                "InvoiceID",
                "InvoiceNo",
            ]
            if c in df.columns
        ),
        None,
    )

    total_sales = (
        float(df[sales_col].sum())
        if sales_col
        else 0.0
    )

    total_quantity = (
        int(df[quantity_col].sum())
        if quantity_col
        else 0
    )

    if order_col:
        total_orders = int(df[order_col].nunique())
    else:
        total_orders = len(df)

    avg_order_value = (
        total_sales / total_orders
        if total_orders > 0
        else 0.0
    )

    return {
        "total_sales": total_sales,
        "total_orders": total_orders,
        "total_quantity": total_quantity,
        "avg_order_value": avg_order_value,
    }
