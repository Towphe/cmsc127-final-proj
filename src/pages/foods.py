import tkinter as tk
import pandas as pd
from tkinter import ttk
from util.repository import Repository

def render_foods(username:str, foods: pd.DataFrame, home, window:tk.Tk, repository:Repository, clear_page, add_food, redirect_to_edit_food_item, redirect_to_food_items_view, redirect_to_review_food, search_key=""):
    def search_food_item():
        name = search_bar.get()
        clear_page()
        render_foods(username, foods, home, window, repository, clear_page, add_food,  redirect_to_edit_food_item, redirect_to_food_items_view, redirect_to_review_food, name )

    def delete_food(food_id:int):
        repository.Food.remove_food(food_id)
        clear_page()
        redirect_to_food_items_view()

    filter_div = tk.LabelFrame()
    welcome_message = tk.Label(text="Food View")
    welcome_message.config(font=("Helvetica", 12, "bold"))

    back_button = tk.Button(filter_div, text="Back", command=lambda: home())
    back_button.grid(row=0, column=0, sticky="ew")

    search_label = tk.Label(filter_div, text="Name:")
    search_label.grid(row=0, column=1, sticky="ew")

    search_bar = tk.Entry(filter_div)
    search_bar.grid(row=0, column=2, sticky="ew")
    
    search_button = tk.Button(filter_div, text="Search", command=lambda: search_food_item())
    search_button.grid(row=0, column=3, sticky="ew")

    add_button = tk.Button(text="Add New Food Item", command=lambda: add_food())


    foods = repository.Food.find_food_with_key(search_key)
    # render table
    table = tk.LabelFrame()

    row = 1
    for i in range(foods.shape[0]):
        food = foods.iloc[i]
        
        id_label = tk.Label(table, text=str(food['food_id']), anchor="w")
        establishment_id_label = tk.Label(table, text=str(food['establishment_id']), anchor="w")
        establishment_name_label = tk.Label(table, text=str(food['establishment_name']), anchor="w")
        name_label = tk.Label(table, text=food['food_name'], anchor="w")
        category_label = tk.Label(table, text=food['category'], anchor="w")
        price_label = tk.Label(table, text=food['price'], anchor="w")
        average_rating_label = tk.Label(table, text=food['average_rating'], anchor="w")
        edit_button = tk.Button(table, text="Edit", anchor="w", command=lambda fid=food["food_id"]: redirect_to_edit_food_item(fid))
        delete_button = tk.Button(table, text="Delete", anchor="w", command=lambda fid=food["food_id"]: delete_food(fid))
        review_button = tk.Button(table, text="Review", anchor="w", command=lambda fid=food["food_id"], eid=food["establishment_id"]: redirect_to_review_food(fid,eid))

        if food["added_by"] != username:
            # disable edit/delete when username != current login
            edit_button.config(state=tk.DISABLED, bg='grey')
            delete_button.config(state=tk.DISABLED, bg='grey')
        else:
            review_button.config(state=tk.DISABLED, bg='grey')

        # render rows
        id_label.grid(row=row, column=0, sticky="ew")
        establishment_id_label.grid(row=row, column=1, sticky="ew")
        establishment_name_label.grid(row=row, column=2, sticky="ew")
        name_label.grid(row=row, column=3, sticky="ew")
        category_label.grid(row=row, column=4, sticky="ew")
        price_label.grid(row=row, column=5, sticky="ew")
        average_rating_label.grid(row=row, column=6, sticky="ew")
        edit_button.grid(row=row, column=7, sticky="ew")
        delete_button.grid(row=row, column=8, sticky="ew")
        review_button.grid(row=row, column=9, sticky="ew")

        row += 1

    tk.Label(table, text="Id", anchor="w").grid(row=0, column=0, sticky="ew")
    tk.Label(table, text="Establishment Id", anchor="w").grid(row=0, column=1, sticky="ew")
    tk.Label(table, text="Establishment Name", anchor="w").grid(row=0, column=2, sticky="ew")
    tk.Label(table, text="Name", anchor="w").grid(row=0, column=3, sticky="ew")
    tk.Label(table, text="Category", anchor="w").grid(row=0, column=4, sticky="ew")
    tk.Label(table, text="Price", anchor="w").grid(row=0, column=5, sticky="ew")
    tk.Label(table, text="Average Rating", anchor="w").grid(row=0, column=6, sticky="ew")
    tk.Label(table, text="Edit", anchor="w").grid(row=0, column=7, sticky="ew")
    tk.Label(table, text="Delete", anchor="w").grid(row=0, column=8, sticky="ew")
    tk.Label(table, text="Review", anchor="w").grid(row=0, column=9, sticky="ew")


    welcome_message.pack(pady=20)
    filter_div.pack()
    table.pack()
    add_button.pack(pady=20)

