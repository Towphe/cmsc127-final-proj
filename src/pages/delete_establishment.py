import dash
from dash import Dash, html, dcc, callback, Output, Input, State
from furl import furl
from flask import redirect
from util.repository import Repository

dash.register_page(__name__, path="/establishments/delete")

repository = Repository()

layout = html.Div([
    dcc.Location(id='url', refresh=False),  # makes url available
    html.Div(id="del_establishment_content")
])

@dash.callback(Output('del_establishment_content', 'children'), [Input('url', 'href')])
def _content(href:str):
    try:
        f = furl(href)
        eid = f.args['eid']

        return html.Div([
            html.H2('Delete establishment?'),
            dcc.Link(
            html.Button('Delete', id="delete_establishment_button"),
            href="/establishments", refresh=True),
        ])
    except:
        return html.H2(children="Establishment not found.")
        
@dash.callback([Input('delete_establishment_button', 'n_clicks'), Input('url', 'href')])
def delete_establishment(n_clicks, href:str):
    f = furl(href)
    eid = f.args['eid']
    print(f"deleted {eid}")
    repository.Establishment.remove_establishment(eid)
    return