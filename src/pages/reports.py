import tkinter as tk
from util.repository import Repository

def render_reports_root(home, view_all_food_establishments, view_establishments_with_high_rating):
    title = tk.Label(text="Reports")
    back_button = tk.Button(text="Back", command=lambda: home())
    view_all_establishments = tk.Button(text="View All Food Establishments", command=lambda: view_all_food_establishments())
    view_high_rated = tk.Button(text="View All Food Establishments with High Ratings", command=lambda: view_establishments_with_high_rating())
    # create option of reports to view

    title.pack()
    back_button.pack()
    view_all_establishments.pack()
    view_high_rated.pack()

def render_view_all_establishments(reports, establishments):
    title = tk.Label(text="View All Establishments")
    back_button = tk.Button(text="Back", command=lambda: reports())
    table = tk.LabelFrame()

    tk.Label(table, text="Id", anchor="w").grid(row=0, column=0, sticky="ew")
    tk.Label(table, text="Name", anchor="w").grid(row=0, column=1, sticky="ew")
    tk.Label(table, text="Added by", anchor="w").grid(row=0, column=2, sticky="ew")
    tk.Label(table, text="Average", anchor="w").grid(row=0, column=3, sticky="ew")

    row = 1
    for i in range(establishments.shape[0]):
        # print(establishments.iloc[i]['establishment_id']) # rendered as python dictionary
        establishment = establishments.iloc[i]
        id_label = tk.Label(table, text=str(establishment['establishment_id']), anchor="w")
        name_label = tk.Label(table, text=establishment['establishment_name'], anchor="w")
        added_by_label = tk.Label(table, text=establishment['added_by'], anchor="w")
        average_rating_label = tk.Label(table, text=establishment['average_rating'], anchor="w")

        # render rows
        id_label.grid(row=row, column=0, sticky="ew")
        name_label.grid(row=row, column=1, sticky="ew")
        added_by_label.grid(row=row, column=2, sticky="ew")
        average_rating_label.grid(row=row, column=3, sticky="ew")

        row += 1

    title.pack()
    back_button.pack()
    table.pack()

def render_establishments_with_high_average_ratings(reports, establishments):
    title = tk.Label(text="Establishments with High Average Rating")
    back_button = tk.Button(text="Back", command=lambda: reports())
    table = tk.LabelFrame()

    tk.Label(table, text="Id", anchor="w").grid(row=0, column=0, sticky="ew")
    tk.Label(table, text="Name", anchor="w").grid(row=0, column=1, sticky="ew")
    tk.Label(table, text="Added by", anchor="w").grid(row=0, column=2, sticky="ew")
    tk.Label(table, text="Average", anchor="w").grid(row=0, column=3, sticky="ew")

    row = 1
    for i in range(establishments.shape[0]):
        # print(establishments.iloc[i]['establishment_id']) # rendered as python dictionary
        establishment = establishments.iloc[i]
        id_label = tk.Label(table, text=str(establishment['establishment_id']), anchor="w")
        name_label = tk.Label(table, text=establishment['establishment_name'], anchor="w")
        added_by_label = tk.Label(table, text=establishment['added_by'], anchor="w")
        average_rating_label = tk.Label(table, text=establishment['average_rating'], anchor="w")

        # render rows
        id_label.grid(row=row, column=0, sticky="ew")
        name_label.grid(row=row, column=1, sticky="ew")
        added_by_label.grid(row=row, column=2, sticky="ew")
        average_rating_label.grid(row=row, column=3, sticky="ew")

        row += 1

    title.pack()
    back_button.pack()
    table.pack()
# ----