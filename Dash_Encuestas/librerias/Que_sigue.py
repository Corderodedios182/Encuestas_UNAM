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

encuestas = pd.read_csv('/home/carlos/Documentos/Encuestas_UNAM/Dash_Encuestas/datos/encuestas.csv')

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

#Facultades
trace_0 = go.Pie(labels=conteo.loc[:,'Facultad'], values=conteo.loc[:,'encuestados'])

layout_0 = go.Layout(xaxis = dict(title = 'xvalue',
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

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 6
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("Puntos de la línea de investigación", className="subtitle padded"),
                                    html.Br([]),
                                ],
                                className="row",
                            ),
                            html.Div(
                                [
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.Li("La investigación se basa en el análisis jurídico-lingüístico del Libro segundo: De los bienes. Títulos primero y segundo \
                                                    (Clasificación de los bienes), capítulos I, II, III, IV, V; títulos tercero y cuarto (De la propiedad), capítulos I, II \
                                                    (De la apropiación de los animales) y IV, del Código Civil Federal (CCF) mexicano."),
                                            html.Li(
                                                "Por lo que se requiere un manejo de información a partir de la interpretación jurídica, del campo de la lingüística aplicada y de la biología."
                                            ),
                                            html.Li(
                                                "Se llevará a cabo un estudio comparado de los códigos civiles de Alemania, Austria, Suiza y Francia, en cuyas legislaciones los animales han dejado de ser cosas."
                                            ),
                                            html.Li(
                                                "Se realizará el análisis lingüístico-biológico del concepto de animal."
                                            ),
                                            html.Li(
                                                "En cuanto hace al reconocimiento de derechos se pretende un análisis categórico de éstos (con ciertas excepciones de acuerdo a la especie), \
                                                pues si bien el sector universitario opinó que todos los animales poseen derechos, es cierto que tales derechos deben ser estudiados a profundidad."
                                            ),
                                            html.Li(
                                                "Tratándose del bienestar animal, durante el sacrificio (ley de sanidad y normas oficiales mexicanas) o en la vida libre de los animales, éste representa un avance en la materia."
                                            ),
                                            html.Li(
                                                "No obstante, sin olvidar que la crueldad hacia ellos y su sufrimiento sigue estando presente en la industria cárnica y farmacéutica, y en los hogares mexicanos, \
                                                se estudiarán las implicaciones legales (obligaciones de hacer o no hacer) sobre la muerte del animal con aturdimiento y la diferencia que existe entre este método \
                                                y la eutanasia (cuando ya no es posible mantener con vida a un animal)."
                                            )
                                        ],
                                        id="reviews-bullet-pts",
                                    ),
                                ],
                                className="row",
                            ),
                        ],
                        className="row ",
                    )
                ],
                className="sub_page",
            ),
        ],
        className="page",
    )