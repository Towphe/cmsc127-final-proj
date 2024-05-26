import dash
from dash import Dash, html, dcc, callback, Output, Input

dash.register_page(__name__, path="/establishments/reviews")

layout = html.Div([
    html.H2('Establishment Reviews View')
])