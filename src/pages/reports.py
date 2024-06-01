import tkinter as tk
from tkinter import ttk
import pandas as pd
from util.repository import Repository

def render_reports_root(home, view_all_food_establishments, view_establishments_with_high_rating, view_all_reviews, view_foods_from_establishment):
    title = tk.Label(text="Reports")
    back_button = tk.Button(text="Back", command=lambda: home())
    view_all_establishments = tk.Button(text="View All Food Establishments", command=lambda: view_all_food_establishments())
    view_high_rated = tk.Button(text="View All Food Establishments with High Ratings", command=lambda: view_establishments_with_high_rating())
    view_all_reviews_button = tk.Button(text="View All Reviews", command=lambda: view_all_reviews())
    foods_from_establishment_button = tk.Button(text="Food from establishment", command=lambda: view_foods_from_establishment())
    # create option of reports to view

    title.pack()
    back_button.pack()
    view_all_establishments.pack()
    view_high_rated.pack()
    view_all_reviews_button.pack()
    foods_from_establishment_button.pack()

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

def render_all_reviews(reports, reviews):
    def load_data_on_table (reviews):
        # Load all reviews
        row = 1
        for i in range(reviews.shape[0]):
            review = reviews.iloc[i]
            name_label = tk.Label(table, text= review['review_for'], anchor="w")
            username_label = tk.Label(table, text= review['reviewer_username'], anchor="w")
            rating_label = tk.Label(table, text= review['rating'], anchor="w")
            content_label = tk.Label(table, text= review['content'], anchor="w")
            date_label = tk.Label(table, text= review['date_created'], anchor="w")

            name_label.grid(row=row, column=0, sticky="ew")
            username_label.grid(row=row, column=1, sticky="ew")
            rating_label.grid(row=row, column=2, sticky="ew")
            content_label.grid(row=row, column=3, sticky="ew")
            date_label.grid(row=row, column=4, sticky="ew")

            row += 1

    def empty_table():
        # empty the table
        for row in table.winfo_children():
            count = 0
            table.winfo_children()[count].destroy()

        
    def search(e):
        name = search_bar.get() #get value
    
        if name == '':
            data = reviews
        else:                   #find review for the given string
            data = reviews.query(f"review_for.str.contains('{name}', case=False)" )
        
        empty_table()
        load_data_on_table(data)

    title = tk.Label(text="View all reviews")
    back_button = tk.Button(text="Back", command=lambda: reports())
    table = tk.LabelFrame()

    search_bar = tk.Entry()

    # Search data frame every key release
    search_bar.bind("<KeyRelease>", search)

    tk.Label(table, text="Review For", anchor="w").grid(row=0, column=0, sticky="ew")
    tk.Label(table, text="Reviewee", anchor="w").grid(row=0, column=1, sticky="ew")
    tk.Label(table, text="Rating", anchor="w").grid(row=0, column=2, sticky="ew")
    tk.Label(table, text="Content", anchor="w").grid(row=0, column=3, sticky="ew")
    tk.Label(table, text="Date", anchor="w").grid(row=0, column=4, sticky="ew")

    # Preload table
    load_data_on_table(reviews)
    
    title.pack()
    back_button.pack()
    search_bar.pack()
    table.pack()

def render_foods_from_establishment(reports, establishments, foods, repository):
    def load_foods_on_table(foods):
        # Render all food items
        row = 1
        for i in range(foods.shape[0]):
            food = foods.iloc[i]
            
            id_label = tk.Label(table, text=str(food['food_id']), anchor="w")
            establishment_id_label = tk.Label(table, text=str(food['establishment_id']), anchor="w")
            name_label = tk.Label(table, text=food['food_name'], anchor="w")
            category_label = tk.Label(table, text=food['category'], anchor="w")
            price_label = tk.Label(table, text=food['price'], anchor="w")
            average_rating_label = tk.Label(table, text=food['average_rating'], anchor="w")  
            # render rows
            id_label.grid(row=row, column=0, sticky="ew")
            establishment_id_label.grid(row=row, column=1, sticky="ew")
            name_label.grid(row=row, column=2, sticky="ew")
            category_label.grid(row=row, column=3, sticky="ew")
            price_label.grid(row=row, column=4, sticky="ew")
            average_rating_label.grid(row=row, column=5, sticky="ew")

            row += 1
    
    def empty_table():
        for row in table.winfo_children():
            count = 0
            table.winfo_children()[count].destroy()
            count = count + 1
        
    def searchFood(e):
        name = search_bar.get()
        empty_table()
        
        if name == '':
            # If the input is empty, show the full list
            data = foods
            load_foods_on_table(data)

        elif (name in establishments['establishment_name'].values):
            # Get id of selected item
            id = establishments.loc[establishments['establishment_name'] == name, 'establishment_id'].iloc[0]
            # Show food items from establishment id
            data:pd.DataFrame = repository.Reports.all_food_items_from_establishment(id)
            
            load_foods_on_table(data)

    welcome_message = tk.Label(text="Food View")
    search_bar = ttk.Combobox(value=establishments['establishment_name'].tolist())

    # Search data frame every key release and change in choices
    search_bar.bind("<KeyRelease>", searchFood)
    search_bar.bind("<<ComboboxSelected>>", searchFood)

    back_button = tk.Button(text="Back", command=lambda: reports())

    # render table
    table = tk.LabelFrame()

    tk.Label(table, text="Id", anchor="w").grid(row=0, column=0, sticky="ew")
    tk.Label(table, text="Establishment Id", anchor="w").grid(row=0, column=1, sticky="ew")
    tk.Label(table, text="Name", anchor="w").grid(row=0, column=2, sticky="ew")
    tk.Label(table, text="Category", anchor="w").grid(row=0, column=3, sticky="ew")
    tk.Label(table, text="Price", anchor="w").grid(row=0, column=4, sticky="ew")
    tk.Label(table, text="Average Rating", anchor="w").grid(row=0, column=5, sticky="ew")

    # Pre-load all foods
    load_foods_on_table(foods)

    welcome_message.pack()
    back_button.pack()
    search_bar.pack()
    table.pack()