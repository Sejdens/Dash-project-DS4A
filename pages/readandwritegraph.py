import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash_labs.plugins import register_page
from dash import dcc,html, Input, Output, callback

register_page(__name__, path="/readandwritegraph")

df = pd.read_csv("data/P6160.csv")
df["YEAR"] = df["YEAR"].astype(str)

readandwrite_bar = px.bar(
        data_frame=df,
        x="P6160",
        y="Index",
        color="YEAR",
        barmode="group",
        title="Index by the Ability to Read and Write per Year",
        labels={ "P6160": "" },
    )

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id="sex-barplot",
                figure=readandwrite_bar,
                ),
        ],
        lg=8,
        className='card',
        ),
    ]),
])