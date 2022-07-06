import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash_labs.plugins import register_page
from dash import dcc,html, Input, Output, callback

register_page(__name__, path="/home_type")

df = pd.read_csv("data/HOMETYPE_P1070.csv")
df["YEAR"] = df["YEAR"].astype(str)

hometype_p1070_bar = px.bar(
        data_frame=df,
        x="P1070",
        y="Index",
        color="YEAR",
        barmode="group",
        labels={ "P1070": "" },
    )

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Index by Home Type"),
            dcc.Checklist(
                ['2018', '2019', '2020','2021'],
                ['2018', '2019', '2020','2021'],
                inline=True,
                id="p1070-checklist",
                labelClassName="px-2",
                inputClassName="mx-1",
            ),
            dcc.Graph(
                id="hometype-p1070-barplot",
                figure=hometype_p1070_bar,
                ),
        ],
        lg=8,
        className='card align-items-center',
        ),
    ],
    className="justify-content-center",
    ),
])

@callback(
    Output("hometype-p1070-barplot", "figure"), 
    Input("p1070-checklist", "value"))
def filter_bar(filter):
    fig = px.bar(
        data_frame=df[df["YEAR"].isin(filter)],
        x="P1070",
        y="Index",
        color="YEAR",
        barmode="group",
        labels={ "P1070": "" },
    )
    return fig
