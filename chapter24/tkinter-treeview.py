import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql

db = mysql.connect(host='localhost', user='root', password='', database='school')
cursor = db.cursor()

root = tk.Tk()
root.geometry('1300x700+0+0')
root.title('TreeView')


def update(rows):
    for i in rows:
        trv.insert('', tk.END, values=i,)



# wrappers
wrapper1 = tk.LabelFrame(root, text='Customer List')
wrapper2 = tk.LabelFrame(root, text='Search')
wrapper3 = tk.LabelFrame(root, text='Customer Data')

# packing
wrapper1.pack(fill='both', expand=True, padx=20, pady=10)
wrapper2.pack(fill='both', expand=True, padx=20, pady=10)
wrapper3.pack(fill='both', expand=True, padx=20, pady=10)

# TreeView
trv = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4), show='headings', height=6)
trv.pack(fill='both', expand=True, padx=2, pady=2)

# table header
trv.heading(1, text='Customer ID', anchor=tk.W)
trv.heading(2, text='First Name', anchor=tk.W)
trv.heading(3, text='Last Name', anchor=tk.W)
trv.heading(4, text='Age', anchor=tk.W)

# column setting
trv.column(1, anchor=tk.W, width=20)
trv.column(2, anchor=tk.W, )
trv.column(3, anchor=tk.W,)
trv.column(4, anchor=tk.W,)





# mysql Query
# query = "SELECT id, first_name, last_name, age FROM customer "
# cursor.execute(query)
# # row = cursor.fetchall()
#
# update(row)



root.mainloop()
