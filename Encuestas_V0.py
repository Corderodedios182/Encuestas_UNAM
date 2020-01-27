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

#Facultades


########################
#4 Creacion Dash Layout#
########################

app.layout = html.Div([

    #Boton desplegable
       html.P([
        html.Label("Facultades"),
        dcc.Dropdown(id = 'facultad', 
                     options = Facultades,
                     value = Facultades,
                     multi = True)],
        style = {'width': '400px',
                 'fontSize' : '20px',
                 'padding-left' : '100px',
                 'display': 'inline-block'}), 
    #Graficas
    html.Div([
        #Facultades
        html.Div([
            dcc.Graph(id='grafica')], className="six columns", style={'width': '50%', 'display': 'inline-block'})
        ])
    ])
     
##########################        
#5 Funciones desplegables#
##########################
@app.callback(Output('grafica', 'figure'),[Input('facultad', 'value')])
def Facultades(filtrar):

    filtro = conteo.loc[:'Facultad' == filtrar]
    
    trace_0 = go.Pie(labels=filtro.loc[:,'Facultad'], values=filtro.loc[:,'encuestados'])
    layout_0 = go.Layout(legend = {"x":-1,"y":.5},  margin=dict(l=40,r=30,b=80,t=100,),
                    paper_bgcolor='rgb(243, 243, 243)',
                    plot_bgcolor='rgb(243, 243, 243)')
    fig_0 = go.Figure(data = [trace_0], layout = layout_0)

    return fig_0
    
#############
#6 Ejecucion#
#############
if __name__ == "__main__":
    app.run_server()
