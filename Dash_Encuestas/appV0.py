# -*- coding: utf-8 -*-

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import os
os.chdir('/home/carlos/Documentos/Encuestas_UNAM/Dash_Encuestas')

from librerias import (Muestra,Resultados, Conclusiones, Que_sigue)

app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
server = app.server

# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/Dash_Encuestas/Resultados":
        return Resultados.create_layout(app)
    elif pathname == "/Dash_Encuestas/Conclusiones":
        return Conclusiones.create_layout(app)
    elif pathname == "/Dash_Encuestas/Que_sigue":
        return Que_sigue.create_layout(app)
    else:
        return Muestra.create_layout(app)
    
    
if __name__ == "__main__":
    app.run_server()


