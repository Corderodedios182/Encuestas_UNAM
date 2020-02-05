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

from utilsv0 import Header
####################
#2 Importando datos#
####################

encuestas = pd.read_csv('/home/carlos/Documentos/Encuestas_UNAM/Dash_Encuestas/datos/encuestas.csv')

#General
conteo = encuestas.Facultad.value_counts().reset_index()
conteo['encuestados'] = conteo.Facultad/12
conteo.columns = ['Facultad','Conteo','encuestados']

#Sexo
Masculino = encuestas[encuestas.Sexo == 'M'].Facultad.value_counts().reset_index()
Masculino['encuestados'] = Masculino.Facultad/12
Masculino.columns = ['Facultad','Conteo','encuestados']

Mujeres = encuestas[encuestas.Sexo == 'F'].Facultad.value_counts().reset_index()
Mujeres['encuestados'] = Mujeres.Facultad/12
Mujeres.columns = ['Facultad','Conteo','encuestados']

######################
#3 Creando el grafico#
######################

#Facultades
trace_0 = go.Pie(labels=conteo.loc[:,'Facultad'], values=conteo.loc[:,'encuestados'])

layout_0 = go.Layout(xaxis = dict(title = 'xvalue',
                                    zeroline = False,
                                    showline = True), 
                       yaxis = dict(title = 'yvalue', 
                                    zeroline = False,
                                    showline = True),
                       hovermode = 'closest')

fig_0 = go.Figure(data = [trace_0], layout = layout_0)

#Sexo
fig_2 = go.Figure()

fig_2.add_trace(go.Bar(
    x=Masculino['Facultad'],
    y=Masculino['encuestados'],
    name='Hombres',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    )
))
fig_2.add_trace(go.Bar(
    x=Mujeres['Facultad'],
    y=Mujeres['encuestados'],
    name='Mujeres',
    marker=dict(
        color='rgba(246, 78, 139, 0.6)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
        )
))

fig_2.update_layout(barmode='stack', title = 'Propoción de Mujeres y Hombres', title_x = 0.45)

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
                                      html.P(
                                            "El fundamento para determinar si los animales son portadores de derechos no depende de que se les otorgue el estatus de personas jurídicas, \
                                            sino que son sujetos de derechos porque cuentan con la condición de ser seres sintientes." ),
                                      html.P(
                                            "De-cosificar a los animales es el primer paso, mediante la reforma al Código Civil Federal, cuya inclusión del bienestar animal es necesaria, \
                                            ya que las problemáticas y situaciones en las que se enfrentan los animales no son finitas, pues de ciertas prácticas se derivan otras cada vez \
                                            más crueles e injustificadas." ),
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
                        ], className="sub_page"
                    ),
                ], className="page",)
        
        