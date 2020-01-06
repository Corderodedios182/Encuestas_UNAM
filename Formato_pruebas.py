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

######################
#3 Creando el grafico#
######################


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
                    )
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