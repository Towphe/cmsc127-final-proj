import tkinter as tk
from tkinter import ttk
import pandas as pd
from util.repository import Repository
import datetime

repository = Repository()

def render_reports_root(home, view_all_food_establishments, view_establishments_with_high_rating, view_reviews_of_establishment, view_reviews_of_food, view_food_items_from_establishments, view_food_items_from_establishments_with_category, view_establishment_reviews_within_month, view_food_reviews_within_month, view_food_items_by_price, view_food_by_price_range_or_category):
    title = tk.Label(text="Reports")
    back_button = tk.Button(text="Back", command=lambda: home())
    view_all_establishments = tk.Button(text="View All Food Establishments", command=lambda: view_all_food_establishments())
    view_high_rated = tk.Button(text="View All Food Establishments with High Ratings", command=lambda: view_establishments_with_high_rating())
    view_establishments_review = tk.Button(text="Reviews of Establishment", command=lambda: view_reviews_of_establishment())
    view_foods_review = tk.Button(text="Reviews of Foods", command=lambda: view_reviews_of_food())
    view_food_from_establishment = tk.Button(text="Food Items from Establishment", command=lambda: view_food_items_from_establishments())
    view_food_from_establishments_with_category = tk.Button(text="Food Items from Establishment with Category", command=lambda: view_food_items_from_establishments_with_category())
    view_establishment_reviews = tk.Button(text="Establishments Reviews in Month", command=lambda: view_establishment_reviews_within_month())
    view_food_reviews = tk.Button(text="Food Reviews in Month", command=lambda: view_food_reviews_within_month())
    view_food_by_price = tk.Button(text="Food By Price", command=lambda: view_food_items_by_price())
    view_food_by_range_and_category = tk.Button(text="Food by Price Range and/or Category", command=lambda: view_food_by_price_range_or_category())

    title.pack()
    back_button.pack()
    view_all_establishments.pack()
    view_establishments_review.pack()
    view_foods_review.pack()
    view_food_from_establishment.pack()
    view_food_from_establishments_with_category.pack()
    view_high_rated.pack()
    view_establishment_reviews.pack()
    view_food_reviews.pack()
    view_food_by_price.pack()
    view_food_by_range_and_category.pack()

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

def render_view_all_establishments(reports, establishments):
    title = tk.Label(text="All Establishments")
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
    
def render_reviews_for_establishment(reports, clear_page, establishments,establishment_id = 0, search_key=''):
    all_establishments = establishments['establishment_name'].tolist()

    def search_establishment_reviews():
        name = search_bar.get()

        if name in establishments['establishment_name'].values:
            # Get establishment id
            eid = establishments.loc[establishments['establishment_name'] == name, 'establishment_id'].iloc[0]
        else:
            eid = 0

        clear_page()
        render_reviews_for_establishment(reports, clear_page, establishments, eid, name)

    def search(e):
        name = search_bar.get()
        if name == '':
            # If the input is empty, show the full list
            search_bar['values'] = all_establishments

        else:
            data = []
            for item in all_establishments:
                if name.lower() in item.lower():
                    data.append(item)
            search_bar['values'] = data

    reviews = repository.Reports.reviews_for_establishment(establishment_id)

    title = tk.Label(text="Establishments Reviews")
    back_button = tk.Button(text="Back", command=lambda: reports())
    establishment_name_label = tk.Label(text="Establishment Name")

    search_bar = ttk.Combobox(value=all_establishments)
    search_bar.set(search_key)
    search_bar.bind("<KeyRelease>", search)
    search_button = tk.Button(text="Search", command=lambda: search_establishment_reviews())

    table = tk.LabelFrame()

    tk.Label(table, text="Id", anchor="w").grid(row=0, column=0, sticky="ew")
    tk.Label(table, text="Reviewer Username", anchor="w").grid(row=0, column=1, sticky="ew")
    tk.Label(table, text="Content", anchor="w").grid(row=0, column=2, sticky="ew")
    tk.Label(table, text="Rating", anchor="w").grid(row=0, column=3, sticky="ew")
    tk.Label(table, text="Date Created", anchor="w").grid(row=0, column=4, sticky="ew")

    row = 1
    for i in range(reviews.shape[0]):
        # print(establishments.iloc[i]['establishment_id']) # rendered as python dictionary
        review = reviews.iloc[i]
        id_label = tk.Label(table, text=str(review['review_id']), anchor="w")
        username_label = tk.Label(table, text=review['reviewer_username'], anchor="w")
        content_label = tk.Label(table, text=review['content'], anchor="w")
        rating_label = tk.Label(table, text=review['rating'], anchor="w")
        date_created_label = tk.Label(table, text=review['date_created'], anchor="w")

        # render rows
        id_label.grid(row=row, column=0, sticky="ew")
        username_label.grid(row=row, column=1, sticky="ew")
        content_label.grid(row=row, column=2, sticky="ew")
        rating_label.grid(row=row, column=3, sticky="ew")
        date_created_label.grid(row=row, column=4, sticky="ew")
        row += 1


    title.pack()
    back_button.pack()
    establishment_name_label.pack()
    search_bar.pack()
    search_button.pack()
    table.pack()

