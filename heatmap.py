import plotly
import plotly.graph_objs as go

import pandas as pd

data = pd.read_csv('train.csv')

corrmat = data.corr()

trace = go.Heatmap(z=corrmat, x=corrmat.columns.tolist(), y=corrmat.columns.tolist())

plot_data = [trace]

plotly.offline.plot(plot_data, filename='basic-heatmap')