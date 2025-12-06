import plotly.express as px
import numpy as np

z = np.random.rand(5, 5)
fig = px.imshow(z, text_auto=True, color_continuous_scale="Plasma", title="Random Heatmap")
fig.show()