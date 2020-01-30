#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 23:17:03 2020

@author: carlos
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash()

encuestas = pd.read_csv('/home/carlos/Documentos/Encuestas_UNAM/encuestas.csv')

#General
conteo = encuestas.Facultad.value_counts().reset_index()
conteo['encuestados'] = conteo.Facultad/12
conteo.columns = ['Facultad','Conteo','encuestados']

#Opciones boton
Facultades_0 = conteo.loc[:,'Facultad']
Facultades = [{'label':i,'value':i} for i in Facultades_0]

def app_layout():
    return(
            html.Div([
                    dcc.Dropdown(id = 'tabs', 
                     options = Facultades,
                     value = "all",
                     clearable=False),
                    html.Div(id='output-tab')
                    ])
    )

app.layout = app_layout()

@app.callback(Output('output-tab', 'children'),
              [Input('tabs', 'value')])

def display_content(value):
    
    Pregunta_1 = encuestas.loc[(encuestas.Pregunta == 1) & (encuestas.Facultad == value),'Respuesta_texto'].value_counts().reset_index()

    trace_1 = go.Pie(labels=Pregunta_1.loc[:,'index'], values=Pregunta_1.loc[:,'Respuesta_texto'])
    layout_1 =  go.Layout(legend = {"x":0,"y":-.5},  margin=dict(l=23,r=18,b=53,t=73,),paper_bgcolor='rgb(223, 223, 223)', template = 'ggplot2')
                    
    fig_1 = go.Figure(data = [trace_1], layout = layout_1)    
    
    return html.Div([ dcc.Graph( id='graph', figure = fig_1) ])

if __name__ == '__main__':
    app.server.run()