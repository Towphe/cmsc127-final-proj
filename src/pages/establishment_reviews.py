import tkinter as tk
import pandas as pd
from pandastable import Table, TableModel
from util.repository import Repository

def render_establishment_reviews(username:str, user_type:str, establishment_reviews: pd.DataFrame, home, window:tk.Tk, redirect_to_edit_establishment_review,repository:Repository, clear_page, redirect_to_establishment_reviews):
    def delete_review(review_id:int, establishment_id:int):
        repository.Establishment.delete_establishment_Review(review_id, establishment_id)
        clear_page()
        redirect_to_establishment_reviews()
        return

    welcome_message = tk.Label(text="Establishment Reviews")
    welcome_message.config(font=("Helvetica", 12, "bold"))
    back_button = tk.Button(text="Back", command=lambda: home())

    # render table
    table = tk.LabelFrame()

    tk.Label(table, text="Review Id", anchor="w").grid(row=0, column=0, sticky="ew")
    tk.Label(table, text="Establishment Id", anchor="w").grid(row=0, column=1, sticky="ew")
    tk.Label(table, text="Username", anchor="w").grid(row=0, column=2, sticky="ew")
    tk.Label(table, text="Rating", anchor="w").grid(row=0, column=3, sticky="ew")
    tk.Label(table, text="Content", anchor="w").grid(row=0, column=4, sticky="ew")
    tk.Label(table, text="Date", anchor="w").grid(row=0, column=5, sticky="ew")
    tk.Label(table, text="Edit", anchor="w").grid(row=0, column=6, sticky="ew")
    tk.Label(table, text="Delete", anchor="w").grid(row=0, column=7, sticky="ew")

    row = 1
    for i in range(establishment_reviews.shape[0]):
       # rendered as python dictionary
        review = establishment_reviews.iloc[i]
        id_label = tk.Label(table, text=str(review['review_id']), anchor="w")
        establishment_id_label = tk.Label(table, text=review['establishment_id'], anchor="w")
        username_label = tk.Label(table, text=review['reviewer_username'], anchor="w")
        rating_label = tk.Label(table, text=review['rating'], anchor="w")
        content_label = tk.Label(table, text=review['content'], anchor="w")
        date_label = tk.Label(table, text=review['date_created'], anchor="w")
        edit_button = tk.Button(table, text="Edit", anchor="w", command=lambda rid=review["review_id"], eid=review["establishment_id"] : redirect_to_edit_establishment_review(rid,eid))
        delete_button = tk.Button(table, text="Delete", anchor="w", command=lambda rid=review["review_id"], eid=review["establishment_id"]: delete_review(rid, eid))

        if user_type != 'admin':
            if review["reviewer_username"] != username:
                # disable edit/delete when username != current login
                edit_button.config(state=tk.DISABLED, bg='grey')
                delete_button.config(state=tk.DISABLED, bg='grey')

        # render rows
        id_label.grid(row=row, column=0, sticky="ew")
        establishment_id_label.grid(row=row, column=1, sticky="ew")
        username_label.grid(row=row, column=2, sticky="ew")
        rating_label.grid(row=row, column=3, sticky="ew")
        content_label.grid(row=row, column=4, sticky="ew")
        date_label.grid(row=row, column=5, sticky="ew")

        edit_button.grid(row=row, column=6, sticky="ew")
        delete_button.grid(row=row, column=7, sticky="ew")

        row += 1

    welcome_message.pack(pady=20)
    back_button.pack()
    table.pack()

def render_edit_establishment_review(review_id:int, establishment_id:int, establishments:pd.DataFrame, repository:Repository, window:tk.Tk, render_establishments):
    def edit_establishment_review():
        content = content_entry.get()
        rating = rating_entry.get()
        repository.Establishment.update_establishment_review(review_id, establishment_id, content, rating)
        render_establishments()

    review_details = repository.Establishment.get_establishment_review_by_id(review_id)

    back_button = tk.Button(text="Back", command=lambda: establishments())
    title = tk.Label(text="Edit Establishment Review")
    title.config(font=("Helvetica", 12, "bold"))

    content_label = tk.Label(text="Content")
    content_entry = tk.Entry()
    content_entry.insert(0, review_details['content'])
    rating_label = tk.Label(text="Rating")
    rating_entry = tk.Entry()
    rating_entry.insert(0, review_details['rating'])

    edit_establishment_button = tk.Button(text="Confirm Changes", command=lambda: edit_establishment_review())

    title.pack(pady=20)
    back_button.pack()
    content_label.pack()
    content_entry.pack()
    rating_label.pack()
    rating_entry.pack()
    edit_establishment_button.pack()