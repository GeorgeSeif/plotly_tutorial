import plotly
import plotly.graph_objs as go

import pandas as pd

data = pd.read_csv('train.csv')

trace = go.Box(
    x = data['YearBuilt'],
    y = data['SalePrice'],
    marker = {'color': 'green'},
    showlegend = True,
)
plot_data = [trace]

plotly.offline.plot(plot_data, filename='basic-box')