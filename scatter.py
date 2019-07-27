import pandas as pd
import matplotlib.pyplot as plt

import plotly
import plotly.graph_objs as go

data = pd.read_csv('train.csv')

# Create a trace
trace = go.Scatter(
    x = data['YearBuilt'],
    y = data['SalePrice'],
    mode = 'markers',
    showlegend = True
)
plot_data = [trace]

# Plot and embed in ipython notebook!
plotly.offline.plot(plot_data, filename='basic-scatter')