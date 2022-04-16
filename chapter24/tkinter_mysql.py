import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql

root = tk.Tk()
root.geometry('700x300+500+300')
root.title('tkinter With MySql')

# labels
id = ttk.Label(root, text='Enter your ID : ', font=('Cinzel', 12))
id.place(x=20, y=30)

name = ttk.Label(root, text='Enter your Name : ', font=('Cinzel', 12))
name.place(x=20, y=60)

phone = ttk.Label(root, text='Enter your Phone : ', font=('Cinzel', 12))
phone.place(x=20, y=90)

# Entries

id_var = tk.StringVar()
id_entry = ttk.Entry(root, width=40, textvariable=id_var)
id_entry.place(x=200, y=30)

name_var = tk.StringVar()
name_entry = ttk.Entry(root, width=40, textvariable=name_var)
name_entry.place(x=200, y=60)

phone_var = tk.StringVar()
phone_entry = ttk.Entry(root, width=40, textvariable=phone_var)
phone_entry.place(x=200, y=90)


submit = ttk.Button(root, )


root.mainloop()