def render_reviews_for_food_item(reports, clear_page, foods, food_id = 0, search_key=''):
    all_foods = foods['food_name'].tolist()

    def search_food_review():        
        food_name = search_bar.get()

        if food_name in foods['food_name'].values:
            # Get food id
            fid = foods.loc[foods['food_name'] == food_name, 'food_id'].iloc[0]
        else:
            fid = 0
        
        clear_page()
        render_reviews_for_food_item(reports, clear_page,foods, int(fid), food_name)
    
    def search(e):
        name = search_bar.get()
        if name == '':
            # If the input is empty, show the full list
            search_bar['values'] = all_foods

        else:
            data = []
            for item in all_foods:
                if name.lower() in item.lower():
                    data.append(item)
            search_bar['values'] = data


    reviews = repository.Reports.reviews_for_food_item(food_id)

    title = tk.Label(text="Food Reviews")
    back_button = tk.Button(text="Back", command=lambda: reports())
    food_name_label = tk.Label(text="Food Name")

    search_bar = ttk.Combobox(value=all_foods)
    search_bar.set(search_key)
    search_bar.bind("<KeyRelease>", search)
    search_button = tk.Button(text="Search", command=lambda: search_food_review())

    table = tk.LabelFrame()

    tk.Label(table, text="Id", anchor="w").grid(row=0, column=0, sticky="ew")
    tk.Label(table, text="Reviewer Username", anchor="w").grid(row=0, column=1, sticky="ew")
    tk.Label(table, text="Content", anchor="w").grid(row=0, column=2, sticky="ew")
    tk.Label(table, text="Rating", anchor="w").grid(row=0, column=3, sticky="ew")
    tk.Label(table, text="Date Created", anchor="w").grid(row=0, column=4, sticky="ew")

    row = 1
    for i in range(reviews.shape[0]):
        review = reviews.iloc[i]
        id_label = tk.Label(table, text=str(review['review_id']), anchor="w")
        username_label = tk.Label(table, text=review['reviewer_username'], anchor="w")
        content_label = tk.Label(table, text=review['content'], anchor="w")
        rating_label = tk.Label(table, text=review['rating'], anchor="w")
        date_created_label = tk.Label(table, text=review['date_created'], anchor="w")

        # render rows
        id_label.grid(row=row, column=0, sticky="ew")
        username_label.grid(row=row, column=1, sticky="ew")
        content_label.grid(row=row, column=2, sticky="ew")
        rating_label.grid(row=row, column=3, sticky="ew")
        date_created_label.grid(row=row, column=4, sticky="ew")

        row += 1


    title.pack()
    back_button.pack()
    food_name_label.pack()
    search_bar.pack()
    search_button.pack()
    table.pack()

def render_food_items_from_establishment(reports, clear_page, establishments, establishment_id = 0, search_key=''):
    all_establishments = establishments['establishment_name'].tolist()

    def search_food():
        name = search_bar.get()

        if name in establishments['establishment_name'].values:
            # Get establishment id
            eid = establishments.loc[establishments['establishment_name'] == name, 'establishment_id'].iloc[0]
        else:
            eid = 0

        clear_page()
        render_food_items_from_establishment(reports, clear_page, establishments, int(eid), name)
    
    def search(e):
        name = search_bar.get()
        if name == '':
            # If the input is empty, show the full list
            search_bar['values'] = all_establishments

        else:
            data = []
            for item in all_establishments:
                if name.lower() in item.lower():
                    data.append(item)
            search_bar['values'] = data

    foods = repository.Reports.food_items_from_establishment(establishment_id)
    title = tk.Label(text="Foods from Establishment")
    back_button = tk.Button(text="Back", command=lambda: reports())

    establishment_label = tk.Label(text="Establishment Name")
    search_bar = ttk.Combobox(value=all_establishments)
    search_bar.set(search_key)
    search_bar.bind("<KeyRelease>", search)
    search_button = tk.Button(text="Search", command=lambda: search_food())

    table = tk.LabelFrame()

    tk.Label(table, text="Id", anchor="w").grid(row=0, column=0, sticky="ew")
    tk.Label(table, text="Establishment Id", anchor="w").grid(row=0, column=1, sticky="ew")
    tk.Label(table, text="Name", anchor="w").grid(row=0, column=2, sticky="ew")
    tk.Label(table, text="Category", anchor="w").grid(row=0, column=3, sticky="ew")
    tk.Label(table, text="Price", anchor="w").grid(row=0, column=4, sticky="ew")
    tk.Label(table, text="Average Rating", anchor="w").grid(row=0, column=5, sticky="ew")

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

    title.pack()
    back_button.pack()
    establishment_label.pack()
    search_bar.pack()
    search_button.pack()
    table.pack()

