import tkinter as tk
import pandas as pd
from util.repository import Repository

def render_foods(username:str, foods: pd.DataFrame, home, window:tk.Tk, repository:Repository, clear_page, add_food, redirect_to_edit_food_item, redirect_to_food_items_view, redirect_to_review_food):
    def delete_food(food_id:int):
        repository.Food.remove_food(food_id)
        clear_page()
        redirect_to_food_items_view()
        return
    
    def load_foods_on_table(foods):
        row = 1
        for i in range(foods.shape[0]):
            food = foods.iloc[i]
            
            id_label = tk.Label(table, text=str(food['food_id']), anchor="w")
            establishment_id_label = tk.Label(table, text=str(food['establishment_id']), anchor="w")
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
            name_label.grid(row=row, column=2, sticky="ew")
            category_label.grid(row=row, column=3, sticky="ew")
            price_label.grid(row=row, column=4, sticky="ew")
            average_rating_label.grid(row=row, column=5, sticky="ew")
            edit_button.grid(row=row, column=6, sticky="ew")
            delete_button.grid(row=row, column=7, sticky="ew")
            review_button.grid(row=row, column=8, sticky="ew")

            row += 1
    
    def empty_table():
        for row in table.winfo_children():
            count = 0
            table.winfo_children()[count].destroy()
            count = count + 1
        
    def searchFood(e):
        name = search_bar.get()
    
        if name == '':
            data = foods
        else:
            data = foods.query(f"food_name.str.contains('{name}', case=False)" )
            
        empty_table()
        load_foods_on_table(data)
        

    welcome_message = tk.Label(text="Food View")
    search_bar = tk.Entry()

    # Search data frame every key release
    search_bar.bind("<KeyRelease>", searchFood)

    back_button = tk.Button(text="Back", command=lambda: home())

    # render table
    table = tk.LabelFrame()

    tk.Label(table, text="Id", anchor="w").grid(row=0, column=0, sticky="ew")
    tk.Label(table, text="Establishment Id", anchor="w").grid(row=0, column=1, sticky="ew")
    tk.Label(table, text="Name", anchor="w").grid(row=0, column=2, sticky="ew")
    tk.Label(table, text="Category", anchor="w").grid(row=0, column=3, sticky="ew")
    tk.Label(table, text="Price", anchor="w").grid(row=0, column=4, sticky="ew")
    tk.Label(table, text="Average Rating", anchor="w").grid(row=0, column=5, sticky="ew")
    tk.Label(table, text="Edit", anchor="w").grid(row=0, column=6, sticky="ew")
    tk.Label(table, text="Delete", anchor="w").grid(row=0, column=7, sticky="ew")
    tk.Label(table, text="Review", anchor="w").grid(row=0, column=8, sticky="ew")

    # Pre-load all foods
    load_foods_on_table(foods)
    
    add_button = tk.Button(text="Add New Food Item", command=lambda: add_food())

    welcome_message.pack()
    back_button.pack()
    search_bar.pack()
    table.pack()
    add_button.pack()

def render_add_food_item(username:str, foods, repository:Repository, window:tk.Tk, render_foods):
    def create_food():
        establishment_id = establishment_id_entry.get()
        food_name = food_name_entry.get()
        price = price_entry.get()
        category = category_entry.get()
        repository.Food.add_food(int(establishment_id), food_name, float(price), category)
        render_foods()
    
    back_button = tk.Button(text="Back", command=lambda: foods())
    title = tk.Label(text="Add New Food Item")

    establishment_id_label = tk.Label(text="Establishment Id")
    establishment_id_entry = tk.Entry()
    food_name_label = tk.Label(text="Food Name")
    food_name_entry = tk.Entry()
    category_label = tk.Label(text="Category")
    category_entry = tk.Entry()
    price_label = tk.Label(text="Price")
    price_entry = tk.Entry()
    create_food_button = tk.Button(text="Create Food", command=lambda: create_food())

    title.pack()
    back_button.pack()
    establishment_id_label.pack()
    establishment_id_entry.pack()
    food_name_label.pack()
    food_name_entry.pack()
    category_label.pack()
    category_entry.pack()
    price_label.pack()
    price_entry.pack()
    create_food_button.pack()

    return

def render_review_food (food_id:int, establishment_id:int, username:str, foods:pd.DataFrame, repository:Repository, window:tk.Tk, render_foods):
    def create_food_review():
        content =  food_review_content_entry.get()
        rating =  food_review_rating_entry.get()

        repository.Food.create_food_review(food_id,establishment_id, username, content, rating)
        render_foods()


    title = tk.Label(text="Review Food Item")

    food_review_content_label = tk.Label(text="Review")
    food_review_content_entry = tk.Entry()
    food_review_rating_label = tk.Label(text="Rating")
    food_review_rating_entry = tk.Entry()

    back_button = tk.Button(text="Back", command=lambda: foods())
    create_review_button = tk.Button(text="Confirm", command=lambda: create_food_review())

    title.pack()
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
        category = category_entry.get()
        repository.Food.update_food(food_id, food_name, category, float(price))
        render_foods()
    
    back_button = tk.Button(text="Back", command=lambda: render_foods())
    title = tk.Label(text="Edit Food Item")

    food_name_label = tk.Label(text="Food Name")
    food_name_entry = tk.Entry()
    category_label = tk.Label(text="Category")
    category_entry = tk.Entry()
    price_label = tk.Label(text="Price")
    price_entry = tk.Entry()
    edit_food_button = tk.Button(text="Create Food", command=lambda: edit_food())

    title.pack()
    back_button.pack()
    food_name_label.pack()
    food_name_entry.pack()
    category_label.pack()
    category_entry.pack()
    price_label.pack()
    price_entry.pack()
    edit_food_button.pack()

    return