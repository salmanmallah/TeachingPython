"""
    Chapter no. 22
    Tutorial no 234
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
win.title("Junaid Ahmed Mallah")
win.geometry('1200x680')

# Create Labels
name_label = ttk.Label(win, text='Enter your name : ')
name_label.grid(row=0, column=0, sticky=tk.W)

email_label = ttk.Label(win, text='Enter your email : ')
email_label.grid(row=1, column=0, sticky=tk.W)

age_label = ttk.Label(win, text='Enter your age : ')
age_label.grid(row=2, column=0, sticky=tk.W)

gender_label = ttk.Label(win, text='Enter your Gender : ')
gender_label.grid(row=3, column=0, sticky=tk.W)

# Create Entry Box
name_var = tk.StringVar()
name_entry = tk.Entry(win, width=20, bg='green', bd=4, textvariable=name_var)
name_entry.grid(row=0, column=1)

email_var = tk.StringVar()
email_entry = tk.Entry(win, width=20, bg='green', bd=4, textvariable=email_var)
email_entry.grid(row=1, column=1)

age_var = tk.StringVar()
age_entry = tk.Entry(win, width=20, bg='green', bd=4, textvariable=age_var)
age_entry.grid(row=2, column=1)

# Create combobox
gender_combobox = ttk.Combobox(win, width=16)
gender_combobox['values'] = ('Male', 'Female', 'Other')
gender_combobox.grid(row=3, column=1)
# Create a Button
# def action():
#     name = name_var.get()
#     email = email_var.get()
#     age = age_var.get()
#     print(name)
#     print(email)
#     print(age)
#

# submit_button = ttk.Button(win, text='Submit', command=action)
# submit_button.grid(row=3, column=0)

win.mainloop()

