#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 00:08:27 2020

@author: carlos
"""

# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objects as go


#####################
#1 Inicio aplicación#
#####################

app = dash.Dash()

####################
#2 Importando datos#
####################

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')

#Opciones de boton
features = df.columns[1:-1]
opts = [{'label' : i, 'value' : i} for i in features]

#Opciones deslizantes
df['Date'] = pd.to_datetime(df.Date)

dates = ['2015-02-17', '2015-05-17', '2015-08-17', '2015-11-17',
         '2016-02-17', '2016-05-17', '2016-08-17', '2016-11-17',  
         '2017-02-17']
date_mark = {i : dates[i] for i in range(0, 9)}

######################
#3 Creando el grafico#
######################

trace_1 = go.Scatter(x = df.Date, y = df['AAPL.High'],
                    name = 'AAPL HIGH',
                    line = dict(width = 2,
                                color = 'rgb(229, 151, 50)'))

layout = go.Layout(title = 'Time Series Plot',
                   hovermode = 'closest')

fig = go.Figure(data = [trace_1], layout = layout)

########################
#4 Creacion Dash Layout#
########################

app.layout = html.Div([
    html.Div([
    html.H1(children='Resultados Encuestas Derecho Animal UNAM'),
    html.P(children='Se realizaron 2000 encuestas en diversas Facultades')
            ],
        style = {'padding' : '40px' ,
                 'backgroundColor' : '#3aaab2'})
    ,
    #Figura creada
    dcc.Graph(
        id='plot',
        figure = fig
    ),
    
    #Boton desplegable
    html.P([
        html.Label("Choose a feature"),
        dcc.Dropdown(id = 'opt', 
                     options = opts,
                     value = opts[0])],
        style = {'width': '400px',
                 'fontSize' : '20px',
                 'padding-left' : '100px',
                 'display': 'inline-block'}),
    #Rango de fechas
    html.P([
        html.Label("Time Period"),
        dcc.RangeSlider(id = 'slider',
                        marks = date_mark,
                        min = 0,
                        max = 8,
                        value = [1, 7]) 
        ], style = {'width' : '80%',
                    'fontSize' : '20px',
                    'padding-left' : '100px',
                    'display': 'inline-block'})
    ])

##########################        
#5 Funciones desplegables#
##########################

@app.callback(Output('plot', 'figure'),
             [Input('opt', 'value'),
             Input('slider', 'value')])

def update_figure(input1, input2):
    # filtering the data
    st2 = df[(df.Date > dates[input2[0]]) & (df.Date < dates[input2[1]])]
    # updating the plot
    trace_1 = go.Scatter(x = st2.Date, y = st2['AAPL.High'],
                        name = 'AAPL HIGH',
                        line = dict(width = 2,
                                    color = 'rgb(229, 151, 50)'))
    trace_2 = go.Scatter(x = st2.Date, y = st2[input1],
                        name = input1,
                        line = dict(width = 2,
                                    color = 'rgb(106, 181, 135)'))
    fig = go.Figure(data = [trace_1, trace_2], layout = layout)
    return fig
    

#############
#6 Ejecucion#
#############
if __name__ == '__main__':
    app.run_server()