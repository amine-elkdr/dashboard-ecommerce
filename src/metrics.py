def get_kpis(df):
    total_revenue = df["Revenue"].sum()
    total_orders = df["InvoiceNo"].nunique()
    avg_basket = total_revenue / total_orders
    total_customers = df["CustomerID"].nunique()

    return {
        "total_revenue": round(total_revenue, 2),
        "total_orders": total_orders,
        "avg_basket": round(avg_basket, 2),
        "total_customers": total_customers
    }

def get_revenue_by_month(df):
    return df.groupby("Month")["Revenue"].sum().reset_index()

def get_top_products(df, n=10):
    return (
        df.groupby("Description")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )

def get_top_countries(df, n=10):
    return (
        df.groupby("Country")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )

def get_kpis(df):
    total_revenue = df["Revenue"].sum()
    total_orders = df["InvoiceNo"].nunique()
    avg_basket = total_revenue / total_orders
    total_customers = df["CustomerID"].nunique()

    return {
        "total_revenue": round(total_revenue, 2),
        "total_orders": total_orders,
        "avg_basket": round(avg_basket, 2),
        "total_customers": total_customers
    }

def get_revenue_by_month(df):
    return df.groupby("Month")["Revenue"].sum().reset_index()

def get_top_products(df, n=10):
    return (
        df.groupby("Description")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )

def get_top_countries(df, n=10):
    return (
        df.groupby("Country")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )

def get_retention(df):
    orders_per_customer = df.groupby("CustomerID")["InvoiceNo"].nunique()
    new = (orders_per_customer == 1).sum()
    returning = (orders_per_customer > 1).sum()
    return {"new_customers": int(new), "returning_customers": int(returning)}

def get_orders_by_month(df):
    return df.groupby("Month")["InvoiceNo"].nunique().reset_index()

def get_avg_basket_by_month(df):
    revenue = df.groupby("Month")["Revenue"].sum()
    orders = df.groupby("Month")["InvoiceNo"].nunique()
    result = (revenue / orders).reset_index()
    result.columns = ["Month", "AvgBasket"]
    return result

def get_top_customers(df, n=10):
    return (
        df.groupby("CustomerID")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(n)
        .reset_index()
    )

def get_revenue_by_weekday(df):
    df = df.copy()
    df["Weekday"] = df["InvoiceDate"].dt.day_name()
    order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    result = df.groupby("Weekday")["Revenue"].sum().reindex(order).reset_index()
    return result