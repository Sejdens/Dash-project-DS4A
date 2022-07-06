import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash_labs.plugins import register_page
from dash import dcc, html, Input, Output, callback

register_page(__name__, path="/ethnicity")

df = pd.read_csv("data/ETHNICITY.csv")
df["YEAR"] = df["YEAR"].astype(str)

ethnicity_bar = px.bar(
        data_frame=df,
        x="P6080",
        y="Index",
        color="YEAR",
        barmode="group",
        labels={ "P6080": "" },
    )

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Index by Ethnicity"),
            dcc.Checklist(
                ['2018', '2019', '2020','2021'],
                ['2018', '2019', '2020','2021'],
                inline=True,
                id="years-checklist",
                labelClassName="px-2",
                inputClassName="mx-1",
            ),
            dcc.Graph(
                id="ethnicity-barplot",
                figure=ethnicity_bar,
                ),
        ],
        lg=8,
        className='card align-items-center',
        ),
    ]),
])

@callback(
    Output("ethnicity-barplot", "figure"),
    Input("years-checklist", "value"))
def filter_bar(filter):
    fig = px.bar(
        data_frame=df[df["YEAR"].isin(filter)],
        y="P6080",
        x="Index",
        color="YEAR",
        barmode="group",
        labels={ "P6080": "" },
    )
    return fig
