import tkinter as tk

def render_home(username, render_establishments, render_foods, render_signin, render_signup, signout, render_reports, render_establishment_reviews, render_food_reviews):
    # define elements

    welcome_message = tk.Label(text="Welcome!")

    establishments_button = tk.Button(text="Establishments", command=lambda: render_establishments())
    foods_button = tk.Button(text="Foods", command=lambda: render_foods())
    reports = tk.Button(text="Reports", command=lambda: render_reports())
    establishment_reviews_button = tk.Button(text="Establishment Reviews", command=lambda: render_establishment_reviews())
    food_reviews_button = tk.Button(text="Food Reviews", command=lambda: render_food_reviews())


    signin_button = tk.Button(text="Sign In", command=lambda: render_signin())
    signup_button = tk.Button(text="Sign Up", command=lambda: render_signup())
    signout_button = tk.Button(text="Sign Out", command=lambda: signout())

    # display elements
    welcome_message.pack()
    establishments_button.pack()
    foods_button.pack()
    food_reviews_button.pack()
    establishment_reviews_button.pack()
    
    reports.pack()

    if username == None:
        signin_button.pack()
        signup_button.pack()
    else:
        signin_button.pack()
