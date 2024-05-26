import dash
from dash import Dash, html, dcc, callback, Output, Input, dash_table
from util.repository import Repository
import pandas as pd
from util.generate_table import generate_table

repository = Repository()
dash.register_page(__name__, path="/establishments")

def serve_layout():
    return html.Div([
        html.H2('Establishments view', id="title"),
        generate_table(repository.Establishment.get_establishments(), ['Id', 'Added by', 'Establishment Name', 'Average Rating'], "establishments", 'establishment_id'),
        html.Div([
        dcc.Link(html.Button('Add New Establishment'), href="/establishments/add", refresh=True)
    ])
])

layout = serve_layout