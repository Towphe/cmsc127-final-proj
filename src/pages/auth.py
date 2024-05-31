import tkinter as tk

def render_signin(home):
    title = tk.Label(text="Sign In")
    back_button = tk.Button(text="Back", command=lambda: home())
    title.pack()
    back_button.pack()