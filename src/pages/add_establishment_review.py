# import dash
# from dash import Dash, html, dcc, callback, Output, Input, State, MATCH
# from util.repository import Repository
# from furl import furl
# from flask import redirect

# dash.register_page(__name__, path="/establishments/review/add")

# repository = Repository()

# layout = html.Div([
#     html.H2('Add Establishment Review'),
#     dcc.Location(id='url', refresh=False),
#     html.Div(id="add_establishment_review_content")
# ])

# @callback(Output('add_establishment_review_content', 'children'), [Input('url', 'href')])
# def _content(href:str):
#     # ner   -   new establishment review
#     try:
#         f = furl(href)
#         eid = f.args['eid']

#         return html.Div([
#             html.Label('Reviewer'),
#             dcc.Input(id='ner_reviewer', name='ner_reviewer', type='text'),
#             # html.Br(),
#             # html.Label('Contente'),
#             # dcc.Input(id='ner_content', name='ner_content', type='text'),
#             # html.Br(),
#             # html.Label('Rating'),
#             # dcc.Input(id='ner_rating', name='ner_rating', type='number'),
#             html.Br(),
#             dcc.Link(
#                 html.Button('Add Review', id="review_establishment_button"),
#             href="/establishments", refresh=True)
#         ])
#     except:
#         return html.H2(children="Establishment not found.")

# #@callback(Input({"type":"review_establishment_button","index": MATCH}, "n_clicks"))
# @dash.callback([Input("review_establishment_button", "n_clicks"), Input('url', 'href')])
# def add_establishment_review(n_clicks):  # n_clicks, href:str, reviewer   # ner_reviewer, ner_content, ner_rating, href:str
#     # f = furl(href)
#     # eid = f.args['eid']
#     # print(eid)
#     print("goes here")
#     return


import dash
from dash import Dash, html, dcc, callback, Output, Input, State
from furl import furl
from flask import redirect
from util.repository import Repository

dash.register_page(__name__, path="/establishments/review/add")

repository = Repository()

layout = html.Div([
    html.H2('Establishment Edit View'),
    dcc.Location(id='url', refresh=False),
    html.Div(id="review_establishment_content")
])

@dash.callback(Output('review_establishment_content', 'children'), [Input('url', 'href')])
def _content(href:str):
    try:
        f = furl(href)
        eid = f.args['eid']

        return html.Div([
            html.Label('Establishment name'),
            dcc.Input(id='nef_name', name='nef_name', type='text'),
            html.Br(),
            dcc.Link(
                html.Button('Edit Establishment', id="review_establishment_button"),
            href="/establishments", refresh=True)   
        ])
    except:
        return html.H2(children="Establishment not found.")
        
@dash.callback([Input('review_establishment_button', 'n_clicks'), Input('url', 'href')], [State('nef_name','value')])
def edit_establishment(n_clicks, href:str, name):
    f = furl(href)
    eid = f.args['eid']
    print(eid)
    print('goes here')
    print(name)
    repository.Establishment.update_establishment(eid, name)
    return


#@dash.callback([Input('create_review', 'n_clicks'), Input('url', 'href')], [State('ner_author','value'), State('ner_content','value'), State('ner_rating','value')])