def render_food_items_from_establishment_with_category(reports, clear_page, establishment_id = 0, category = ""):
    def search_food():
        eid = chosen_establishment.get()
        eid = int(eid.split(" - ")[0])
        c = choice.get()
        clear_page()
        render_food_items_from_establishment_with_category(reports, clear_page, int(eid), c)

    establishments = repository.Establishment.get_establishments()
    foods = repository.Reports.food_item_from_establishment_from_category(establishment_id, category)
    
    title = tk.Label(text="Food from Establishment with Category")
    back_button = tk.Button(text="Back", command=lambda: reports())
    establishment_label = tk.Label(text="Establishment Id")
    establishment_options = []

    for establishment in establishments.to_numpy():
        establishment_options.append(f"{establishment[0]} - {establishment[1]}")
    # establishment_id_entry = tk.Entry()
    
    chosen_establishment = tk.StringVar()
    chosen_establishment.set("Select establishment")
    establishment_id_entry = tk.OptionMenu(None, chosen_establishment, *establishment_options)

    choice = tk.StringVar()
    choice.set("meal")
    options = ["meal","appetizer","dessert"]

    category_entry_label = tk.Label(text="Category")
    category_drop = tk.OptionMenu (None, choice,*options)

    search_button = tk.Button(text="Search", command=lambda: search_food())
    table = tk.LabelFrame()

    tk.Label(table, text="Id", anchor="w").grid(row=0, column=0, sticky="ew")
    tk.Label(table, text="Establishment Id", anchor="w").grid(row=0, column=1, sticky="ew")
    tk.Label(table, text="Name", anchor="w").grid(row=0, column=2, sticky="ew")
    tk.Label(table, text="Category", anchor="w").grid(row=0, column=3, sticky="ew")
    tk.Label(table, text="Price", anchor="w").grid(row=0, column=4, sticky="ew")
    tk.Label(table, text="Average Rating", anchor="w").grid(row=0, column=5, sticky="ew")

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

    title.pack()
    back_button.pack()
    establishment_label.pack()
    establishment_id_entry.pack()
    category_entry_label.pack()
    category_drop.pack()
    search_button.pack()
    table.pack()

