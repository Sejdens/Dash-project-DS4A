import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash_labs.plugins import register_page
from dash import dcc, html, Input, Output, callback

register_page(__name__, path="/radial")

df = pd.read_csv("data/radial.csv")
df["YEAR"] = df["YEAR"].astype(str)

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
            html.H2("Index by Dimension"),
            dcc.Checklist(
                ['2018', '2019', '2020','2021'],
                ['2018', '2019', '2020','2021'],
                inline=True,
                id="radial-checklist",
                labelClassName="px-2",
                inputClassName="mx-1",
            ),
            dcc.Graph(
                id="dimensions-radial",
                figure=dimensions_radial,
                className="img-fluid",
            ),
        ],
        lg=8,
        className='card align-items-center',
        ),
    ], className='justify-content-center'),
])

@callback(
    Output("dimensions-radial", "figure"),
    Input("radial-checklist", "value"))
def filter_bar(filter):
    fig = px.line_polar(
        data_frame=df[df["YEAR"].isin(filter)],
        r="Index",
        theta="Dimension",
        color="YEAR",
        line_close=True,
    )
    return fig
