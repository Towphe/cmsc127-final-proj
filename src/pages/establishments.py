import tkinter as tk
import pandas as pd
from pandastable import Table, TableModel

def render_establishments(establishments: pd.DataFrame, add_establishment, home, window:tk.Tk):
    welcome_message = tk.Label(text="Establishments View")

    back_button = tk.Button(text="Back", command=lambda: home())

    # render table
    table = tk.LabelFrame()

    tk.Label(table, text="Id", anchor="w").grid(row=0, column=0, sticky="ew")
    tk.Label(table, text="Name", anchor="w").grid(row=0, column=1, sticky="ew")
    tk.Label(table, text="Added by", anchor="w").grid(row=0, column=2, sticky="ew")
    tk.Label(table, text="Average", anchor="w").grid(row=0, column=3, sticky="ew")
    tk.Label(table, text="Edit", anchor="w").grid(row=0, column=4, sticky="ew")
    tk.Label(table, text="Delete", anchor="w").grid(row=0, column=5, sticky="ew")

    row = 1
    for i in range(establishments.shape[0]):
        # print(establishments.iloc[i]['establishment_id']) # rendered as python dictionary
        establishment = establishments.iloc[i]
        id_label = tk.Label(table, text=str(establishment['establishment_id']), anchor="w")
        name_label = tk.Label(table, text=establishment['establishment_name'], anchor="w")
        added_by_label = tk.Label(table, text=establishment['added_by'], anchor="w")
        average_rating_label = tk.Label(table, text=establishment['average_rating'], anchor="w")
        edit_button = tk.Button(table, text="Edit", anchor="w")
        delete_button = tk.Button(table, text="Delete", anchor="w")

        # render rows
        id_label.grid(row=row, column=0, sticky="ew")
        name_label.grid(row=row, column=1, sticky="ew")
        added_by_label.grid(row=row, column=2, sticky="ew")
        average_rating_label.grid(row=row, column=3, sticky="ew")
        edit_button.grid(row=row, column=4, sticky="ew")
        delete_button.grid(row=row, column=5, sticky="ew")

        row += 1
    
    add_button = tk.Button(text="Add New Establishment", command=lambda: add_establishment())

    welcome_message.pack()
    back_button.pack()
    table.pack()
    add_button.pack()

def render_add_establishment(establishments, window:tk.Tk):
    back_button = tk.Button(text="Back", command=lambda: establishments())
    title = tk.Label(text="Add Establishment")

    title.pack()
    back_button.pack()