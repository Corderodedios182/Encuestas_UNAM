#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 23:17:03 2020

@author: carlos
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd

app = dash.Dash()

encuestas = pd.read_csv('/home/carlos/Documentos/Encuestas_UNAM/encuestas.csv')

#General
conteo = encuestas.Facultad.value_counts().reset_index()
conteo['encuestados'] = conteo.Facultad/12
conteo.columns = ['Facultad','Conteo','encuestados']

#Opciones boton
Facultades_0 = conteo.loc[:,'Facultad']
Facultades = [{'label':i,'value':i} for i in Facultades_0]
Facultades[0]['value'] = 1
Facultades[1]['value'] = 2
Facultades[2]['value'] = 3
Facultades[3]['value'] = 4
Facultades[4]['value'] = 5
Facultades[5]['value'] = 6
Facultades[6]['value'] = 7
Facultades[7]['value'] = 8
Facultades[8]['value'] = 9
Facultades[9]['value'] = 10
Facultades[10]['value'] = 11


def app_layout():
    return(
            html.Div([
                    dcc.Dropdown(id = 'tabs', 
                     options = Facultades,
                     value = "all",
                     clearable=False),
                    html.Div(id='output-tab')
                    ])
    )

app.layout = app_layout()

@app.callback(Output('output-tab', 'children'),
              [Input('tabs', 'value')])
def display_content(value):
    data = [
        {
            'values': [[10,90],[5, 95],[15,85],[20,80]][int(value)-1],
            'type': 'pie',
        },
    ]

    return html.Div([
        dcc.Graph(
            id='graph',
            figure={
                'data': data,
                'layout': {
                    'margin': {
                        'l': 30,
                        'r': 0,
                        'b': 30,
                        't': 0
                    },
                    'legend': {'x': 0, 'y': 1}
                }
            }
        )
    ])
if __name__ == '__main__':
    app.server.run()