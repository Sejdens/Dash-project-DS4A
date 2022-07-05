import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash_labs.plugins import register_page
from dash import dcc

register_page(__name__, path="/radial")

df = pd.read_csv("data/radial.csv")

dimensions_radial = px.line_polar(
        data_frame=df,
        r="Index",
        theta="Dimension",
        color="YEAR",
        line_close=True,
    )

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id="dimensions-radial",
                figure=dimensions_radial,
                ),
        ],
        lg=8,
        className='card',
        ),
    ]),
])
