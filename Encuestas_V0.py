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
import numpy as np
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
df = conteo
#Facultades
def nueva(df):
    nb_leads = df['encuestados'].sum()
    types = df['Facultad'].unique().tolist()
    values = []
    
    for case_type in types:
        nb_type = df[df['Facultad'] == case_type].iloc[:,2]
        values.append(nb_type / nb_leads)
        
    pd.DataFrame(values)
    trace = go.Pie(labels = np.array(types), values = np.array([values]))
    layout =  go.Layout(legend = {"x":0,"y":-.5},  margin=dict(l=23,r=18,b=53,t=73,),
                    paper_bgcolor='rgb(223, 223, 223)', template = 'ggplot2')
    
    fig = go.Figure(data = [trace], layout = layout)

    pyo.plot(fig_1)
    
    return dict(data=[trace], layout=layout)

########################
#4 Creacion Dash Layout#
########################

app.layout = html.Div([

    #Boton desplegable
       html.P([
        dcc.Dropdown(id = 'facultad', 
                     options = Facultades,
                     value = "all",
                     clearable=False)
        ],
        ), 
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
def nueva_final(df):
    df = conteo
    return nueva(df)
    
#############
#6 Ejecucion#
#############
if __name__ == "__main__":
    app.run_server()
