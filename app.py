import numpy as np
import json
import plotly.express as px
from datetime import datetime as dt
from IPython.core.display import display, HTML

import warnings

from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL #, ClientsideFunction
import dash_bootstrap_components as dbc

import pandas as pd
import json
import os
################################################################################################
# Load the data and create the map
################################################################################################
df = pd.read_csv("BASE_FINAL.csv")

###########
#Genero P6020
###########
dic_P6020={"1":"Male","2": "Female"}
df.P6020=df.P6020.astype("str").replace(dic_P6020, regex=False)
# merge.P6020=merge.P6020.astype("str").apply(lambda x: dic_P6020, regex=False)
genero=df[["P6020","FEX_C"]].groupby('P6020')['FEX_C'].sum().reset_index(name="Total") # con sum para sumar el factor de expancion
genero
g = px.bar(x="P6020",  y="Total", data_frame=genero,
           title=("Distribution by Gender"),
          #  color='#69b3a2'
# , estimator=
)
# px.xlabel("Gender")
# px.ylabel("Population")
# px.xticks((0, 1), ("Male", "Female"))

################################################################################################
# Create the app
################################################################################################
app = Dash(__name__,
            requests_pathname_prefix=request_path_prefix,
            external_stylesheets=[dbc.themes.FLATLY],
            hot_reload=True,
                meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}])

################################################################################################
# Create Layout
################################################################################################
app.layout = dbc.Row([
    dbc.Col(
        html.Nav(
            [
                html.P("asdf"),
            ],
            className="nav",
        ),
        width=2,
        align="stretch",
        class_name="navbar",
    ),
    dbc.Col(
        html.Div([
            html.H2("asdf", id='title'), #Creates the title of the app
            dcc.Graph(figure=g,id='main-figure'),
            dcc.Slider(min=0,max=1,marks={0:'US Map', 1:'Scatter Plot'},value=0,id='fig-slider',),
        ]),
        width=6
    ),
],
align="baseline",
justify="center",
)
# id="div_principal")

#Initiate the server where the app will work
if __name__ == "__main__":
    app.run_server(host='0.0.0.0',port='8050', threaded=True)
