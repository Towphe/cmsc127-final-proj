import dash
from dash import Dash, html, dcc, callback, Output, Input, State
from furl import furl
from flask import redirect
from util.repository import Repository

dash.register_page(__name__, path="/establishments/edit")

repository = Repository()

layout = html.Div([
    html.H2('Establishment Edit View'),
    dcc.Location(id='url', refresh=False),
    html.Div(id="edit_establishment_content")
])

@dash.callback(Output('edit_establishment_content', 'children'), [Input('url', 'href')])
def _content(href:str):
    try:
        f = furl(href)
        eid = f.args['eid']

        return html.Div([
            html.Label('Establishment name'),
            dcc.Input(id='nef_name', name='nef_name', type='text'),
            html.Br(),
            dcc.Link(
            html.Button('Edit Establishment', id="edit_establishment_button"),
            href="/establishments", refresh=True)
        ])
    except:
        return html.H2(children="Establishment not found.")
        
@dash.callback([Input('edit_establishment_button', 'n_clicks'), Input('url', 'href')], [State('nef_name','value')])
def edit_establishment(n_clicks, href:str, name):
    f = furl(href)
    eid = f.args['eid']
    print(eid)
    print('goes here')
    print(name)
    repository.Establishment.update_establishment(eid, name)
    return