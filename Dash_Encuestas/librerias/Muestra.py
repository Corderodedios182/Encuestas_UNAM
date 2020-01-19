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

#Rango de Edades
tmp = encuestas.groupby(['Facultad','Edad'],  as_index = False).count().iloc[:,:3]
tmp.columns = ['Facultad','Edad','Conteo']
tmp.Conteo = tmp.Conteo/12

tmp.loc[tmp['Edad'] == 16]

######################
#3 Creando el grafico#
######################

#Facultades
trace_0 = go.Pie(labels=conteo.loc[:,'Facultad'], values=conteo.loc[:,'encuestados'])
layout_0 = go.Layout(legend = {"x":-1,"y":.5},  margin=dict(l=40,r=30,b=80,t=100,),
                    paper_bgcolor='rgb(243, 243, 243)',
                    plot_bgcolor='rgb(243, 243, 243)')
fig_0 = go.Figure(data = [trace_0], layout = layout_0)

#Sexo
fig_1 = go.Figure()

fig_1.add_trace(go.Bar(
    x=Masculino['Facultad'],
    y=Masculino['encuestados'],
    name='Hombres',
    text = Masculino['encuestados'],
    textposition = 'auto',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    )
))
fig_1.add_trace(go.Bar(
    x=Mujeres['Facultad'],
    y=Mujeres['encuestados'],
    name='Mujeres',
    text = Masculino['encuestados'],
    textposition = 'auto',
    marker=dict(
        color='rgba(246, 78, 139, 0.6)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
        )
))

fig_1.update_layout(barmode='stack', title = 'Puedo colocar texto aquí', title_x = 0.45,
                    margin=dict(l=40,r=30,b=80,t=100,),
                    paper_bgcolor='rgb(243, 243, 243)',
                    plot_bgcolor='rgb(243, 243, 243)')

#Rango de Edades
fig_2 = go.Figure()

fig_2.add_trace(go.Box(
    y=tmp["Edad"],
    x=tmp["Facultad"],
    name='kale',
    boxpoints='all',
    jitter=0.5,
    whiskerwidth=0.2,
    marker_size=2,
    line_width=1)
    )

fig_2.update_layout(
    title = 'Puedo colocar texto aqui',
    yaxis_title='Rango de Edades',
    yaxis=dict(
        autorange=True,
        showgrid=True,
        zeroline=True,
        dtick=3,
        gridcolor='rgb(255, 255, 255)',
        gridwidth=1,
        zerolinecolor='rgb(255, 255, 255)',
        zerolinewidth=2,
    ),
    margin=dict(
        l=40,
        r=30,
        b=80,
        t=100,
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
    showlegend=False
)



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
                html.Div([
                         html.Div([
                                    html.H5("¿Qué es el Derecho Animal?"),
                                    html.Br([]),
                                    html.P(
                                        "\
                                    As the industry’s first index fund for individual investors, \
                                    the Calibre Index Fund is a low-cost way to gain diversified exposure \
                                    to the U.S. equity market. The fund offers exposure to 500 of the \
                                    largest U.S. companies, which span many different industries and \
                                    account for about three-fourths of the U.S. stock market’s value. \
                                    The key risk for the fund is the volatility that comes with its full \
                                    exposure to the stock market. Because the Calibre Index Fund is broadly \
                                    diversified within the large-capitalization market, it may be \
                                    considered a core equity holding in a portfolio.",
                                        style={"color": "#ffffff"},
                                        className="row")],
                         className="product")],
                        className="row"),
                #Row 4
                html.Div([
                         html.Div([
                                    html.H6("Porcentaje Muestra por Facultades UNAM", className="subtitle padded"),
                                    dcc.Graph(id='plot_0',figure = fig_0)],
                                    className="six columns", style={'width': '50%', 'display': 'inline-block'})],
                                className = "row", style = {"margin-bottom":"35px"}),
                #Row 5
                    html.Div([
                        html.Div([
                                    html.H6("Proporción Mujeres y Hombres", className="subtitle padded"),
                                    dcc.Graph(id='plot_1',figure = fig_1)])]),
                #row 6
                    html.Div([
                        html.Div([
                                    html.H6("Rango de Edades Facultades", className="subtitle padded"),
                                    dcc.Graph(id='plot_2',figure = fig_2)])])
                    ], className="sub_page"),
                ], className="page",)
        
        