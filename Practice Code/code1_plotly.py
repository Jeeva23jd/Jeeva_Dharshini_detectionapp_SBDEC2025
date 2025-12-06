import plotly.express as px

data = {
    "Year": [2018, 2019, 2020, 2021, 2022],
    "Sales": [100, 150, 130, 170, 180]
}

fig = px.line(data, x="Year", y="Sales", title="Sales Growth Over Years")
fig.show()