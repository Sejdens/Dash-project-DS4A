import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash_labs.plugins import register_page
from dash import dcc, html, Input, Output, callback

register_page(__name__, path="/readandwritegraph")

df = pd.read_csv("data/P6160.csv")
df["YEAR"] = df["YEAR"].astype(str)

readandwrite_bar = px.bar(
        data_frame=df,
        x="P6160",
        y="Index",
        color="YEAR",
        barmode="group",
        labels={ "P6160": "" },
    )

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Index by the Ability to Read and Write"),
            dcc.Checklist(
                ['2018', '2019', '2020','2021'],
                ['2018', '2019', '2020','2021'],
                inline=True,
                id="readwrite-checklist",
                labelClassName="px-2",
                inputClassName="mx-1",
            ),
            dcc.Graph(
                id="readwrite-barplot",
                figure=readandwrite_bar,
                ),
        ],
        lg=8,
        className='card align-items-center',
        ),
    ]),
])

@callback(
    Output("readwrite-barplot", "figure"),
    Input("readwrite-checklist", "value"))
def filter_bar(filter):
    fig = px.bar(
        data_frame=df[df["YEAR"].isin(filter)],
        x="P6160",
        y="Index",
        color="YEAR",
        barmode="group",
        labels={ "P6160": "" },
    )
    return fig
