"""
    Chapter 22
    –   Second Project (application)
        tkinter [1] Create GUI
    Pronunciation:
    ~tee-kinter
    ~kt-inter
    ~kinter
"""
# starter code
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("First Project")
win.geometry('1200x680')

# Create Labels
name_label = ttk.Label(win, text='Enter your name : ')
name_label.grid(row=0, column=0, sticky=tk.W)

age_label = ttk.Label(win, text='Enter your age : ')
age_label.grid(row=1, column=0, sticky=tk.W)

email_label = ttk.Label(win, text='Enter your email : ')
email_label.grid(row=2, column=0, sticky=tk.W)
win.mainloop()
