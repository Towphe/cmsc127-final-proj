import tkinter as tk
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
    view_high_rated.pack()
    view_establishments_review.pack()
    view_foods_review.pack()
    view_food_from_establishment.pack()
    view_food_from_establishments_with_category.pack()
    view_establishment_reviews.pack()
    view_food_reviews.pack()
    view_food_by_price.pack()
    view_food_by_range_and_category.pack()

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

def render_reviews_for_establishment(reports, clear_page, establishment_id = 0):
    def search_establishment_reviews():
        eid = establishment_id_entry.get()
        clear_page()
        render_reviews_for_establishment(reports, clear_page, int(eid))

    reviews = repository.Reports.reviews_for_establishment(establishment_id)

    title = tk.Label(text="Establishments Reviews")
    back_button = tk.Button(text="Back", command=lambda: reports())
    establishment_id_label = tk.Label(text="Entry Id")
    establishment_id_entry = tk.Entry()
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
    establishment_id_label.pack()
    establishment_id_entry.pack()
    search_button.pack()
    table.pack()

def render_reviews_for_food_item(reports, clear_page, food_id = 0):
    def search_food_review():
        fid = food_id_entry.get()
        clear_page()
        render_reviews_for_establishment(reports, clear_page, int(fid))

    reviews = repository.Reports.reviews_for_food_item(food_id)

    title = tk.Label(text="Food Reviews")
    back_button = tk.Button(text="Back", command=lambda: reports())
    food_id_label = tk.Label(text="Entry Id")
    food_id_entry = tk.Entry()
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
    food_id_label.pack()
    food_id_entry.pack()
    search_button.pack()
    table.pack()

def render_food_items_from_establishment(reports, clear_page, establishment_id = 0):
    def search_food():
        eid = establishment_id_entry.get()
        clear_page()
        render_food_items_from_establishment(reports, clear_page, int(eid))
    
    foods = repository.Reports.food_items_from_establishment(establishment_id)
    
    title = tk.Label(text="Foods from Establishment")
    back_button = tk.Button(text="Back", command=lambda: reports())
    establishment_label = tk.Label(text="Entry Id")
    establishment_id_entry = tk.Entry()
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
    search_button.pack()
    table.pack()

def render_food_items_from_establishment_with_category(reports, clear_page, establishment_id = 0, category = ""):
    def search_food():
        eid = establishment_id_entry.get()
        c = category_entry.get()
        clear_page()
        render_food_items_from_establishment_with_category(reports, clear_page, int(eid), c)
    
    foods = repository.Reports.food_item_from_establishment_from_category(establishment_id, category)
    
    title = tk.Label(text="Food from Establishment with Category")
    back_button = tk.Button(text="Back", command=lambda: reports())
    establishment_label = tk.Label(text="Entry Id")
    establishment_id_entry = tk.Entry()
    category_entry_label = tk.Label(text="Category")
    category_entry = tk.Entry()
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
    category_entry.pack()
    search_button.pack()
    table.pack()

def render_establishment_reviews_within_month(reports, clear_page, month:int, year:int, establishment_id:int=0):
    def search_establishment():
        eid = establishment_id_entry.get()
        d = datetime.datetime.now()

        m = month_entry.get()
        if m == "": m = d.month
        else: m = int(m)

        y = year_entry.get()
        if y == "": y = d.year
        else: y = int(y)
        
        clear_page()
        render_establishment_reviews_within_month(reports, clear_page, m, y, int(eid))
    
    reviews = repository.Reports.establishment_reviews_within_month(establishment_id, month, year)
    
    title = tk.Label(text="Establishment Reviews within Month")
    back_button = tk.Button(text="Back", command=lambda: reports())
    establishment_id_label = tk.Label(text="Entry Id")
    establishment_id_entry = tk.Entry()
    month_label = tk.Label(text="Month")
    month_entry = tk.Entry()
    year_label = tk.Label(text="Year")
    year_entry = tk.Entry()
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
        fid = food_id_entry.get()
        d = datetime.datetime.now()

        m = month_entry.get()
        if m == "": m = d.month
        else: m = int(m)

        y = year_entry.get()
        if y == "": y = d.year
        else: y = int(y)
        
        clear_page()
        render_establishment_reviews_within_month(reports, clear_page, m, y, int(fid))
    
    reviews = repository.Reports.food_reviews_within_month(establishment_id, month, year)
    
    title = tk.Label(text="Food Reviews within Month")
    back_button = tk.Button(text="Back", command=lambda: reports())
    food_id_label = tk.Label(text="Entry Id")
    food_id_entry = tk.Entry()
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
        eid = establishment_id_entry.get()
        
        clear_page()
        render_food_from_establishment_by_price(reports, clear_page, by_str.get(), int(eid))
    
    foods = repository.Reports.food_items_from_establishment_by_price(establishment_id, by)
    by_str = tk.StringVar()
    by_str.set(by)
    
    title = tk.Label(text="Foods by Price")
    back_button = tk.Button(text="Back", command=lambda: reports())
    establishment_label = tk.Label(text="Entry Id")
    establishment_id_entry = tk.Entry()
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
        c = cat_entry.get()
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
    cat_label = tk.Label(text="Category")
    cat_entry = tk.Entry()
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
    cat_label.pack()
    cat_entry.pack()
    min_price_label.pack()
    min_price_entry.pack()
    max_price_label.pack()
    max_price_entry.pack()
    
    search_button.pack()
    table.pack()

    return