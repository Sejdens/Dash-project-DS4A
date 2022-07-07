import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash_labs.plugins import register_page
from dash import dcc,html

register_page(__name__, path="/multidimensional_cluster")

df = pd.read_csv("data/cluster.csv")

cluster = px.scatter_3d(
        data_frame=df,
        x="Household_composition",
        y="Living_place",
        z="Education",
        color="Cluster",
        size_max=1,
        opacity=0.5,
        labels={
          "Living_place": "Living place",
          "Household_composition": "Household composition",
          },
    )

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Index by Education, Living Place and Household Composition"),
            dcc.Graph(
                id="cluster",
                figure=cluster,
                ),
        ],
        lg=8,
        className='card align-items-center',
        ),
    ],
    className="justify-content-center",
    ),
])
