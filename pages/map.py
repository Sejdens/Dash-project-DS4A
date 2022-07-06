import json
from urllib.request import urlopen
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
from dash_labs.plugins import register_page
from dash import dcc, html, Input, Output, callback

with urlopen('https://gist.githubusercontent.com/john-guerra/43c7656821069d00dcbc/raw/be6a6e239cd5b5b803c6e7c2ec405b793a9064dd/Colombia.geo.json') as response:
    counties = json.load(response)

register_page(__name__, path="/map")

dptos = pd.read_csv("data/dptos.csv", dtype={ "P1_DEPARTAMENTO": str })
locs = dptos[dptos["YEAR"] == 2018]['P1_DEPARTAMENTO']

for loc in counties['features']:
    loc['id'] = loc['properties']['DPTO']
fig = go.Figure(
    go.Choroplethmapbox(
            geojson=counties,
            locations=locs,
            z=dptos[dptos["YEAR"] == 2021]['Index'],
            colorscale='Viridis',
            colorbar_title="Index 2021",
        )
    )
fig.update_layout(
    mapbox_style="carto-positron",
    mapbox_zoom=3.4,
    mapbox_center = { "lat": 4.570868, "lon": -74.2973328 },
)

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Index by Department per Year"),
            dcc.Graph(
                id="map-graph",
                figure=fig,
                ),
            dcc.Slider(
                marks={
                    2018: "2018",
                    2019: "2019",
                    2020: "2020",
                    2021: "2021",
                },
                step=1,
                value=2021,
                id="map-years",
                updatemode="drag",
                className="w-75",
            ),
        ],
        lg=8,
        className='card m-1 align-items-center',
        ),
    ], className='justify-content-center' ),
])

@callback(
    Output("map-graph", "figure"), 
    Input("map-years", "value"))
def filter_bar(filter):
    fig = go.Figure(
        go.Choroplethmapbox(
                geojson=counties,
                locations=locs,
                z=dptos[dptos["YEAR"] == filter]['Index'],
                colorscale='Viridis',
                colorbar_title=f"Index {filter}",
            )
        )
    fig.update_layout(
        mapbox_style="carto-positron",
        mapbox_zoom=3.4,
        mapbox_center={ "lat": 4.570868, "lon": -74.2973328 },
    )
    return fig
