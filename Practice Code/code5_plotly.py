import plotly.express as px

data = {
    "Country": ["India", "USA", "Canada", "Germany", "Australia"],
    "GDP": [3.7, 25.5, 2.2, 4.9, 1.8]
}

fig = px.choropleth(data, locations="Country", locationmode="country names",
                    color="GDP", title="World GDP (Trillions USD)",
                    color_continuous_scale="Viridis")
fig.show()