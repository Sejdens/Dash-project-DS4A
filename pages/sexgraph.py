import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash_labs.plugins import register_page
from dash import dcc

register_page(__name__, path="/sexgraph")

merge = pd.read_csv("data/MERGE_FINAL_YEARS_FILTER_SEX.csv")
merge.P6020 = merge.P6020.astype("str").replace({"1.0":"Male","2.0": "Female"}, regex=False)
merge["YEAR"] = merge["YEAR"].astype(int)

sex_bar = px.box(
        x = "P6020",
        y = "Index",
        data_frame = merge,
        color = "YEAR",
        boxmode="group",
        title="Index by Gender per Year",
        labels={ "Sex": "" },
    )

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            dcc.Graph(
                id="sex-barplot",
                figure=sex_bar,
                ),
        ],
        lg=8,
        className='card',
        ),
    ]),
])
