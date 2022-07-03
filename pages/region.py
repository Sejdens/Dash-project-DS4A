import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash_labs.plugins import register_page
from dash import dcc

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
            dcc.Graph(
                id="region-barplot",
                figure=region_bar,
                ),
        ],
        lg=8,
        className='card',
        ),
    ]),
])
