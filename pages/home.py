################################################################################################
# Libraries
################################################################################################
import dash
from dash import Dash, html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import pandas as pd
import plotly.express as px

################################################################################################
# Import components
################################################################################################
from components.kpi.kpicard import kpicard

################################################################################################
# Route
################################################################################################
register_page(
    __name__,
    path="/",
    redirect_from=["/home", "/about"],
)

################################################################################################
# Load the data and create the map
################################################################################################
df = pd.read_csv("./data/DATA_KPI.csv", dtype = {"YEAR": str, "FEX_C": int})


# px.xlabel("Gender")
# px.ylabel("Population")
# px.xticks((0, 1), ("Male", "Female"))

## df[["YEAR", "FEX_C"]].groupby('YEAR')['FEX_C'].sum().astype(str)

kpi_total = kpicard("Total population", "7'428.432", "person.svg", "total-population")

semaforo = html.Div(
    dbc.Container(
        [
            html.P(
                "vulnerability level indicator",
                className="lead",
            ),
            html.P(
                """Greem: Less vulnerability
                Yellow: Medium vulnerability
                Red: High vulnerability"""
            ),
            html.Hr(className="my-2"),

            html.Div([
                html.P("test",id="less-vulnerable")
            ], className="test rounded-circle bg-success text-center align-items-center justify-content-center m-auto d-flex"),

            html.Hr(className="my-2"),
            html.Div([
                html.P("test",id="medium-vulnerable" )
            ], className="test yellow rounded-circle bg-warning text-center m-auto align-items-center justify-content-center d-flex"),
            html.Hr(className="my-2"),
            html.Div([
                html.P("test",id="high-vulnerable" )
            ], className="test red rounded-circle bg-danger text-center m-auto align-items-center justify-content-center d-flex"),
        ],
        fluid=True,
        className="py-3",
    ),
    className="p-3 bg-light rounded-3",
)
################################################################################################
# Create Layout
################################################################################################
layout = dbc.Container([
    dbc.Row([
        dbc.Row([
            html.H2("Social Vulnerability Index for the Elderly ")
        ], className="display-4 text-center"),
        dbc.Row([
            dbc.Col([
                dbc.Container([
                    html.H4("What is social vulnerability?"),
                    html.P(
                        """Social vulnerability is the result of the impacts caused by the current development pattern, but it also expresses the inability of the weakest groups in society to face them, neutralize them or obtain benefits from them. """
                    ),
                    html.H4(
                        "Why a vulnerability index in adults over 60 years of age?"),
                    html.P(
                        """Although it is complex to establish why one age group is more vulnerable than another, it is evident that, specifically in old age, conditions appear that generate disadvantages or weaknesses to face unfavorable situations."""
                    ),
                    html.H4(
                        "Multidimensional Index of Vulnerability in Older Adults (“IMV”)"),
                    html.P(
                        """For the construction of the multidimensional vulnerability index, the 2021 Quality of Life Survey (ECV) will be used as a source of information, which is carried out by the National Administrative Department of Statistics (DANE) in 9 main regions of Colombia."""
                    ),
                    html.P(
                        """The calculation of the Multidimensional Vulnerability Index can be established as a weighted average per person over 60 years of age, in which 8 equally weighted dimensions are considered (the sum of all of them is 1)."""
                    ),
                ],
                    fluid=True,
                    className="p-2 bg-light rounded-3",
                ),

            ], width={"size": 8}),
            dbc.Col([
                html.P("Years:"),
                dcc.RadioItems(
                    ['2018', '2019', '2020', '2021'],
                    '2021',
                    id="years-radiogroup"
                ),
                kpi_total.display(),
                semaforo,
            ])
        ]),
    ]),
])


@callback(
    Output("less-vulnerable", "children"),
    Output("medium-vulnerable", "children"),
    Output("high-vulnerable", "children"),
    Output("total-population", "children"),
    Input("years-radiogroup", "value"))
def lessVulnerable(filter):
    less = df[(df["YEAR"] == filter) & (df["VulnerabilityLevel"] == "Low")]["FEX_C"].values[0]
    medium = df[(df["YEAR"] == filter) & (df["VulnerabilityLevel"] == "Medium")]["FEX_C"].values[0]
    high = df[(df["YEAR"] == filter) & (df["VulnerabilityLevel"] == "High")]["FEX_C"].values[0]
    total = df[df["YEAR"] == filter].groupby('YEAR')['FEX_C'].sum().values[0]
    return format(less, ","), format(medium, ","), format(high, ","), format(total, ",")
