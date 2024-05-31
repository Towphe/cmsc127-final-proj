import tkinter as tk
import pandas as pd
from pandastable import Table, TableModel
from util.repository import Repository

def render_establishments(username:str, establishments: pd.DataFrame, add_establishment, home, window:tk.Tk, redirect_to_edit_establishment, repository:Repository, clear_page, redirect_to_establishments):
    
    def delete_establishment(establishment_id:int):
        repository.Establishment.remove_establishment(establishment_id)
        clear_page()
        redirect_to_establishments()
        return

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
        edit_button = tk.Button(table, text="Edit", anchor="w", command=lambda eid=establishment["establishment_id"]: redirect_to_edit_establishment(eid))
        delete_button = tk.Button(table, text="Delete", anchor="w", command=lambda eid=establishment["establishment_id"]: delete_establishment(eid))
        review_button = tk.Button(table, text="Review", anchor="w")

        if establishment["added_by"] != username:
            # disable edit/delete when username != current login
            edit_button.config(state=tk.DISABLED, bg='grey')
            delete_button.config(state=tk.DISABLED, bg='grey')
        else:
            review_button.config(state=tk.DISABLED, bg='grey')

        # render rows
        id_label.grid(row=row, column=0, sticky="ew")
        name_label.grid(row=row, column=1, sticky="ew")
        added_by_label.grid(row=row, column=2, sticky="ew")
        average_rating_label.grid(row=row, column=3, sticky="ew")

        edit_button.grid(row=row, column=4, sticky="ew")
        delete_button.grid(row=row, column=5, sticky="ew")
        review_button.grid(row=row, column=6, sticky="ew")

        row += 1
    
    add_button = tk.Button(text="Add New Establishment", command=lambda: add_establishment())

    welcome_message.pack()
    back_button.pack()
    table.pack()
    add_button.pack()

def render_add_establishment(username:str, establishments:pd.DataFrame, repository:Repository, window:tk.Tk, render_establishments):
    def create_establishment():
        establishment_name = establishment_name_entry.get()
        repository.Establishment.add_establishment(username, establishment_name)
        render_establishments()
    
    back_button = tk.Button(text="Back", command=lambda: establishments())
    title = tk.Label(text="Add Establishment")

    establishment_name_label = tk.Label(text="Establishment Name")
    establishment_name_entry = tk.Entry()
    create_establishment_button = tk.Button(text="Create Establishment", command=lambda: create_establishment())

    title.pack()
    back_button.pack()
    establishment_name_label.pack()
    establishment_name_entry.pack()
    create_establishment_button.pack()

def render_edit_establishment(establishment_id:int, establishments:pd.DataFrame, repository:Repository, window:tk.Tk, render_establishments):
    def edit_establishment():
        establishment_name = establishment_name_entry.get()
        repository.Establishment.update_establishment(establishment_id, establishment_name)
        render_establishments()
    
    back_button = tk.Button(text="Back", command=lambda: establishments())
    title = tk.Label(text="Edit Establishment")

    establishment_name_label = tk.Label(text="Establishment Name")
    establishment_name_entry = tk.Entry()
    edit_establishment_button = tk.Button(text="Edit Establishment", command=lambda: edit_establishment())

    title.pack()
    back_button.pack()
    establishment_name_label.pack()
    establishment_name_entry.pack()
    edit_establishment_button.pack()