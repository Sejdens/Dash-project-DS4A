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
        opacity=0.5,
        labels={
            "Living_place": "Living place",
            "Household_composition": "Household composition",
        },
    )
cluster.update_layout(
    margin=dict(l=0, r=0, t=0, b=0),
)
cluster.update_traces(marker_size=6)
# Change legend names
for i in range(len(cluster.data)):
    cluster.data[i].name = "Grupo " + str(i + 1)

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
