import tkinter as tk

def render_home(username, render_establishments, render_signin):
    # define elements

    welcome_message = tk.Label(text="Welcome!")

    establishments_button = tk.Button(text="Establishments", command=lambda: render_establishments())
    signin_button = tk.Button(text="Sign In", command=lambda: render_signin())
    signup_button = tk.Button(text="Sign Up")

    # display elements
    welcome_message.pack()
    establishments_button.pack()
    if username == None:
        signin_button.pack()
        signup_button.pack()
