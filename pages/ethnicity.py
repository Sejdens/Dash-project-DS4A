import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash_labs.plugins import register_page
from dash import dcc,html, Input, Output, callback

register_page(__name__, path="/ethnicity")

df = pd.read_csv("data/ETHNICITY.csv")
df["YEAR"] = df["YEAR"].astype(str)

ethnicity_bar = px.bar(
        data_frame=df,
        x="P6080",
        y="Index",
        color="YEAR",
        barmode="group",
        title="Index by Ethnicity per Year",
        labels={ "P6080": "" },
    )

layout = dbc.Container([
    dbc.Row([
        html.P("Years:"),
        dcc.Checklist(
            ['2018', '2019', '2020','2021'],
            ['2018', '2019', '2020','2021'],
            inline=True,
            id="years-checklist"
        ),
        dbc.Col([
            dcc.Graph(
                id="ethnicity-barplot",
                figure=ethnicity_bar,
                ),
        ],
        lg=8,
        className='card',
        ),
    ]),
])

@callback(
    Output("ethnicity-barplot", "figure"), 
    Input("years-checklist", "value"))
def filter_bar(filter):
##    fig = px.imshow(df[df["YEAR"].isin(filter)])
    fig = px.bar(
        data_frame=df[df["YEAR"].isin(filter)],
        y="P6080",
        x="Index",
        color="YEAR",
        barmode="group",
        title="Index by Ethnicity per Year",
        labels={ "P6080": "" },
    )
    return fig
