# -*- coding: utf-8 -*-
import plotly.figure_factory as ff
import pandas as pd
import plotly.offline


df = pd.read_csv('C:/Users/Victor/data_science_projects/plotly/band_members.csv')

colors = dict(Vocals = 'rgb(190, 30, 30)',
              Keyboards = 'rgb(30, 190, 30)',
              Drums = 'rgb(30, 30, 190)',
              Bass = 'rgb(190, 30, 190)', 
              Guitar = 'rgb(190, 190, 30)')


df.Start = pd.to_datetime(df.Start, format='%Y')
df.Finish = pd.to_datetime(df.Finish, format='%Y')

df = df.rename(columns={"Name": "Task"})

fig = ff.create_gantt(df, colors=colors, index_col='Role', show_colorbar=True,
                      bar_width=0.4, showgrid_x=True, showgrid_y=True, 
                      title='Membros Blind Guardian (1984-2019)')

plotly.offline.plot(fig)
