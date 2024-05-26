import dash
from dash import Dash, html, dcc, callback, Output, Input, State
from util.repository import Repository

dash.register_page(__name__, path="/establishments/add")

repository = Repository()

layout = html.Div([
    html.H2('Add New Establishment'),
    html.Div([
        html.Label('Establishment name'),
        dcc.Input(id='nef_name', name='nef_name', type='text'),
        html.Br(),
        html.Label('Added by'),
        dcc.Input(id='nef_added_by', name='nef_added_by', type='text'),
        html.Br(),
        dcc.Link(
        html.Button('Add Establishment', id="add_establishment_button"),
        href="/establishments",
        refresh=True)
    ]),
])

@callback(Input('add_establishment_button', 'n_clicks'), [State('nef_name','value'), State('nef_added_by', 'value')])
def add_establishment(n_clicks, name, added_by):
    repository.Establishment.add_establishment(added_by, name)
    return