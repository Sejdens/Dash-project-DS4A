from distutils.command.config import config
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash_labs.plugins import register_page
from dash import dcc, html

register_page(__name__, path="/gender")

df = pd.read_csv("data/MERGE_FINAL_YEARS_FILTER_SEX.csv")
df["YEAR"] = df["YEAR"].astype(int)

gender_box = px.box(
        x = "P6020",
        y = "Index",
        data_frame = df,
        color = "YEAR",
        boxmode="group",
        labels={ "P6020": "" },
    )

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Index by Gender"),
            dcc.Graph(
                id="gender-boxplot",
                figure=gender_box,
                ),
        ],
        lg=8,
        className='card align-items-center',
        ),
    ],
    className="justify-content-center",
    ),
])
