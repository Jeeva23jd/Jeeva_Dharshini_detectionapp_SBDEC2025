import plotly.express as px

data = {
    "Fruit": ["Apple", "Banana", "Grapes", "Orange"],
    "Quantity": [30, 15, 25, 20]
}

fig = px.pie(data, names="Fruit", values="Quantity", title="Fruit Market Share")
fig.show()