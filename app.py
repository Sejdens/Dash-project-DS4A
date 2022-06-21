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
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.FLATLY],
    plugins=[dl.plugins.pages],
    meta_tags=[{'name':'viewport', 'content':'width=device-width, initial-scale=1.0'}]
)


################################################################################################
# Initiate the server where the app will work
#################################################################################################
server = app.server

if __name__ == "__main__":
    app.run_server(host='0.0.0.0',port='8050', debug=True, threaded=True)
