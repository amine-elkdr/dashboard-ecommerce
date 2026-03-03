import plotly.express as px

def chart_revenue_by_month(df_month):
    fig = px.line(
        df_month,
        x="Month",
        y="Revenue",
        title="Chiffre d'affaires mensuel",
        markers=True,
        labels={"Revenue": "Revenu (£)", "Month": "Mois"}
    )
    fig.update_layout(template="plotly_dark")
    return fig

def chart_top_products(df_products):
    fig = px.bar(
        df_products,
        x="Revenue",
        y="Description",
        orientation="h",
        title="Top 10 produits par revenu",
        labels={"Revenue": "Revenu (£)", "Description": "Produit"}
    )
    fig.update_layout(template="plotly_dark", yaxis=dict(autorange="reversed"))
    return fig

def chart_top_countries(df_countries):
    fig = px.bar(
        df_countries,
        x="Country",
        y="Revenue",
        title="Top 10 pays par revenu",
        labels={"Revenue": "Revenu (£)", "Country": "Pays"}
    )
    fig.update_layout(template="plotly_dark")
    return fig


def chart_revenue_by_month(df_month):
    fig = px.line(df_month, x="Month", y="Revenue", title="CA mensuel", markers=True,
                  labels={"Revenue": "Revenu (£)", "Month": "Mois"})
    fig.update_layout(template="plotly_dark")
    return fig

def chart_top_products(df_products):
    fig = px.bar(df_products, x="Revenue", y="Description", orientation="h",
                 title="Top 10 produits", labels={"Revenue": "Revenu (£)", "Description": "Produit"})
    fig.update_layout(template="plotly_dark", yaxis=dict(autorange="reversed"))
    return fig

def chart_top_countries(df_countries):
    fig = px.bar(df_countries, x="Country", y="Revenue", title="Top 10 pays",
                 labels={"Revenue": "Revenu (£)", "Country": "Pays"})
    fig.update_layout(template="plotly_dark")
    return fig

def chart_world_map(df_countries_all):
    fig = px.choropleth(df_countries_all, locations="Country", locationmode="country names",
                        color="Revenue", title="Revenu par pays",
                        color_continuous_scale="Blues")
    fig.update_layout(template="plotly_dark")
    return fig

def chart_retention(retention):
    import plotly.graph_objects as go
    fig = go.Figure(go.Pie(
        labels=["Nouveaux clients", "Clients récurrents"],
        values=[retention["new_customers"], retention["returning_customers"]],
        hole=0.4
    ))
    fig.update_layout(title="Nouveaux vs Récurrents", template="plotly_dark")
    return fig

def chart_orders_by_month(df_orders):
    fig = px.bar(df_orders, x="Month", y="InvoiceNo", title="Commandes par mois",
                 labels={"InvoiceNo": "Nb commandes", "Month": "Mois"})
    fig.update_layout(template="plotly_dark")
    return fig

def chart_avg_basket_by_month(df_avg):
    fig = px.line(df_avg, x="Month", y="AvgBasket", title="Panier moyen par mois",
                  markers=True, labels={"AvgBasket": "Panier moyen (£)", "Month": "Mois"})
    fig.update_layout(template="plotly_dark")
    return fig

def chart_top_customers(df_customers):
    df_customers["CustomerID"] = df_customers["CustomerID"].astype(str)
    fig = px.bar(df_customers, x="Revenue", y="CustomerID", orientation="h",
                 title="Top 10 clients", labels={"Revenue": "Revenu (£)", "CustomerID": "Client"})
    fig.update_layout(template="plotly_dark", yaxis=dict(autorange="reversed"))
    return fig

def chart_revenue_by_weekday(df_weekday):
    fig = px.bar(df_weekday, x="Weekday", y="Revenue", title="Revenu par jour de la semaine",
                 labels={"Revenue": "Revenu (£)", "Weekday": "Jour"})
    fig.update_layout(template="plotly_dark")
    return fig

def chart_heatmap(df):
    import pandas as pd
    df = df.copy()
    df["Hour"] = df["InvoiceDate"].dt.hour
    df["Weekday"] = df["InvoiceDate"].dt.day_name()
    order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    pivot = df.groupby(["Weekday","Hour"])["InvoiceNo"].nunique().unstack().reindex(order)
    fig = px.imshow(pivot, title="Heatmap commandes par jour/heure",
                    labels={"x": "Heure", "y": "Jour", "color": "Nb commandes"},
                    color_continuous_scale="Blues")
    fig.update_layout(template="plotly_dark")
    return fig

def chart_scatter(df):
    sample = df.sample(2000, random_state=42)
    fig = px.scatter(sample, x="UnitPrice", y="Quantity", title="Quantité vs Prix unitaire",
                     opacity=0.5, labels={"UnitPrice": "Prix (£)", "Quantity": "Quantité"})
    fig.update_layout(template="plotly_dark")
    return fig