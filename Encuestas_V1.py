#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 21:25:43 2020

@author: carlos
"""
import plotly.graph_objs as go
import plotly.offline as pyo
import pandas as pd

#########################
#Resumenes Exploratorios#
#########################

encuestas = pd.read_csv('/home/carlos/Documentos/Encuestas_UNAM/encuestas.csv')

#Muestra Facultades
conteo = encuestas.Facultad.value_counts().reset_index()
conteo['encuestados'] = conteo.Facultad/12
conteo.columns = ['Facultad','Conteo','encuestados']

trace_0 = go.Pie(labels=conteo.loc[:,'Facultad'], values=conteo.loc[:,'encuestados'])
layout_0 = go.Layout(legend = {"x":0,"y":.5})
fig_0 = go.Figure(data = [trace_0], layout = layout_0)
pyo.plot(fig_0, filename='scatter2.html')

#Rango de Edad
tmp = encuestas.groupby(['Facultad','Edad'],  as_index = False).count().iloc[:,:3]
tmp.columns = ['Facultad','Edad','Conteo']
tmp.Conteo = tmp.Conteo/12

tmp.loc[tmp['Edad'] == 16]

fig = go.Figure()

fig.add_trace(go.Box(
    y=tmp["Edad"],
    x=tmp["Facultad"],
    name='kale',
    boxpoints='all',
    jitter=0.5,
    whiskerwidth=0.2,
    marker_size=2,
    line_width=1)
    )

fig.update_layout(
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

pyo.plot(fig)

#Sexo
Masculino = encuestas[encuestas.Sexo == 'M'].Facultad.value_counts().reset_index()
Masculino['encuestados'] = Masculino.Facultad/12
Masculino.columns = ['Facultad','Conteo','encuestados']

Mujeres = encuestas[encuestas.Sexo == 'F'].Facultad.value_counts().reset_index()
Mujeres['encuestados'] = Mujeres.Facultad/12
Mujeres.columns = ['Facultad','Conteo','encuestados']

#Sexo
fig_2 = go.Figure()

fig_2.add_trace(go.Bar(
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
fig_2.add_trace(go.Bar(
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

fig_2.update_layout(barmode='stack', title = 'Propoción de Mujeres y Hombres', title_x = 0.45)

pyo.plot(fig_2, filename='scatter2.html')







