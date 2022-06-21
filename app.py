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
request_path_prefix = None
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.FLATLY],
    requests_pathname_prefix=request_path_prefix,
    plugins=[dl.plugins.pages],
    meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}]
)

################################################################################################
# Navbar
################################################################################################
navbar = dbc.NavbarSimple([
    dbc.NavItem(dbc.NavLink("Home", href=request_path_prefix)),
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=request_path_prefix+page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="Data Science",
    ),
    dbc.NavItem(dbc.NavLink("Us", href=request_path_prefix+"/us")),
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
    app.run_server(host='0.0.0.0',port='8050', debug=True, threaded=True)
