import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import seaborn as sns
from dash_labs.plugins import register_page
from dash import dcc

register_page(__name__, path="/sexgraph")

df = pd.read_csv("data/MERGE_FINAL_YEARS_FILTER_SEX.csv")
df.P6020 = df.P6020.astype("str").replace({"1.0":"Male","2.0": "Female"}, regex=False)
df["YEAR"] = df["YEAR"].astype(int)

sex_bar = px.box(
        x = "P6020",
        y = "Index",
        data_frame = df,
        color = "YEAR",
        boxmode="group",
        title="Index by Gender per Year",
        labels={ "P6020": "" },
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
