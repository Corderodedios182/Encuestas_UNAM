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

conteo = encuestas.Facultad.value_counts().reset_index()
conteo['encuestados'] = conteo.Facultad/12
conteo.columns = ['Facultad','Conteo','encuestados']


#Opciones boton
Facultades_0 = conteo.loc[:,'Facultad']
Facultades = [{'label':i,'value':i} for i in Facultades_0]

######################
#3 Creando el grafico#
######################

trace_0 = go.Pie(labels=conteo.loc[:,'Facultad'], values=conteo.loc[:,'encuestados'])

layout_0 = go.Layout(title = '% Muestra Facultades UNAM', title_x=0.45, 
                   hovermode = 'closest')

fig_0 = go.Figure(data = [trace_0], layout = layout_0)


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
    
    #Graficas
    html.Div([
        html.Div([
            dcc.Graph(id='plot_0',figure = fig_0)], className="six columns", style={'width': '50%', 'display': 'inline-block'}),
        
        html.Div([
            dcc.Graph(id='plot_1',figure = fig_0)], className="six columns", style={'width': '50%', 'align': 'right', 'display': 'inline-block'})
        
             ],
        className="row" , style = {'padding' : '40px' ,'backgroundColor' : '#3aaab2'}),
    
                      ])

##########################        
#5 Funciones desplegables#
##########################
@app.callback([Output('plot_0', 'figure'),
               Output('plot_1', 'figure')],
               [Input('opt', 'value')])

def actualiza_figura(input1):
    
    conteo_tmp = conteo.loc[conteo.Facultad == input1,:]
    
    trace_0 = go.Pie(labels=conteo_tmp.loc[:,'Facultad'], values=conteo_tmp.loc[:,'encuestados'])
    
    fig_0 = go.Figure(data = [trace_0], layout = layout_0)
    
    return fig_0
    

#############
#6 Ejecucion#
#############
if __name__ == '__main__':
    app.run_server()