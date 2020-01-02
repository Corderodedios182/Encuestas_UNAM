#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 22:13:28 2020

@author: carlos
"""

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import matplotlib.pyplot as plt

##############
#PlotlyBasics#
##############

####basic1

df = pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
df.plot()
plt.show()

####basic2

pyo.plot([{
    'x': df.index,
    'y': df[col],
    'name': col
} for col in df.columns])

##############
#ScatterPLots#
##############

####scatter1

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',
)]

pyo.plot(data, filename='scatter1.html')

####scatter2

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',
)]
layout = go.Layout(
    title = 'Random Data Scatterplot', # Graph title
    xaxis = dict(title = 'Some random x-values'), # x-axis label
    yaxis = dict(title = 'Some random y-values'), # y-axis label
    hovermode ='closest' # handles multiple points landing on the same vertical
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter2.html')

####scatter3

np.random.seed(42)
random_x = np.random.randint(1,101,100)
random_y = np.random.randint(1,101,100)

data = [go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers',
    marker = dict(      # change the marker style
        size = 12,
        color = 'rgb(51,204,153)',
        symbol = 'pentagon',
        line = dict(
            width = 2,
        )
    )
)]
layout = go.Layout(
    title = 'Random Data Scatterplot', # Graph title
    xaxis = dict(title = 'Some random x-values'), # x-axis label
    yaxis = dict(title = 'Some random y-values'), # y-axis label
    hovermode ='closest' # handles multiple points landing on the same vertical
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter3.html')

############
#LineCharts#
############

####line1

np.random.seed(56)
x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

trace_0 = go.Scatter(
    x = x_values, 
    y = y_values + 5,
    mode = 'markers', 
    name = 'markers')

trace_1 = go.Scatter(
    x = x_values,
    y = y_values,
    mode = 'lines', 
    name = 'mylines')

trace_2 = go.Scatter(
    x = x_values,
    y = y_values - 5,
    mode = 'lines+markers',
    name = 'my favorite')


data = [trace_0, trace_1, trace_2]

layout = go.Layout(
    title = 'Line chart showing three different modes')

fig = go.Figure(data = data, layout = layout)
pyo.plot(fig, filename = 'line1.html')

####line2

df = pd.read_csv('https://www2.census.gov/programs-surveys/popest/datasets/2010-2017/national/totals/nst-est2017-alldata.csv')

# grab just the six New England states:
df2 = df[df['DIVISION']=='1']
# set the index to state name:
df2.set_index('NAME', inplace=True)
# grab just the population columns:
df2 = df2[[col for col in df2.columns if col.startswith('POP')]]

traces=[go.Scatter(
    x = df2.columns,
    y = df2.loc[name],
    mode = 'markers+lines',
    name = name
) for name in df2.index]

layout = go.Layout(
    title = 'Population Estimates of the Six New England States'
)

fig = go.Figure(data=traces,layout=layout)
pyo.plot(fig, filename='line2.html')

####Sol2a-Linechart

df = pd.read_csv('/home/carlos/Documentos/Plotly/Data/2010YumaAZ.csv')

days = ['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']

# Use a for loop to create the traces for the seven days
# There are many ways to do this! Could also do this with a
# list comprehension.

data = []

for day in days:
    trace = go.Scatter(x=df['LST_TIME'],
                       y=df[df['DAY']==day]['T_HR_AVG'],
                       mode='lines',
                       name=day)
    data.append(trace)

layout = go.Layout(
    title='Daily temperatures from June 1-7, 2010 in Yuma, Arizona',
    hovermode='closest'
)

# Create a fig from data and layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution2a.html')

###########
#BarCharts#
###########

####bar1

df = pd.read_csv('/home/carlos/Documentos/Plotly/Data/2018WinterOlympics.csv')

data = [go.Bar(
    x=df['NOC'],  # NOC stands for National Olympic Committee
    y=df['Total']
)]

layout = go.Layout(
    title='2018 Winter Olympic Medals by Country'
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar1.html')

#bar2

trace1 = go.Bar(
    x=df['NOC'],  # NOC stands for National Olympic Committee
    y=df['Gold'],
    name = 'Gold',
    marker=dict(color='#FFD700') # set the marker color to gold
)
trace2 = go.Bar(
    x=df['NOC'],
    y=df['Silver'],
    name='Silver',
    marker=dict(color='#9EA0A1') # set the marker color to silver
)
trace3 = go.Bar(
    x=df['NOC'],
    y=df['Bronze'],
    name='Bronze',
    marker=dict(color='#CD7F32') # set the marker color to bronze
)

data = [trace1, trace2, trace3]

layout = go.Layout(
    title='2018 Winter Olympic Medals by Country'
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar2.html')

####bar3

layout = go.Layout(
    title='2018 Winter Olympic Medals by Country',
    barmode='stack'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bar3.html')

####Sol3a-Barchart

df = pd.read_csv('/home/carlos/Documentos/Plotly/Data/mocksurvey.csv',index_col=0)

# create traces using a list comprehension:
data = [go.Bar(
    x = df.index,
    y = df[response],
    name=response
) for response in df.columns]

# create a layout, remember to set the barmode here
layout = go.Layout(
    title='Mock Survey Results',
    barmode='stack'
)

# create a fig from data & layout, and plot the fig
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution3a.html')

####Sol3b-Barchart

data = [go.Bar(
    y = df.index,     # reverse your x- and y-axis assignments
    x = df[response],
    orientation='h',  # this line makes it horizontal!
    name=response
) for response in df.columns]

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='solution3b.html')

##############
#BubbleCharts#
##############

####bubble1

df = pd.read_csv('/home/carlos/Documentos/Plotly/Data/mpg.csv')

data = [go.Scatter(          # start with a normal scatter plot
    x=df['horsepower'],
    y=df['mpg'],
    text=df['name'],
    mode='markers',
    marker=dict(size=1.5*df['cylinders']) # set the marker size
)]

layout = go.Layout(
    title='Vehicle mpg vs. horsepower',
    xaxis = dict(title = 'horsepower'), # x-axis label
    yaxis = dict(title = 'mpg'),        # y-axis label
    hovermode='closest'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble1.html')

####bubble2

df['text1']=pd.Series(df['model_year'],dtype=str)
df['text2']="'"+df['text1']+" "+df['name']

data = [go.Scatter(
            x=df['horsepower'],
            y=df['mpg'],
            text=df['text2'],  # use the new column for the hover text
            mode='markers',
            marker=dict(size=1.5*df['cylinders'])
    )]
layout = go.Layout(
    title='Vehicle mpg vs. horsepower',
    hovermode='closest'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='bubble2.html')

##########
#Heatmaps#
##########

####heat1

df = pd.read_csv('/home/carlos/Documentos/Plotly/Data/2010SantaBarbaraCA.csv')

data = [go.Heatmap(
    x=df['DAY'],
    y=df['LST_TIME'],
    z=df['T_HR_AVG'],
    colorscale='Jet'
)]

layout = go.Layout(
    title='Hourly Temperatures, June 1-7, 2010 in<br>\
    Santa Barbara, CA USA'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Santa_Barbara.html')

####heat2

df = pd.read_csv('/home/carlos/Documentos/Plotly/Data/2010YumaAZ.csv')

data = [go.Heatmap(
    x=df['DAY'],
    y=df['LST_TIME'],
    z=df['T_HR_AVG'],
    colorscale='Jet'
)]

layout = go.Layout(
    title='Hourly Temperatures, June 1-7, 2010 in<br>\
    Yuma, AZ USA'
)
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Yuma.html')





