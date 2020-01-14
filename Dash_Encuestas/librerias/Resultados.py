#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 23:47:18 2020

@author: carlos
"""
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from utilsv0 import Header
####################
#2 Importando datos#
####################

encuestas = pd.read_csv('/home/carlos/Documentos/Encuestas_UNAM/Dash_Encuestas/datos/encuestas.csv')

#General
Pregunta_1 = encuestas.loc[encuestas.Pregunta == 1,'Respuesta_texto'].value_counts().reset_index()
Pregunta_2 = encuestas.loc[encuestas.Pregunta == 2,'Respuesta_texto'].value_counts().reset_index()
Pregunta_3 = encuestas.loc[encuestas.Pregunta == 3,'Respuesta_texto'].value_counts().reset_index()
Pregunta_4 = encuestas.loc[encuestas.Pregunta == 4,'Respuesta_texto'].value_counts().reset_index()

Pregunta_5 = encuestas.loc[encuestas.Pregunta == 5,'Respuesta_texto'].value_counts().reset_index()
Pregunta_6 = encuestas.loc[encuestas.Pregunta == 6,'Respuesta_texto'].value_counts().reset_index()
Pregunta_7 = encuestas.loc[encuestas.Pregunta == 7,'Respuesta_texto'].value_counts().reset_index()
Pregunta_8 = encuestas.loc[encuestas.Pregunta == 8,'Respuesta_texto'].value_counts().reset_index()

Pregunta_9 = encuestas.loc[encuestas.Pregunta == 9,'Respuesta_texto'].value_counts().reset_index()
Pregunta_10 = encuestas.loc[encuestas.Pregunta == 10,'Respuesta_texto'].value_counts().reset_index()
Pregunta_11 = encuestas.loc[encuestas.Pregunta == 11,'Respuesta_texto'].value_counts().reset_index()
Pregunta_12 = encuestas.loc[encuestas.Pregunta == 12,'Respuesta_texto'].value_counts().reset_index()

######################
#3 Creando el grafico#
######################

#Facultades
trace_4 = go.Pie(labels=Pregunta_1.loc[:,'index'], values=Pregunta_1.loc[:,'Respuesta_texto'])

layout_4 = go.Layout(legend={"x": 0, "y": -.5})

fig_4 = go.Figure(data = [trace_4], layout = layout_4)

########################
#4 Creacion Dash Layout#
########################

def create_layout(app):
    
    return html.Div(
        [
        
        html.Div([Header(app)]),
            #page 1
            html.Div([
                    
                # Row 3
                html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Tenemos lo Resultados Siguientes"),
                                    html.Br([]),
                                    html.P(
                                        "",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                        ),
                    #Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("Porcentaje Muestra por Facultades UNAM", className="subtitle padded"),
                                    dcc.Graph(id='plot_0',figure = fig_4)
                                ],  className="six columns", style={'width': '33%','align': 'right', 'display': 'inline-block'}
                                    ),
                            html.Div(
                                [
                                    html.H6("Porcentaje Muestra por Facultades UNAM", className="subtitle padded",),
                                    dcc.Graph(id='plot_1',figure = fig_4)
                                ],  className="six columns",style={'width': '33%', 'align': 'right', 'display': 'inline-block'}
                                    ),
                            html.Div(
                                [
                                    html.H6("Porcentaje Muestra por Facultades UNAM", className="subtitle padded",),
                                    dcc.Graph(id='plot_2',figure = fig_4)
                                ],  className="six columns", style={'width': '33%', 'align': 'right', 'display': 'inline-block'}
                                    ),
                        ],
                        className = "row",
                        style = {"margin-bottom":"35px"},
                            ),
                        ], className = "page"
                    )
                ])
        
        