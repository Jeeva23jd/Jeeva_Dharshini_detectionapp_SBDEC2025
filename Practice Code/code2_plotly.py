import plotly.express as px

data = {
    "Height": [150, 160, 170, 180, 190],
    "Weight": [55, 60, 70, 80, 90],
    "Gender": ["F", "F", "M", "M", "M"]
}

fig = px.scatter(data, x="Height", y="Weight", color="Gender", title="Height vs Weight by Gender")
fig.show()