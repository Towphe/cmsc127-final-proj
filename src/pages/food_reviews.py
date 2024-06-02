import tkinter as tk
import pandas as pd
from pandastable import Table, TableModel
from util.repository import Repository

def render_food_reviews(username:str, food_reviews: pd.DataFrame, home, window:tk.Tk, redirect_to_edit_food_review,repository:Repository, clear_page, redirect_to_food_reviews):
    def delete_review(review_id:int, food_id:int):
        repository.Food.delete_food_review(review_id, food_id)
        clear_page()
        redirect_to_food_reviews()
        return

    welcome_message = tk.Label(text="Food Reviews")
    back_button = tk.Button(text="Back", command=lambda: home())

    # render table
    table = tk.LabelFrame()

    tk.Label(table, text="Review Id", anchor="w").grid(row=0, column=0, sticky="ew")
    tk.Label(table, text="Food Id", anchor="w").grid(row=0, column=1, sticky="ew")
    tk.Label(table, text="Establishment Id", anchor="w").grid(row=0, column=2, sticky="ew")
    tk.Label(table, text="Username", anchor="w").grid(row=0, column=3, sticky="ew")
    tk.Label(table, text="Rating", anchor="w").grid(row=0, column=4, sticky="ew")
    tk.Label(table, text="Content", anchor="w").grid(row=0, column=5, sticky="ew")
    tk.Label(table, text="Date", anchor="w").grid(row=0, column=6, sticky="ew")
    tk.Label(table, text="Edit", anchor="w").grid(row=0, column=7, sticky="ew")
    tk.Label(table, text="Delete", anchor="w").grid(row=0, column=8, sticky="ew")

    row = 1
    for i in range(food_reviews.shape[0]):
       # rendered as python dictionary
        review = food_reviews.iloc[i]
        id_label = tk.Label(table, text=str(review['review_id']), anchor="w")
        food_id_label = tk.Label(table, text=review['food_id'], anchor="w")
        establishment_id_label = tk.Label(table, text=review['establishment_id'], anchor="w")
        username_label = tk.Label(table, text=review['reviewer_username'], anchor="w")
        rating_label = tk.Label(table, text=review['rating'], anchor="w")
        content_label = tk.Label(table, text=review['content'], anchor="w")
        date_label = tk.Label(table, text=review['date_created'], anchor="w")
        edit_button = tk.Button(table, text="Edit", anchor="w", command=lambda rid=review["review_id"], fid=review["food_id"]: redirect_to_edit_food_review(rid, fid))
        delete_button = tk.Button(table, text="Delete", anchor="w", command=lambda rid=review["review_id"], fid=review["food_id"]: delete_review(rid, fid))

        if review["reviewer_username"] != username:
            # disable edit/delete when username != current login
            edit_button.config(state=tk.DISABLED, bg='grey')
            delete_button.config(state=tk.DISABLED, bg='grey')

        # render rows
        id_label.grid(row=row, column=0, sticky="ew")
        food_id_label.grid(row=row, column=1, sticky="ew")
        establishment_id_label.grid(row=row, column=2, sticky="ew")
        username_label.grid(row=row, column=3, sticky="ew")
        rating_label.grid(row=row, column=4, sticky="ew")
        content_label.grid(row=row, column=5, sticky="ew")
        date_label.grid(row=row, column=6, sticky="ew")

        edit_button.grid(row=row, column=7, sticky="ew")
        delete_button.grid(row=row, column=8, sticky="ew")

        row += 1

    welcome_message.pack()
    back_button.pack()
    table.pack()

def render_edit_food_review(review_id:int, food_id:int, foods:pd.DataFrame, repository:Repository, window:tk.Tk, render_foods):
    def edit_food_review():
        content = content_entry.get()
        rating = rating_entry.get()
        # review_id:int, food_id:int, content:str, rating:float
        repository.Food.update_food_review(review_id, food_id, content, rating)
        render_foods()

    back_button = tk.Button(text="Back", command=lambda: foods())
    title = tk.Label(text="Edit food Review")

    content_label = tk.Label(text="Content")
    content_entry = tk.Entry()
    rating_label = tk.Label(text="Rating")
    rating_entry = tk.Entry()

    edit_food_button = tk.Button(text="Confirm Changes", command=lambda: edit_food_review())

    title.pack()
    back_button.pack()
    content_label.pack()
    content_entry.pack()
    rating_label.pack()
    rating_entry.pack()
    edit_food_button.pack()