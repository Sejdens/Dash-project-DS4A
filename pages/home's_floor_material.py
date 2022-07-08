import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash_labs.plugins import register_page
from dash import dcc,html, Input, Output, callback

register_page(__name__, path="/home_floor")

df = pd.read_csv("data/HOMETYPE_P4015.csv")
df["YEAR"] = df["YEAR"].astype(str)

hometype_p4015_bar = px.bar(
        data_frame=df,
        x="P4015",
        y="Index",
        color="YEAR",
        barmode="group",
        labels={ "P4015": "" },
    )

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Index by Home's Floor Material"),
            dcc.Checklist(
                ['2018', '2019', '2020','2021'],
                ['2018', '2019', '2020','2021'],
                inline=True,
                id="P4015-checklist",
                labelClassName="px-2",
                inputClassName="mx-1",
            ),
            dcc.Graph(
                id="hometype-p4015-barplot",
                figure=hometype_p4015_bar,
                className="img-fluid",
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
    Output("hometype-p4015-barplot", "figure"), 
    Input("P4015-checklist", "value"))
def filter_bar(filter):
    fig = px.bar(
        data_frame=df[df["YEAR"].isin(filter)],
        x="P4015",
        y="Index",
        color="YEAR",
        barmode="group",
        labels={ "P4015": "" },
    )
    return fig
