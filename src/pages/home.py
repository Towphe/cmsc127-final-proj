import tkinter as tk

def render_home(username, render_establishments, render_foods, render_signin, render_signup, signout, render_reports, render_my_establishment_reviews, render_my_food_reviews):
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

    if username == None:
        signin_button.pack()
        signup_button.pack()
    else:
        signout_button.pack()
