import plotly.graph_objects as go

years = [2018, 2019, 2020, 2021, 2022]
sales = [100, 150, 130, 170, 180]
profit = [20, 30, 25, 35, 40]

fig = go.Figure()
fig.add_trace(go.Scatter(x=years, y=sales, mode='lines+markers', name='Sales'))
fig.add_trace(go.Scatter(x=years, y=profit, mode='lines+markers', name='Profit'))

fig.update_layout(title="Sales and Profit Over Time", xaxis_title="Year", yaxis_title="Value")
fig.show()