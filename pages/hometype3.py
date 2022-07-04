import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash_labs.plugins import register_page
from dash import dcc,html, Input, Output, callback

register_page(__name__, path="/hometype3")

df = pd.read_csv("data/HOMETYPE_P4567.csv")
df["YEAR"] = df["YEAR"].astype(str)

hometype_p4567_bar = px.bar(
        data_frame=df,
        x="P4567",
        y="Index",
        color="YEAR",
        barmode="group",
        title="Index by Home Type per Year",
        labels={ "Home Type": "" },
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
                id="hometype-p4567-barplot",
                figure=hometype_p4567_bar,
                ),
        ],
        lg=8,
        className='card',
        ),
    ]),
])

@callback(
    Output("hometype-p4567-barplot", "figure"), 
    Input("years-checklist", "value"))
def filter_bar(filter):
##    fig = px.imshow(df[df["YEAR"].isin(filter)])
    fig = px.bar(
        data_frame=df[df["YEAR"].isin(filter)],
        x="P4567",
        y="Index",
        color="YEAR",
        barmode="group",
        title="Index by Home Type per Year",
        labels={ "Home Type": "" },
    )
    return fig
