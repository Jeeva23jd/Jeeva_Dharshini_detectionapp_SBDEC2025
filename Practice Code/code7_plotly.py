import plotly.express as px

data = {
    "Department": ["HR", "IT", "Finance", "IT", "HR", "Finance"],
    "Salary": [40, 60, 55, 70, 45, 65]
}

fig = px.box(data, x="Department", y="Salary", title="Salary Distribution by Department")
fig.show()