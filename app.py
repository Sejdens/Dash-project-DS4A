################################################################################################
# Libraries
################################################################################################
import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
import os

# import numpy as np
# import json
# import plotly.express as px
# from datetime import datetime as dt
# from IPython.core.display import display, HTML

# import warnings

# from dash import Dash, callback, html, dcc, dash_table, Input, Output, State, MATCH, ALL #, ClientsideFunction
# import dash_labs as dl
# import dash_bootstrap_components as dbc

# import pandas as pd
# import json
# import os

################################################################################################
# Instance declaration
################################################################################################
request_path_prefix = "/"
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.FLATLY],
    plugins=[dl.plugins.pages],
    meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}]
)

################################################################################################
# Navbar
################################################################################################
dropdown_exclude = ["pages.not_found_404", "pages.home", "pages.team"]
navbar = dbc.NavbarSimple([
    dbc.NavItem(dbc.NavLink("Home", href=request_path_prefix)),
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] not in dropdown_exclude
        ],
        nav=True,
        label="Index Graphs",
    ),
    dbc.NavItem(dbc.NavLink("Team", href=request_path_prefix+"team")),
    ],
    brand="DS4A Project - Team 148",
    color="primary",
    dark=True,
    className="mb-2",
)

################################################################################################
# Main layout
################################################################################################
app.layout = dbc.Container(
    [
        navbar,
        dl.plugins.page_container,
    ],
    className="dbc",
    fluid=True,
)

################################################################################################
# Register Callbacks
################################################################################################
# register_callbacks(app)

################################################################################################
# Initiate the server where the app will work
#################################################################################################
server = app.server

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port='8050',
        debug=True,
    )
