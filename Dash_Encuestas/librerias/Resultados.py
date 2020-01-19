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
trace_1 = go.Pie(labels=Pregunta_1.loc[:,'index'], values=Pregunta_1.loc[:,'Respuesta_texto'])
layout_1 = go.Layout(legend={"x": 0, "y": -.5})
fig_1 = go.Figure(data = [trace_1], layout = layout_1)

trace_2 = go.Pie(labels=Pregunta_2.loc[:,'index'], values=Pregunta_2.loc[:,'Respuesta_texto'])
layout_2 = go.Layout(legend={"x": 0, "y": -.5})
fig_2 = go.Figure(data = [trace_2], layout = layout_2)

trace_3 = go.Pie(labels=Pregunta_3.loc[:,'index'], values=Pregunta_3.loc[:,'Respuesta_texto'])
layout_3 = go.Layout(legend={"x": 0, "y": -.5})
fig_3 = go.Figure(data = [trace_3], layout = layout_3)

trace_4 = go.Pie(labels=Pregunta_4.loc[:,'index'], values=Pregunta_4.loc[:,'Respuesta_texto'])
layout_4 = go.Layout(legend={"x": 0, "y": -.5})
fig_4 = go.Figure(data = [trace_4], layout = layout_4)

#################
trace_5 = go.Pie(labels=Pregunta_5.loc[:,'index'], values=Pregunta_5.loc[:,'Respuesta_texto'])
layout_5 = go.Layout(legend={"x": 0, "y": -.5})
fig_5 = go.Figure(data = [trace_5], layout = layout_5)

trace_6 = go.Pie(labels=Pregunta_6.loc[:,'index'], values=Pregunta_6.loc[:,'Respuesta_texto'])
layout_6 = go.Layout(legend={"x": 0, "y": -.5})
fig_6 = go.Figure(data = [trace_6], layout = layout_6)

trace_7 = go.Pie(labels=Pregunta_7.loc[:,'index'], values=Pregunta_7.loc[:,'Respuesta_texto'])
layout_7 = go.Layout(legend={"x": 0, "y": -.5})
fig_7 = go.Figure(data = [trace_7], layout = layout_7)

trace_8 = go.Pie(labels=Pregunta_8.loc[:,'index'], values=Pregunta_8.loc[:,'Respuesta_texto'])
layout_8 = go.Layout(legend={"x": 0, "y": -.5})
fig_8 = go.Figure(data = [trace_8], layout = layout_8)

##################
trace_9 = go.Pie(labels=Pregunta_9.loc[:,'index'], values=Pregunta_9.loc[:,'Respuesta_texto'])
layout_9 = go.Layout(legend={"x": 0, "y": -.5})
fig_9 = go.Figure(data = [trace_9], layout = layout_9)

trace_10 = go.Pie(labels=Pregunta_10.loc[:,'index'], values=Pregunta_10.loc[:,'Respuesta_texto'])
layout_10 = go.Layout(legend={"x": 0, "y": -.5})
fig_10 = go.Figure(data = [trace_10], layout = layout_10)

trace_11 = go.Pie(labels=Pregunta_11.loc[:,'index'], values=Pregunta_11.loc[:,'Respuesta_texto'])
layout_11 = go.Layout(legend={"x": 0, "y": -.5})
fig_11 = go.Figure(data = [trace_11], layout = layout_11)

