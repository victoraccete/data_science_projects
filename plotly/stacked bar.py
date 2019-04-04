# -*- coding: utf-8 -*-
import plotly.graph_objs as go
import plotly.offline

tracebr = go.Bar(
    x=['1980', '2017'],
    y=[0.235, 2.056],
    name='Brasil',
    marker=dict(
        color='rgb(40,200,40)'),
)
traceus = go.Bar(
    x=['1980', '2017'],
    y=[2.768, 19.390],
    name='EUA',
    marker=dict(
        color='rgb(40,40,200)'),
)

tracech = go.Bar(
    x=['1980', '2017'],
    y=[0.189, 12.2400],
    name='China',
    marker=dict(
        color='rgb(200,40,40)'),
)

data = [tracebr, traceus, tracech]
layout = go.Layout(
    barmode='group',
    title='PIB em trilhões (1980 x 2017)'
)

fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='bar.html')
