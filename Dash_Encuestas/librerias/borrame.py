#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 23:47:18 2020
@author: carlos
"""
from appV0 import app
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.graph_objects as go

from utilsv0 import Header

####################
#2 Importando datos#
####################

encuestas = pd.read_csv('/home/carlos/Documentos/Encuestas_UNAM/encuestas.csv')

#General
conteo = encuestas.Facultad.value_counts().reset_index()
conteo['encuestados'] = conteo.Facultad/12
conteo.columns = ['Facultad','Conteo','encuestados']

#Opciones boton
Facultades_0 = conteo.loc[:,'Facultad']
Facultades = [{'label':i,'value':i} for i in Facultades_0]

######################
#3 Creando el grafico#
######################
Pregunta_1 = encuestas.loc[encuestas.Pregunta == 1,'Respuesta_texto'].value_counts().reset_index()

trace_1 = go.Pie(labels=Pregunta_1.loc[:,'index'], values=Pregunta_1.loc[:,'Respuesta_texto'])
layout_1 =  go.Layout(legend = {"x":0,"y":-.5},  margin=dict(l=23,r=18,b=53,t=73,),
                          paper_bgcolor='rgb(223, 223, 223)', template = 'ggplot2')
                    
fig_1 = go.Figure(data = [trace_1], layout = layout_1)    

########################
#4 Creacion Dash Layout#
########################
value = 'Derecho'
def create_layout(app):
    
    return html.Div(
        [
        html.Div([Header(app)]),
            #page 1
            html.Div([
                    
                # Row 3
                html.Div([
                         html.Div([
                                    html.H5("¿Qué es el Derecho Animal?"),
                                    html.Br([]),
                                    html.P(
                                        "",
                                        style={"color": "#ffffff"},
                                        className="row")],
                         className="product")],
                        className="row"),
                # Boton
                 html.Div([
                    dcc.Dropdown(id='filtro_13', 
                     options = Facultades,
                     value = "all",
                     clearable=False)
                    ]),
                 html.Div(id='grafica_13',children=dcc.Graph(id='dummy'))
                    ], className="sub_page"),
                ], className="page",)

@app.callback(Output('grafica_13', 'children'),[Input('filtro_13', 'value')])
def display_content(value):
    
    Pregunta_1 = encuestas.loc[(encuestas.Pregunta == 1) &
                               (encuestas.Facultad == value),'Respuesta_texto'].value_counts().reset_index()

    trace_1 = go.Pie(labels=Pregunta_1.loc[:,'index'], values=Pregunta_1.loc[:,'Respuesta_texto'])
    layout_1 =  go.Layout(legend = {"x":0,"y":-.5},  margin=dict(l=23,r=18,b=53,t=73,),
                          paper_bgcolor='rgb(223, 223, 223)', template = 'ggplot2')
                    
    fig_1 = go.Figure(data = [trace_1], layout = layout_1)    
    
    return fig_1
