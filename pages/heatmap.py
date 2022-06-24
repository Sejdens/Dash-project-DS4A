import dash
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page

from components.kpi.kpicard import kpicard

register_page(__name__, path="/heatmaps")

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

df = px.data.medals_wide(indexed=True)
kpi_total = kpicard("Total population", "7'428.432", "person.svg")
kpi_vul = kpicard("Vulnerable People", "523.435", "charity.svg")

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.P("Medals included:"),
            dcc.Dropdown(
                id="heatmaps-medals",
                options=[
                    {"label": "GOLD", "value": "gold"},
                    {"label": "SILVER", "value": "silver"},
                    {"label": "BRONZE", "value": "bronze"},
                ],
                value=['gold', 'silver', 'bronze'],
                multi = True
            ),
            dcc.Graph(id="heatmaps-graph"),
        ],
        lg=8,
        className='card',
        ),
        dbc.Col([
            kpi_total.display(),
            kpi_vul.display(),
        ],
        lg=4,
        )
    ]),
])

@callback(
    Output("heatmaps-graph", "figure"), 
    Input("heatmaps-medals", "value"))
def filter_heatmap(cols):
    fig = px.imshow(df[cols])
    return fig