def render_add_food_item(username:str, foods, repository:Repository, window:tk.Tk, render_foods):
    def create_food():
        name = search_bar.get()
        # FK CONTRAINT CHECKER -- Only create food item if establishment exists in database
        if name in establishments['establishment_name'].values:
            # Get establishment id
            eid = establishments.loc[establishments['establishment_name'] == name, 'establishment_id'].iloc[0]
            food_name = food_name_entry.get()
            price = price_entry.get()
            category = choice.get()
            repository.Food.add_food(int(eid), food_name, float(price), category)
            render_foods()
    
    
    def search(e):
        name = search_bar.get()
        if name == '':
            # If the input is empty, show the full list
            search_bar['values'] = establishment_options

        else:
            data = []
            for item in establishment_options:
                if name.lower() in item.lower():
                    data.append(item)
            search_bar['values'] = data
    
    establishments = repository.Establishment.get_establishments()
    establishment_options = establishments['establishment_name'].tolist()

    search_bar = ttk.Combobox(value=establishment_options)
    search_bar.set("")
    search_bar.bind("<KeyRelease>", search)

    back_button = tk.Button(text="Back", command=lambda: foods())
    title = tk.Label(text="Add New Food Item")
    title.config(font=("Helvetica", 12, "bold"))

    establishment_id_label = tk.Label(text="Establishment")
    food_name_label = tk.Label(text="Food Name")
    food_name_entry = tk.Entry()

    choice = tk.StringVar()
    choice.set("meal")
    options = ["meal","appetizer","dessert"]

    category_label = tk.Label(text="Category")
    category_drop = tk.OptionMenu (None, choice,*options)

    # category_entry = tk.Entry()
    price_label = tk.Label(text="Price")
    price_entry = tk.Entry()
   
    price_label = tk.Label(text="Price")
    price_entry = tk.Entry()
    create_food_button = tk.Button(text="Create Food", command=lambda: create_food())

    title.pack(pady=20)
    back_button.pack()
    establishment_id_label.pack()
    search_bar.pack()
    food_name_label.pack()
    food_name_entry.pack()
    category_label.pack()
    category_drop.pack()
    price_label.pack()
    price_entry.pack()
    create_food_button.pack()

    return

def render_review_food (food_id:int, establishment_id:int, username:str, foods:pd.DataFrame, repository:Repository, window:tk.Tk, render_foods):
    def create_food_review():
        content =  food_review_content_entry.get()
        rating =  food_review_rating_entry.get()

        repository.Food.create_food_review(food_id, username, content, rating)
        render_foods()

    title = tk.Label(text="Review Food Item")
    title.config(font=("Helvetica", 12, "bold"))

    food_review_content_label = tk.Label(text="Review")
    food_review_content_entry = tk.Entry()
    food_review_rating_label = tk.Label(text="Rating")
    food_review_rating_entry = tk.Entry()

    back_button = tk.Button(text="Back", command=lambda: foods())
    create_review_button = tk.Button(text="Confirm", command=lambda: create_food_review())

    title.pack(pady=20)
    back_button.pack()

    food_review_content_label.pack()
    food_review_content_entry.pack()
    food_review_rating_label.pack()
    food_review_rating_entry.pack()

    create_review_button.pack()

def render_edit_food_item(food_id:int, render_foods, repository:Repository, window:tk.Tk):
    def edit_food():
        food_name = food_name_entry.get()
        price = price_entry.get()
        category = choice.get()
        repository.Food.update_food(food_id, food_name, category, float(price))
        render_foods()
    
    food_details = repository.Food.find_food_with_id(food_id)
    back_button = tk.Button(text="Back", command=lambda: render_foods())
    title = tk.Label(text="Edit Food Item")
    title.config(font=("Helvetica", 12, "bold"))

    food_name_label = tk.Label(text="Food Name")
    food_name_entry = tk.Entry()
    food_name_entry.insert(0, food_details['food_name'])
    food_name_entry.config(width=15)

    choice = tk.StringVar()
    choice.set(food_details['category'])
    options = ["meal","appetizer","dessert"]
    
    category_label = tk.Label(text="Category")
    category_drop = tk.OptionMenu (None, choice,*options)
    category_drop.config(width=15)
    # category_entry = tk.Entry()
    price_label = tk.Label(text="Price")
    price_entry = tk.Entry()
    price_entry.insert(0, food_details["price"])
    price_entry.config(width=15)

    edit_food_button = tk.Button(text="Confirm", command=lambda: edit_food())

    title.pack(pady=20)
    back_button.pack()
    food_name_label.pack()
    food_name_entry.pack()
    category_label.pack()
    category_drop.pack()
    # category_entry.pack()
    price_label.pack()
    price_entry.pack()
    edit_food_button.pack()

    return