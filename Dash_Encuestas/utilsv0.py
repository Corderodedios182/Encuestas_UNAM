#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 23:42:54 2020

@author: carlos
"""

import dash_html_components as html
import dash_core_components as dcc

def Header(app):
    return html.Div([get_header(app), html.Br([]), get_menu()])


def get_header(app):
    header = html.Div([
                html.Div([
                    html.Img(
                        src=app.get_asset_url("derecho-animal.jpg"),
                        style={'height':'5%', 'width':'5%'},
                        className = "logo")],
                    className="row"),
                html.Div([
                    html.Div(
                        [html.H5("Análisis estadístico sobre derecho animal")],
                        className="seven columns main-title"),
                    html.Div([
                            dcc.Link(
                                "Logo UNAM",
                                href="https://www.facebook.com/tere.baena.1",
                                className="full-view-link")],
                        className="five columns")],
                className="twelve columns",
                style={"padding-left": "0"})
                ],className="row")
    return header


def get_menu():
    menu = html.Div(
        [
            dcc.Link(
                "Muestra",
                href="/Dash_Encuestas/Muestra",
                className="tab first",
            ),
            dcc.Link(
                "Resultados",
                href="/Dash_Encuestas/Resultados",
                className="tab",
            ),
            dcc.Link(
                "Conclusiones",
                href="/Dash_Encuestas/Conclusiones",
                className="tab",
            ),
            dcc.Link(
                "¿Qué sigue?", href="/Dash_Encuestas/Que_sigue", className="tab"
            ),
        ],
        className="row all-tabs",
    )
    return menu
