import tkinter as tk
from util.repository import Repository

def render_reports_root(home):
    title = tk.Label(text="Reports")
    back_button = tk.Button(text="Back", command=lambda: home())
    # create option of reports to view

    title.pack()
    back_button.pack()