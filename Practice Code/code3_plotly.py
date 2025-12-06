import plotly.express as px

data = {
    "Category": ["A", "B", "C", "D"],
    "Revenue": [120, 300, 180, 250]
}

fig = px.bar(data, x="Category", y="Revenue", title="Revenue by Category", color="Category")
fig.show()