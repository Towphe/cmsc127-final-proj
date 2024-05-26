from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd

# TRY APPROACH: create pandas dataframe of tuples here

def generate_table(dataframe: pd.DataFrame, column_names:list, element_name:str, pk_name:str):
    column_names.insert(len(column_names), 'Edit')
    column_names.insert(len(column_names), 'Delete')
    
    rows = []

    for i in range(len(dataframe)):

        # html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        row_to_add = []
        for j in range(len(column_names)):
            if j == len(column_names) - 1:
                # delete button
                row_to_add.append(html.Td(dcc.Link(html.Button('delete'), refresh=True, href=f"/{element_name}/delete?eid={dataframe.iloc[i][pk_name]}")))
            elif j == len(column_names) - 2:
                # edit button
                row_to_add.append(html.Td(dcc.Link(html.Button('edit'), refresh=True, href=f"/{element_name}/edit?eid={dataframe.iloc[i][pk_name]}")))
            else:
                row_to_add.append(html.Td(dataframe.iloc[i][dataframe.columns[j]]))
        rows.append(html.Tr(row_to_add))

    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in column_names])
        ),
        html.Tbody(rows)
    ])