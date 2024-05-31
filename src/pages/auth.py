import tkinter as tk
from util.repository import Repository

def render_signin(home, repository:Repository, set_user, clear_page):
    def signin():
        # repository.Users
        username = username_entry.get()
        password = password_entry.get()
        signin_result = repository.Users.sign_in(username, password)
        
        if signin_result[0] == True:
            # set username and password
            set_user(username, password)
        else:
            is_wrong_password = True
            clear_page()
            render_signin(home, repository, set_user, clear_page)
    
    # define elements
    title = tk.Label(text="Sign In")
    back_button = tk.Button(text="Back", command=lambda: home())
    username_label = tk.Label(text="Username")
    username_entry = tk.Entry()
    password_label = tk.Label(text="Password")
    password_entry = tk.Entry()
    sign_in_button = tk.Button(text="Sign In", command=lambda: signin())

    # render
    title.pack()
    back_button.pack()
    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()
    sign_in_button.pack()

def render_signup(home, repository:Repository, set_user, clear_page):
    def signup():
        # repository.Users
        username = username_entry.get()
        password = password_entry.get()
        signup_result = repository.Users.sign_up(username, password)

        if signup_result[0] == True:
            # successful signup, redirect to home
            set_user(username, password)
        else:
            # unsuccessful signup, retain page
            clear_page()
            render_signup(home, repository, set_user, clear_page)

    # define elements
    title = tk.Label(text="Sign Up")
    back_button = tk.Button(text="Back", command=lambda: home())
    username_label = tk.Label(text="Username")
    username_entry = tk.Entry()
    password_label = tk.Label(text="Password")
    password_entry = tk.Entry()
    sign_up_button = tk.Button(text="Sign Up", command=lambda: signup())

    # render
    title.pack()
    back_button.pack()
    username_label.pack()
    username_entry.pack()
    password_label.pack()
    password_entry.pack()
    sign_up_button.pack()