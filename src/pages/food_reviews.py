import dash
from dash import Dash, html, dcc, callback, Output, Input

dash.register_page(__name__, path="/foods/reviews")

layout = html.Div([
    html.H2('Food Reviews View')
])