import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash_labs.plugins import register_page
from dash import dcc, html, Input, Output, callback

register_page(__name__, path="/municipal_type")

df = pd.read_csv("data/CLASE.csv")
df["YEAR"] = df["YEAR"].astype(str)

clase_bar = px.bar(
        data_frame=df,
        x="CLASE",
        y="Index",
        color="YEAR",
        barmode="group",
        labels={ "CLASE": "" },
    )

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Index by Municipal Type"),
            dcc.Checklist(
                ['2018', '2019', '2020','2021'],
                ['2018', '2019', '2020','2021'],
                inline=True,
                id="clase-checklist",
                labelClassName="px-2",
                inputClassName="mx-1",
            ),
            dcc.Graph(
                id="clase-barplot",
                figure=clase_bar,
                ),
        ],
        lg=8,
        className='card align-items-center',
        ),
    ]),
])

@callback(
    Output("clase-barplot", "figure"), 
    Input("clase-checklist", "value"))
def filter_bar(filter):
    fig = px.bar(
        data_frame=df[df["YEAR"].isin(filter)],
        x="CLASE",
        y="Index",
        color="YEAR",
        barmode="group",
        labels={ "CLASE": "" },
    )
    return fig
