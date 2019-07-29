import plotly as plt
import csv
import pandas as pd

df = pd.read_csv('improvement.csv')

data = [{'type': 'bar', 'x': df['Name'], 'y': df['AVG Improvement'], 'marker': {'color': 'rgb(60, 100, 150)', 'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}}, 'opacity': 0.6, }]
layout = {'title': 'Most Improved OPS over career (on average)', 'titlefont': {'size':28, 'color': 'rgb(46,84,101)'},'xaxis': {'title': 'Player', 'titlefont': {'size': 24}, 'tickfont': {'size': 14}}, 'yaxis': {'title': 'Avg OPS improvement (by %)', 'titlefont': {'size': 24}, 'tickfont': {'size': 14}},}

fig = {'data': data, 'layout': layout}
plt.offline.plot(fig, filename= 'OPS_viz.html')