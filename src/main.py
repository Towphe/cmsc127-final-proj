import dash
from dash import Dash, html, dcc, callback, Output, Input
import mariadb
import sys

# initialize app
app = Dash(__name__, use_pages=True)

app.layout = [
    html.H1(children='Food App', style={'textAlign':'center'}),
    dash.page_container
]

# run app
if __name__ == '__main__':
    
    app.run(debug=True)
