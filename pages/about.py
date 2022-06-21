################################################################################################
# Libraries
################################################################################################
import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import pandas as pd
import plotly.express as px


################################################################################################
# Route
################################################################################################
register_page(__name__, path="/about")

################################################################################################
# Load the data and create the map
################################################################################################
df = pd.read_csv("./data/BASE_FINAL.csv")

###############
# Genero P6020
###############
dic_P6020 = { "1":"Male","2": "Female" }
df.P6020 = df.P6020.astype("str").replace(dic_P6020, regex=False)
genero = df[["P6020","FEX_C"]].groupby('P6020')['FEX_C'].sum().reset_index(name="Total") # con sum para sumar el factor de expancion
g = px.bar(
    x = "P6020",
    y = "Total",
    data_frame = genero,
    title = ("Distribution by Gender"),
)
# px.xlabel("Gender")
# px.ylabel("Population")
# px.xticks((0, 1), ("Male", "Female"))

################################################################################################
# Create Layout
################################################################################################
layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1(["Title"], id='title'),
            dcc.Graph(figure=g,id='main-figure'),
            dcc.Slider(min=0,max=1,marks={0:'US Map', 1:'Scatter Plot'},value=0,id='fig-slider',),
        ],
        lg=12,
        ),
    ]),
])