def render_establishment_reviews_within_month(reports, clear_page, month:int, year:int, establishment_id:int=0):
    def search_establishment():
        eid = chosen_establishment.get()
        eid = int(eid.split(" - ")[0])
        d = datetime.datetime.now()

        m = month_entry.get()
        if m == "": m = d.month
        else: m = int(m)

        y = year_entry.get()
        if y == "": y = d.year
        else: y = int(y)
        
        clear_page()
        render_establishment_reviews_within_month(reports, clear_page, m, y, int(eid))
    
    dt = datetime.datetime.now()
    chosen_establishment = tk.StringVar()
    chosen_establishment.set("n/a")

    establishments = repository.Establishment.get_establishments()

    reviews = repository.Reports.establishment_reviews_within_month(establishment_id, month, year)
    
    title = tk.Label(text="Establishment Reviews within Month")
    back_button = tk.Button(text="Back", command=lambda: reports())
    establishment_id_label = tk.Label(text="Establishment")
    establishment_options = []
    for establishment in establishments.to_numpy():
        establishment_options.append(f"{establishment[0]} - {establishment[1]}")

    # establishment_id_entry = tk.Entry()
    establishment_id_entry = tk.OptionMenu(None, chosen_establishment, *establishment_options)
    month_label = tk.Label(text="Month")
    month_entry = tk.Entry()
    month_entry.insert(0, dt.month)

    year_label = tk.Label(text="Year")
    year_entry = tk.Entry()
    year_entry.insert(0, dt.year)

    search_button = tk.Button(text="Search", command=lambda: search_establishment())
    table = tk.LabelFrame()

    tk.Label(table, text="Id", anchor="w").grid(row=0, column=0, sticky="ew")
    tk.Label(table, text="Reviewer Username", anchor="w").grid(row=0, column=1, sticky="ew")
    tk.Label(table, text="Content", anchor="w").grid(row=0, column=2, sticky="ew")
    tk.Label(table, text="Rating", anchor="w").grid(row=0, column=3, sticky="ew")
    tk.Label(table, text="Date Created", anchor="w").grid(row=0, column=4, sticky="ew")

    row = 1
    for i in range(reviews.shape[0]):
        review = reviews.iloc[i]
        id_label = tk.Label(table, text=str(review['review_id']), anchor="w")
        username_label = tk.Label(table, text=review['reviewer_username'], anchor="w")
        content_label = tk.Label(table, text=review['content'], anchor="w")
        rating_label = tk.Label(table, text=review['rating'], anchor="w")
        date_created_label = tk.Label(table, text=review['date_created'], anchor="w")

        # render rows
        id_label.grid(row=row, column=0, sticky="ew")
        username_label.grid(row=row, column=1, sticky="ew")
        content_label.grid(row=row, column=2, sticky="ew")
        rating_label.grid(row=row, column=3, sticky="ew")
        date_created_label.grid(row=row, column=4, sticky="ew")

        row += 1


    title.pack()
    back_button.pack()
    establishment_id_label.pack()
    establishment_id_entry.pack()
    month_label.pack()
    month_entry.pack()
    year_label.pack()
    year_entry.pack()
    search_button.pack()
    table.pack()

def render_food_reviews_within_month(reports, clear_page, month:int, year:int, establishment_id:int=0):
    def search_food_reviews():
        fid = chosen_food.get()
        fid = int(fid.split(" - ")[0])

        d = datetime.datetime.now()

        m = month_entry.get()
        if m == "": m = d.month
        else: m = int(m)

        y = year_entry.get()
        if y == "": y = d.year
        else: y = int(y)
        
        clear_page()
        render_food_reviews_within_month(reports, clear_page, m, y, int(fid))
    
    chosen_food = tk.StringVar()
    chosen_food.set("n/a")

    foods = repository.Food.get_food()
    
    reviews = repository.Reports.food_reviews_within_month(establishment_id, month, year)
    
    title = tk.Label(text="Food Reviews within Month")
    back_button = tk.Button(text="Back", command=lambda: reports())

    food_options = []
    for food in foods.to_numpy():
        food_options.append(f"{food[0]} - {food[4]}")

    food_id_label = tk.Label(text="Entry Id")
    # food_id_entry = tk.Entry()
    food_id_entry = tk.OptionMenu(None, chosen_food, *food_options)
    month_label = tk.Label(text="Month")
    month_entry = tk.Entry()
    year_label = tk.Label(text="Year")
    year_entry = tk.Entry()
    search_button = tk.Button(text="Search", command=lambda: search_food_reviews())
    table = tk.LabelFrame()

    tk.Label(table, text="Id", anchor="w").grid(row=0, column=0, sticky="ew")
    tk.Label(table, text="Reviewer Username", anchor="w").grid(row=0, column=1, sticky="ew")
    tk.Label(table, text="Content", anchor="w").grid(row=0, column=2, sticky="ew")
    tk.Label(table, text="Rating", anchor="w").grid(row=0, column=3, sticky="ew")
    tk.Label(table, text="Date Created", anchor="w").grid(row=0, column=4, sticky="ew")

    row = 1
    for i in range(reviews.shape[0]):
        review = reviews.iloc[i]
        id_label = tk.Label(table, text=str(review['review_id']), anchor="w")
        username_label = tk.Label(table, text=review['reviewer_username'], anchor="w")
        content_label = tk.Label(table, text=review['content'], anchor="w")
        rating_label = tk.Label(table, text=review['rating'], anchor="w")
        date_created_label = tk.Label(table, text=review['date_created'], anchor="w")

        # render rows
        id_label.grid(row=row, column=0, sticky="ew")
        username_label.grid(row=row, column=1, sticky="ew")
        content_label.grid(row=row, column=2, sticky="ew")
        rating_label.grid(row=row, column=3, sticky="ew")
        date_created_label.grid(row=row, column=4, sticky="ew")

        row += 1


    title.pack()
    back_button.pack()
    food_id_label.pack()
    food_id_entry.pack()
    month_label.pack()
    month_entry.pack()
    year_label.pack()
    year_entry.pack()
    search_button.pack()
    table.pack()

