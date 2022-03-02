import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("widgets With For loops")
win.geometry('400x200')

labels = ['Enter your Name: ', 'Enter your Email: ', 'Enter your Age: ']

for label in range(len(labels)):
    ttk.Label(win, text=labels[label]).grid(row=label, column=0, sticky=tk.W)
    ttk.Entry(win).grid(row=label, column=1)

win.mainloop()