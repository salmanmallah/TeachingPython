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
ttk.Label(win, text='Enter your name : ')

win.mainloop()
