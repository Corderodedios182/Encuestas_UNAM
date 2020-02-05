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

encuestas = pd.read_csv('https://raw.githubusercontent.com/Corderodedios182/Encuestas_UNAM/master/Dash_Encuestas/datos/encuestas.csv')

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
                                    html.P(
                                            "La presente encuesta se realizó a los alumnos de las facultades de la Universidad Nacional Autónoma de México (UNAM) \
                                            con la finalidad de conocer las opiniones y conocimiento que tienen sobre el derecho animal y la importancia de éste para la defensa de  \
                                            los animales en México." ) ,
                                    html.P(        
                                            "Se estudiaron a fondo las respuestas de los alumnos encuestados de la Facultad de Derecho, de la Facultad de Medicina Veterinaria y Zootecnia y de la Facultad de Ciencias, \
                                            debido a que en estas facultades el estudio, trato y manejo de los animales es sustancial para crear investigaciones interdisciplinarias en el campo del derecho animal."),
                                    html.P(
                                            "Los siguientes datos son de considerable interés para la presente investigación, ya que la comunidad universitaria desempeñará un papel fundamental en distintos sectores \
                                            de la sociedad, en los cuales los animales representan un fin en sí mismo o un recurso.") ,
                                    html.P(
                                            "Per se, la profesionalización y capacitación hacia la comunidad universitaria en temas de bienestar animal y derecho animal resulta necesaria para entender \
                                            el trato y cuidado de los animales; las implicaciones jurídicas que se derivan de los actos civiles-mercantiles y las limitaciones que se tienen en materia civil." ),
                                    html.P(
                                            "Si bien en el Código Civil Federal mexicano, los animales son definidos como cosas (partiendo de una visión románica-germánica derivada de la época de Gayo y Justiniano), \
                                            la comunidad científica ha logrado comprobar que la conciencia es un fundamento clave para la protección jurídica de los animales (Declaración de Cambridge sobre la Conciencia)."),
                                    html.P(        
                                            "Con el estudio de las regiones del encéfalo y diecénfalo de un animal vertebrado se puede constatar que en ellas se presentan funciones como el miedo, la agresión, los afectos, \
                                            la memoria emocional, los estados de ánimo, la percepción consciente y la localización del dolor; así como el hambre, la sed, el impulso sexual y la expresión de las emociones. \
                                            Por lo que ha quedado demostrado que los animales al igual que los seres humanos son capaces de sentir dolor y no son máquinas sin memoria, como lo expuso Descartes." ,
                                            style={"color": "#ffffff"},
                                        className="row")],
                         className="product")],
                        className="row"),
                #Row 4
                html.Div([
                    
                        html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("Porcentaje Muestra por Facultades UNAM", className="subtitle padded"),
                                    dcc.Graph(id='plot_0',figure = fig_0)
                                ],  className="six columns",  style={'width': '50%', 'align': 'right', 'display': 'inline-block'}
                                    ),
                            ],
                          className = "row",
                        style = {"margin-bottom":"35px"})
                         ],
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
        
        