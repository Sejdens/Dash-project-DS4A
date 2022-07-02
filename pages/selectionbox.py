import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash_labs.plugins import register_page
from dash import dcc

register_page(__name__, path="/graph")

df = pd.read_csv("data/CLASE.csv")
df["YEAR"] = df["YEAR"].astype(str)

clase_bar = px.bar(
        data_frame=df,
        x="CLASE",
        y="Index",
        color="YEAR",
        barmode="group",
        title="Index by Municipal Type per Year",
        labels={ "CLASE": "" },
    )

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id="clase-barplot",
                figure=clase_bar,
                ),
        ],
        lg=8,
        className='card',
        ),
    ]),
])
