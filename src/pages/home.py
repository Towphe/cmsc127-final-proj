import tkinter as tk
from util.repository import Repository

def render_home(username, user_type, render_establishments, render_foods, render_signin, render_signup, signout, render_reports, render_my_establishment_reviews, render_my_food_reviews, render_create_admin_account, render_all_acounts):
    # define elements

    welcome_message = tk.Label(text="Welcome!")
    welcome_message.config(font=("Helvetica", 12, "bold"))

    establishments_button = tk.Button(text="Establishments", command=lambda: render_establishments())
    establishments_button.config(width=25)
    foods_button = tk.Button(text="Foods", command=lambda: render_foods())
    foods_button.config(width=25)
    reports = tk.Button(text="Reports", command=lambda: render_reports())
    reports.config(width=25)
    establishment_reviews_button = tk.Button(text="My Establishment Reviews", command=lambda: render_my_establishment_reviews())
    establishment_reviews_button.config(width=25)
    food_reviews_button = tk.Button(text="My Food Reviews", command=lambda: render_my_food_reviews())
    food_reviews_button.config(width=25)
    create_admin_button = tk.Button(text="Create admin account", command=lambda: render_create_admin_account())
    create_admin_button.config(width=25)
    view_all_accounts_button = tk.Button(text="View all accounts", command=lambda: render_all_acounts())
    view_all_accounts_button.config(width=25)

    signin_button = tk.Button(text="Sign In", command=lambda: render_signin())
    signin_button.config(width=25)
    signup_button = tk.Button(text="Sign Up", command=lambda: render_signup())
    signup_button.config(width=25)
    signout_button = tk.Button(text="Sign Out", command=lambda: signout())
    signout_button.config(width=25)

    # display elements
    welcome_message.pack(pady=20)
    establishments_button.pack()
    foods_button.pack()
    food_reviews_button.pack()
    establishment_reviews_button.pack()
    
    reports.pack()

    if user_type == "admin":
        create_admin_button.pack()
        view_all_accounts_button.pack()

    if username == None:
        signin_button.pack()
        signup_button.pack()
    else:
        signout_button.pack()

def render_create_admin_account(home, repository:Repository, clear_page):
    def signup_admin():
        # repository.Users
        username = username_entry.get()
        password = password_entry.get()
        type = 'admin'
        signup_result = repository.Users.sign_up(username, password, type)

        if signup_result[0] == True:
            # successful signup, redirect to home
            home()
        else:
            # unsuccessful signup, retain page
            clear_page()
            render_create_admin_account(home, repository, clear_page)

    # define elements
    title = tk.Label(text="Create admin account")
    title.config(font=("Helvetica", 12, "bold"))
    back_button = tk.Button(text="Back", command=lambda: home())
    username_label = tk.Label(text="Username")
    username_entry = tk.Entry()
    password_label = tk.Label(text="Password")
    password_entry = tk.Entry()
    sign_up_button = tk.Button(text="Create", command=lambda: signup_admin())

    # render
    title.pack(pady=20)
    back_button.pack()
    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()
    sign_up_button.pack()

def render_view_all_accounts(home, accounts, repository:Repository, clear_page):
    title = tk.Label(text="All accounts")
    title.config(font=("Helvetica", 12, "bold"))
    back_button = tk.Button(text="Back", command=lambda: home())
    table = tk.LabelFrame()

    tk.Label(table, text="Username", anchor="w").grid(row=0, column=0, sticky="ew")
    tk.Label(table, text="User type", anchor="w").grid(row=0, column=1, sticky="ew")

    row = 1
    for i in range(accounts.shape[0]):
        # print(establishments.iloc[i]['establishment_id']) # rendered as python dictionary
        account = accounts.iloc[i]
        username_label = tk.Label(table, text=account['username'], anchor="w")
        type_label = tk.Label(table, text=account['type'], anchor="w")
        # render rows
        username_label.grid(row=row, column=0, sticky="ew")
        type_label.grid(row=row, column=1, sticky="ew")

        row += 1

    title.pack(pady=20)
    back_button.pack()
    table.pack()