def render_food_from_establishment_by_price(reports, clear_page, by:str = 'ASC', establishment_id:int = 0):
    def search_food():
        eid = chosen_establishment.get()
        eid = int(eid.split(" - ")[0])
        
        clear_page()
        render_food_from_establishment_by_price(reports, clear_page, by_str.get(), int(eid))

    chosen_establishment = tk.StringVar()
    chosen_establishment.set("n/a")

    establishments = repository.Establishment.get_establishments()
    foods = repository.Reports.food_items_from_establishment_by_price(establishment_id, by)
    by_str = tk.StringVar()
    by_str.set(by)
    title = tk.Label(text="Foods by Price")
    back_button = tk.Button(text="Back", command=lambda: reports())
    establishment_label = tk.Label(text="Establishment")
    establishment_options = []

    for establishment in establishments.to_numpy():
        establishment_options.append(f"{establishment[0]} - {establishment[1]}")
    establishment_id_entry = tk.OptionMenu(None, chosen_establishment, *establishment_options)

    sort_label = tk.Label(text="By")
    options = ['ASC', 'DESC']
    sort_entry = tk.OptionMenu(None, by_str, *options)
    search_button = tk.Button(text="Search", command=lambda: search_food())
    table = tk.LabelFrame()

    tk.Label(table, text="Id", anchor="w").grid(row=0, column=0, sticky="ew")
    tk.Label(table, text="Establishment Id", anchor="w").grid(row=0, column=1, sticky="ew")
    tk.Label(table, text="Name", anchor="w").grid(row=0, column=2, sticky="ew")
    tk.Label(table, text="Category", anchor="w").grid(row=0, column=3, sticky="ew")
    tk.Label(table, text="Price", anchor="w").grid(row=0, column=4, sticky="ew")
    tk.Label(table, text="Average Rating", anchor="w").grid(row=0, column=5, sticky="ew")

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

    title.pack()
    back_button.pack()
    establishment_label.pack()
    establishment_id_entry.pack()
    sort_label.pack()
    sort_entry.pack()
    search_button.pack()
    table.pack()

def render_food_by_range_and_category(reports, clear_page, min_price:float = None, max_price:float = None, category:str = None):
    def search_food():
        c = choice.get()
        if c == "": c = None
        min_p = min_price_entry.get()
        if min_p == "": min_p = None
        else: min_p = float(min_p)
        max_p = max_price_entry.get()
        if max_p == "": max_p = None
        else: max_p = float(max_p)
        clear_page()
        render_food_by_range_and_category(reports, clear_page, min_p, max_p, c)

    foods = repository.Reports.food_by_price_range_and_or_category(category, min_price, max_price)
    
    title = tk.Label(text="View Foods by Price Range and/or Category")
    back_button = tk.Button(text="Back", command=lambda: reports())

    choice = tk.StringVar()
    choice.set("meal")
    options = ["meal","appetizer","dessert"]

    category_entry_label = tk.Label(text="Category")
    category_drop = tk.OptionMenu (None, choice,*options)

    min_price_label = tk.Label(text="Minimum Price")
    min_price_entry = tk.Entry()
    max_price_label = tk.Label(text="Maximum Price")
    max_price_entry = tk.Entry()
    search_button = tk.Button(text="Search", command=lambda: search_food())
    table = tk.LabelFrame()

    tk.Label(table, text="Id", anchor="w").grid(row=0, column=0, sticky="ew")
    tk.Label(table, text="Establishment Id", anchor="w").grid(row=0, column=1, sticky="ew")
    tk.Label(table, text="Name", anchor="w").grid(row=0, column=2, sticky="ew")
    tk.Label(table, text="Category", anchor="w").grid(row=0, column=3, sticky="ew")
    tk.Label(table, text="Price", anchor="w").grid(row=0, column=4, sticky="ew")
    tk.Label(table, text="Average Rating", anchor="w").grid(row=0, column=5, sticky="ew")

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

    title.pack()
    back_button.pack()
    category_entry_label.pack()
    category_drop.pack()
    min_price_label.pack()
    min_price_entry.pack()
    max_price_label.pack()
    max_price_entry.pack()
    
    search_button.pack()
    table.pack()