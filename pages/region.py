import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash_labs.plugins import register_page
from dash import dcc, html, Input, Output, callback

register_page(__name__, path="/region")

df = pd.read_csv("data/REGION.csv")
df["YEAR"] = df["YEAR"].astype(str)

region_bar = px.bar(
        data_frame=df,
        x="REGION",
        y="Index",
        color="YEAR",
        barmode="group",
        title="Index by Region per Year",
        labels={ "REGION": "" },
    )

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Index by Region"),
            dcc.Checklist(
                ['2018', '2019', '2020','2021'],
                ['2018', '2019', '2020','2021'],
                inline=True,
                id="region-checklist",
                labelClassName="px-2",
                inputClassName="mx-1",
            ),
            dcc.Graph(
                id="region-barplot",
                figure=region_bar,
                ),
        ],
        lg=8,
        className='card align-items-center',
        ),
    ], className='justify-content-center'),
])

@callback(
    Output("region-barplot", "figure"),
    Input("region-checklist", "value"))
def filter_bar(filter):
    fig = px.bar(
        data_frame=df[df["YEAR"].isin(filter)],
        x="REGION",
        y="Index",
        color="YEAR",
        barmode="group",
        labels={ "REGION": "" },
    )
    return fig
