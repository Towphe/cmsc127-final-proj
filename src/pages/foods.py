import dash
from dash import Dash, html, dcc, callback, Output, Input

dash.register_page(__name__, pash="/foods/")

layout = html.Div([
    html.H2('Food Items View')
])