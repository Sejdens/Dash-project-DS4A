################################################################################################
# Libraries
################################################################################################
import dash
from dash import Dash, html, dcc
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
    redirect_from=["/about"],
)

################################################################################################
# Load the data and create the map
################################################################################################
df = pd.read_csv("./data/BASE_FINAL.csv")

###############
# Genero P6020
###############
dic_P6020 = {"1": "Male", "2": "Female"}
df.P6020 = df.P6020.astype("str").replace(dic_P6020, regex=False)
genero = df[["P6020", "FEX_C"]].groupby('P6020')['FEX_C'].sum().reset_index(
    name="Total")  # con sum para sumar el factor de expancion
g = px.bar(
    x="P6020",
    y="Total",
    data_frame=genero,
    title=("Distribution by Gender"),
)
# px.xlabel("Gender")
# px.ylabel("Population")
# px.xticks((0, 1), ("Male", "Female"))

kpi_total = kpicard("Total population", "7'428.432", "person.svg")
kpi_vul = kpicard("Vulnerable People", "523.435", "charity.svg")

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
                kpi_total.display(),
                kpi_vul.display(),
            ])
        ]),
    ]),
])
