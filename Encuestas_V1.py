#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 21:25:43 2020

@author: carlos
"""

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash

import pandas as pd
import pathlib

#####################
#1 Inicio aplicación#
#####################

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

####################
#2 Importando datos#
####################
encuestas = pd.read_csv('/home/carlos/Documentos/Encuestas_UNAM/encuestas.csv')

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
trace_0 = go.Pie(labels=conteo.loc[:,'Facultad'], values=conteo.loc[:,'encuestados'])

layout_0 = go.Layout(title = '% Muestra Facultades UNAM', xaxis = dict(title = 'xvalue',
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

app.layout = html.Div(
        [
            
            html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
                    ),
            html.Div(
                [
                    html.Img(
                        src=app.get_asset_url("unam.png"),
                        className="logo"
                    ),
                ],
                className="row",
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("Encuesta Derecho Animal")],
                        className="seven columns main-title",
                    ),
                    html.Div(
                        [
                            dcc.Link(
                                "Tere Baena Sanchez",
                                href="/dash-financial-report/full-view",
                                className="full-view-link",
                            )
                        ],
                        className="five columns",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
            ),
            html.Div(
        [
            dcc.Link(
                "Muestra",
                href="/dash-financial-report/overview",
                className="tab first",
            ),
            dcc.Link(
                "Resultados",
                href="/dash-financial-report/price-performance",
                className="tab",
            ),
            dcc.Link(
                "Conclusiones",
                href="/dash-financial-report/portfolio-management",
                className="tab",
            ),
            dcc.Link(
                "¿Qué sigue?", href="/dash-financial-report/fees", className="tab"
            ),
        ],
        className="row all-tabs",
                    ),
                html.Div([
        #Facultades
        html.Div([
            dcc.Graph(id='plot_0',figure = fig_0)], className="six columns", style={'width': '50%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Graph(id='plot_1',figure = fig_2)], className="six columns", style={'width': '50%', 'align': 'right', 'display': 'inline-block'})
        
             ],
        className="row" , style = {'padding' : '40px' ,'backgroundColor' : '#3aaab2'})
        ],
        className="row",
    )


##########################        
#5 Funciones desplegables#
##########################


#############
#6 Ejecucion#
#############
if __name__ == '__main__':
    app.run_server()