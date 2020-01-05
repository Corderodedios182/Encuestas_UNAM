#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 19:02:10 2020

@author: carlos
"""
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots

import pandas as pd
import plotly.graph_objects as go


#####################
#1 Inicio aplicación#
#####################

app = dash.Dash()

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

#Rango de Edad
R_Edad = encuestas.Edad.value_counts().reset_index()
R_Edad['encuestados'] = R_Edad.Edad/12
R_Edad.columns = ['Edad','Conteo','encuestados']

#Opciones boton
Facultades_0 = conteo.loc[:,'Facultad']
Facultades = [{'label':i,'value':i} for i in Facultades_0]

#Preguntas
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

#Rango de Edad

fig_3 = go.Figure()

fig_3.add_trace(go.Bar(
    x=R_Edad['Edad'],
    y=R_Edad['encuestados'],
    name='Edades',
    marker=dict(
        color='rgba(246, 78, 139, 0.6)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3))
    ))

fig_3.update_layout(title = 'Rango de Edades entre 18 y 23', title_x = 0.45)

#Preguntas

specs = [[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}]]

fig_4 = make_subplots(rows=1, cols=3, specs=specs,
                    subplot_titles = ['¿Conoces de la existencia del derecho animal?','¿Consideras que los animales tienen derechos?','¿Qué derechos consideras tienen los animales?'])

fig_4.add_trace(go.Pie(labels=Pregunta_1.loc[:,'index'], values=Pregunta_1.loc[:,'Respuesta_texto']), 1, 1)
fig_4.add_trace(go.Pie(labels=Pregunta_2.loc[:,'index'], values=Pregunta_2.loc[:,'Respuesta_texto']), 1, 2)
fig_4.add_trace(go.Pie(labels=Pregunta_3.loc[:,'index'], values=Pregunta_3.loc[:,'Respuesta_texto']), 1, 3)

fig_5 = make_subplots(rows=1, cols=3, specs=specs,
                    subplot_titles = ['¿Conoces de la existencia del derecho animal?','¿Consideras que los animales tienen derechos?','¿Qué derechos consideras tienen los animales?'])

fig_5.add_trace(go.Pie(labels=Pregunta_4.loc[:,'index'], values=Pregunta_4.loc[:,'Respuesta_texto']), 1, 1)
fig_5.add_trace(go.Pie(labels=Pregunta_5.loc[:,'index'], values=Pregunta_5.loc[:,'Respuesta_texto']), 1, 2)
fig_5.add_trace(go.Pie(labels=Pregunta_6.loc[:,'index'], values=Pregunta_6.loc[:,'Respuesta_texto']), 1, 3)

fig_6 = make_subplots(rows=1, cols=3, specs=specs,
                    subplot_titles = ['¿Conoces de la existencia del derecho animal?','¿Consideras que los animales tienen derechos?','¿Qué derechos consideras tienen los animales?'])
                    
fig_6.add_trace(go.Pie(labels=Pregunta_7.loc[:,'index'], values=Pregunta_7.loc[:,'Respuesta_texto']), 1, 1)
fig_6.add_trace(go.Pie(labels=Pregunta_8.loc[:,'index'], values=Pregunta_8.loc[:,'Respuesta_texto']), 1, 2)
fig_6.add_trace(go.Pie(labels=Pregunta_9.loc[:,'index'], values=Pregunta_9.loc[:,'Respuesta_texto']), 1, 3)

fig_7 = make_subplots(rows=1, cols=3, specs=specs,
                    subplot_titles = ['¿Conoces de la existencia del derecho animal?','¿Consideras que los animales tienen derechos?','¿Qué derechos consideras tienen los animales?'])

fig_7.add_trace(go.Pie(labels=Pregunta_10.loc[:,'index'], values=Pregunta_10.loc[:,'Respuesta_texto']), 1, 1)
fig_7.add_trace(go.Pie(labels=Pregunta_11.loc[:,'index'], values=Pregunta_11.loc[:,'Respuesta_texto']), 1, 2)
fig_7.add_trace(go.Pie(labels=Pregunta_12.loc[:,'index'], values=Pregunta_12.loc[:,'Respuesta_texto']), 1, 3)


########################
#4 Creacion Dash Layout#
########################

app.layout = html.Div([
    
    html.Div([
        html.H1(children='Resultados Encuestas Derecho Animal UNAM'),
        html.P(children='Se realizaron 2000 encuestas en diversas Facultades')
             ],
        style = {'padding' : '40px' ,
                 'backgroundColor' : '#3aaab2'}),
    
    #Graficas
    html.Div([
        #Facultades
        html.Div([
            dcc.Graph(id='plot_0',figure = fig_0)], className="six columns", style={'width': '50%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Graph(id='plot_1',figure = fig_2)], className="six columns", style={'width': '50%', 'align': 'right', 'display': 'inline-block'})
        
             ],
        className="row" , style = {'padding' : '40px' ,'backgroundColor' : '#3aaab2'}),
    #Rango de Edad
    html.Div([
        html.Div([
            dcc.Graph(id='plot_2',figure = fig_3)], className="six columns", style={'width': '50%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Graph(id='plot_3',figure = fig_2)], className="six columns", style={'width': '50%', 'align': 'right', 'display': 'inline-block'})
        
            ],
        className="row" , style = {'padding' : '40px' ,'backgroundColor' : '#3aaab2'}),
    
    #Boton desplegable
       html.P([
        html.Label("Facultades"),
        dcc.Dropdown(id = 'opt', 
                     options = Facultades,
                     value = Facultades[0])],
        style = {'width': '400px',
                 'fontSize' : '20px',
                 'padding-left' : '100px',
                 'display': 'inline-block'}),
     #Respuestas
       html.Div([
        html.Div([
            dcc.Graph(id='plot_4',figure = fig_4)])
        ],
        className="row" , style = {'padding' : '40px' ,'backgroundColor' : '#3aaab2'}),
       
       html.Div([
        html.Div([
            dcc.Graph(id='plot_5',figure = fig_5)])
        ],
        className="row" , style = {'padding' : '40px' ,'backgroundColor' : '#3aaab2'}),
       
       html.Div([
        html.Div([
            dcc.Graph(id='plot_6',figure = fig_6)])
        ],
        className="row" , style = {'padding' : '40px' ,'backgroundColor' : '#3aaab2'}),
       
       html.Div([
        html.Div([
            dcc.Graph(id='plot_7',figure = fig_7)])
        ],
        className="row" , style = {'padding' : '40px' ,'backgroundColor' : '#3aaab2'})
               ])

##########################        
#5 Funciones desplegables#
##########################
@app.callback([Output('plot_0', 'figure'),
               Output('plot_1', 'figure')],
               [Input('opt', 'value')])

def update_figure(input1):
    
    conteo_tmp = conteo.loc[conteo.Facultad == input1,:]
    
    trace_0 = go.Pie(labels=conteo.loc[:,'Facultad'], values=conteo.loc[:,'encuestados'])
    
    trace_1 = go.Pie(labels=conteo_tmp.loc[:,'Facultad'], values=conteo_tmp.loc[:,'encuestados'])
    
    fig_0 = go.Figure(data = [trace_0, trace_1], layout = layout_0)
    
    return fig_0
    

#############
#6 Ejecucion#
#############
if __name__ == '__main__':
    app.run_server()