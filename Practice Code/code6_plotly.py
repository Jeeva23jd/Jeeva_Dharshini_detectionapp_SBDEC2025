import plotly.express as px
import numpy as np

data = np.random.randn(500)

fig = px.histogram(data, nbins=20, title="Random Data Distribution")
fig.show()