trace_12 = go.Pie(labels=Pregunta_12.loc[:,'index'], values=Pregunta_12.loc[:,'Respuesta_texto'])
layout_12 = go.Layout(legend={"x": 0, "y": -.5})
fig_12 = go.Figure(data = [trace_12], layout = layout_12)


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
                                    html.H6("¿Conoces de la existencia del derecho animal?", className="subtitle padded"),
                                    dcc.Graph(id='plot_1',figure = fig_1)
                                ],  className="six columns", style={'width': '25%','align': 'right', 'display': 'inline-block'}
                                    ),
                            html.Div(
                                [
                                    html.H6("¿Consideras que los animales tienen derechos?", className="subtitle padded",),
                                    dcc.Graph(id='plot_2',figure = fig_2)
                                ],  className="six columns",style={'width': '25%', 'align': 'right', 'display': 'inline-block'}
                                    ),
                            html.Div(
                                [
                                    html.H6("¿Qué derechos consideras tienen los animales?", className="subtitle padded",),
                                    dcc.Graph(id='plot_3',figure = fig_3)
                                ],  className="six columns", style={'width': '25%', 'align': 'right', 'display': 'inline-block'}
                                    ),
                            html.Div(
                                [
                                    html.H6("¿Qué animales consideras tienen que ser protegidos jurídicamente?", className="subtitle padded",),
                                    dcc.Graph(id='plot_4',figure = fig_4)
                                ],  className="six columns", style={'width': '25%', 'align': 'right', 'display': 'inline-block'}
                                    )
                        ],
                        className = "row",
                        style = {"margin-bottom":"35px"},
                            ),
                         html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("¿Cómo crees qué es defendido un animal en las leyes mexicanas y el Código Civil Femeninoederal?", className="subtitle padded"),
                                    dcc.Graph(id='plot_5',figure = fig_5)
                                ],  className="six columns", style={'width': '25%','align': 'right', 'display': 'inline-block'}
                                    ),
                            html.Div(
                                [
                                    html.H6("¿Sabes qué hacer ante una situación de maltrato animal?",),
                                    dcc.Graph(id='plot_6',figure = fig_6)
                                ],  className="six columns",style={'width': '25%', 'align': 'right', 'display': 'inline-block'}
                                    ),
                            html.Div(
                                [
                                    html.H6("¿Consideras importante que los servidores judiciales estén capacitados en materia de derecho animal?",),
                                    dcc.Graph(id='plot_7',figure = fig_7)
                                ],  className="six columns", style={'width': '25%', 'align': 'right', 'display': 'inline-block'}
                                    ),
                            html.Div(
                                [
                                    html.H6("¿Consideras idónea la prisión como un mecanismo para crear conciencia sobre el bienestar de los animales?", className="subtitle padded",),
                                    dcc.Graph(id='plot_8',figure = fig_8)
                                ],  className="six columns", style={'width': '25%', 'align': 'right', 'display': 'inline-block'}
                                    )
                        ],
                        className = "row",
                        style = {"margin-bottom":"35px"},
                            ),
                              html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("¿Qué opinas de la representación jurídica hacia los animales por parte de los abogados y el Ministerio Público?", className="subtitle padded"),
                                    dcc.Graph(id='plot_9',figure = fig_9)
                                ],  className="six columns", style={'width': '25%','align': 'right', 'display': 'inline-block'}
                                    ),
                            html.Div(
                                [
                                    html.H6("¿Qué protecciones básicas consideras viables para los animales de trabajo?", className="subtitle padded",),
                                    dcc.Graph(id='plot_10',figure = fig_10)
                                ],  className="six columns",style={'width': '25%', 'align': 'right', 'display': 'inline-block'}
                                    ),
                            html.Div(
                                [
                                    html.H6("Tratándose de la base de tu alimentación, ¿qué tanto consumes productos cárnicos?", className="subtitle padded",),
                                    dcc.Graph(id='plot_11',figure = fig_11)
                                ],  className="six columns", style={'width': '25%', 'align': 'right', 'display': 'inline-block'}
                                    ),
                            html.Div(
                                [
                                    html.H6("¿Consideras importante que los lingüistas participen en la redacción de las leyes y códigos en materia de derecho animal?", className="subtitle padded",),
                                    dcc.Graph(id='plot_12',figure = fig_12)
                                ],  className="six columns", style={'width': '25%', 'align': 'right', 'display': 'inline-block'}
                                    )
                        ],
                        className = "row",
                        style = {"margin-bottom":"35px"},
                            )
                        ],className = "sub_page"
                    )
                ],className="page")
        
        