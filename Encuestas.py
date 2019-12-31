#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 00:08:51 2019

@author: carlos
"""

import plotly.express as px
import plotly.offline as pyo

import pandas as pd
import os

os.chdir('/home/carlos/Documentos/Encuestas_UNAM')
os.listdir()

encuestas = pd.read_csv('encuestas.csv')
encuestas.head()

conteo = encuestas.Facultad.value_counts().reset_index()
conteo['encuestados'] = conteo.Facultad/12


df = px.data.tips()

fig = px.pie(conteo, values='encuestados', names='index', title = 'Distribución de Encuestados Facultades UNAM')
pyo.plot(fig)

