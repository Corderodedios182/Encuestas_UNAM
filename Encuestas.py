#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 00:08:51 2019

@author: carlos
"""

import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.plotly as py

import pandas as pd
import os

os.chdir('/home/carlos/Documentos/Encuestas_UNAM')
os.listdir()

encuestas = pd.read_csv('encuestas.csv')
encuestas.head()

##

conteo = encuestas.Facultad.value_counts().reset_index()
conteo['encuestados'] = conteo.Facultad/12

df = px.data.tips()

fig = px.pie(conteo, values='encuestados', names='index', title = 'Distribución de Encuestados Facultades UNAM')
pyo.plot(fig)

###

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


specs = [[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}],
         [{'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}],
         [{'type':'domain'}, {'type':'domain'}, {'type':'domain'}, {'type':'domain'}],
         ]

fig = make_subplots(rows=3, cols=4, specs=specs,
                    subplot_titles = ['Pregunta 1','Pregunta 2','Pregunta 3','Pregunta 4',
                                      'Pregunta 5','Pregunta 6','Pregunta 7','Pregunta 8',
                                      'Pregunta 9','Pregunta 10','Pregunta 11','Pregunta 12',])

#subplot_titles = ['¿Conoces de la existencia del derecho animal?','¿Consideras que los animales tienen derechos?','¿Qué derechos consideras tienen los animales?','¿Qué animales consideras tienen que ser protegidos jurídicamente?',
                                      #'¿Cómo crees qué es deFemeninoinido un animal en las leyes mexicanas y el Código Civil Femeninoederal?','¿Sabes qué hacer ante una situación de maltrato animal?','¿Consideras importante que los servidores judiciales estén capacitados en materia de derecho animal?','¿Consideras idónea la prisión como un mecanismo para crear conciencia sobre el bienestar de los animales?',
                                      #'¿Qué opinas de la representación jurídica hacia los animales por parte de los abogados y el Ministerio Público?','¿Qué protecciones básicas consideras viables para los animales de trabajo?','Tratándose de la base de tu alimentación, ¿qué tanto consumes productos cárnicos?','¿Consideras importante que los lingüistas participen en la redacción de las leyes y códigos en materia de derecho animal?',])


fig.add_trace(go.Pie(labels=Pregunta_1.loc[:,'index'], values=Pregunta_1.loc[:,'Respuesta_texto']), 1, 1)
fig.add_trace(go.Pie(labels=Pregunta_2.loc[:,'index'], values=Pregunta_2.loc[:,'Respuesta_texto']), 1, 2)
fig.add_trace(go.Pie(labels=Pregunta_3.loc[:,'index'], values=Pregunta_3.loc[:,'Respuesta_texto']), 1, 3)
fig.add_trace(go.Pie(labels=Pregunta_4.loc[:,'index'], values=Pregunta_4.loc[:,'Respuesta_texto']), 1, 4)

fig.add_trace(go.Pie(labels=Pregunta_5.loc[:,'index'], values=Pregunta_5.loc[:,'Respuesta_texto']), 2, 1)
fig.add_trace(go.Pie(labels=Pregunta_6.loc[:,'index'], values=Pregunta_6.loc[:,'Respuesta_texto']), 2, 2)
fig.add_trace(go.Pie(labels=Pregunta_7.loc[:,'index'], values=Pregunta_7.loc[:,'Respuesta_texto']), 2, 3)
fig.add_trace(go.Pie(labels=Pregunta_8.loc[:,'index'], values=Pregunta_8.loc[:,'Respuesta_texto']), 2, 4)

fig.add_trace(go.Pie(labels=Pregunta_9.loc[:,'index'], values=Pregunta_9.loc[:,'Respuesta_texto']), 3, 1)
fig.add_trace(go.Pie(labels=Pregunta_10.loc[:,'index'], values=Pregunta_10.loc[:,'Respuesta_texto']), 3, 2)
fig.add_trace(go.Pie(labels=Pregunta_11.loc[:,'index'], values=Pregunta_11.loc[:,'Respuesta_texto']), 3, 3)
fig.add_trace(go.Pie(labels=Pregunta_12.loc[:,'index'], values=Pregunta_12.loc[:,'Respuesta_texto']), 3, 4)

fig.update(layout_title_text='Se realizaron 12 Preguntas en diversas Facultades de la UNAM',
           layout_showlegend=False)

pyo.plot(fig)

#SEXO POR FACULTAD
conteo_sexo = encuestas.Facultad.value_counts().reset_index()
conteo_sexo['encuestados'] = conteo_sexo.Facultad/12
conteo_sexo.columns = ['Facultad','Conteo','encuestados']


Sexo = encuestas.groupby(['Sexo']).count().reset_index().loc[:,['Sexo','Edad']]
Sexo.columns = ['Sexo','Conteo']
Sexo.Conteo = Sexo.Conteo/12

encuestas['numero'] = 1

data = [go.Bar(
    x=conteo_sexo['Facultad'],
    y=conteo_sexo['encuestados']
)]

layout = go.Layout(
    title='2018 Winter Olympic Medals by Country'
)

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig)

#Sexo

Masculino = encuestas[encuestas.Sexo == 'M'].Facultad.value_counts().reset_index()
Masculino['encuestados'] = Masculino.Facultad/12
Masculino.columns = ['Facultad','Conteo','encuestados']

Mujeres = encuestas[encuestas.Sexo == 'F'].Facultad.value_counts().reset_index()
Mujeres['encuestados'] = Mujeres.Facultad/12
Mujeres.columns = ['Facultad','Conteo','encuestados']


fig = go.Figure()
fig.add_trace(go.Bar(
    x=Masculino['Facultad'],
    y=Masculino['encuestados'],
    name='Hombres',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    )
))
fig.add_trace(go.Bar(
    x=Mujeres['Facultad'],
    y=Mujeres['encuestados'],
    name='Mujeres',
    marker=dict(
        color='rgba(246, 78, 139, 0.6)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
        )
))

fig.update_layout(barmode='stack')
pyo.plot(fig,"a.hmtl")


#Rango edad

R_Edad = encuestas.Edad.value_counts().reset_index()
R_Edad['encuestados'] = R_Edad.R_Edad/12
R_Edad.columns = ['Edad','Conteo','encuestados']

fig = go.Figure()

fig.add_trace(go.Bar(
    x=R_Edad['Edad'],
    y=R_Edad['encuestados'],
    name='Edades',
    marker=dict(
        color='rgba(246, 78, 139, 0.6)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3))
    ))

pyo.plot(fig,"a.hmtl")




