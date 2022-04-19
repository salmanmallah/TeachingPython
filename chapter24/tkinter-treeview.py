import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql

db = mysql.connect(host='localhost', user='root', password='', database='school')
cursor = db.cursor()

root = tk.Tk()
root.geometry('1300x700+0+0')
root.title('TreeView')


# search function
def search():
    global cursor
    search_word = entrydata.get()
    if search_word == '':
        messagebox.showwarning('input status', 'please type something to search')
    else:
        query = r'SELECT id, first_name, last_name, age FROM customer WHERE first_name LIKE "' + search_word + '" OR last_name LIKE "' + search_word +'"'
        cursor.execute(query)
        rows = cursor.fetchall()
        update(rows)


def clear():
    trv.delete(*trv.get_children())
    query = "SELECT id, first_name, last_name, age FROM customer "
    cursor.execute(query)
    row = cursor.fetchall()
    update(row)

def update(rows):
    trv.delete(*trv.get_children())
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
query = "SELECT id, first_name, last_name, age FROM customer "
cursor.execute(query)
row = cursor.fetchall()

update(row)


# Search Section
label = ttk.Label(wrapper2, text='Search')
label.pack(side=tk.LEFT, padx=10)

entrydata = tk.StringVar()
entry = ttk.Entry(wrapper2, textvariable=entrydata)
entry.pack(side=tk.LEFT, padx=6)

button = ttk.Button(wrapper2, text='Submit', command=search)
button.pack(side=tk.LEFT, padx=6)

clear_btn = ttk.Button(wrapper2, text='Clear', command=clear)
clear_btn.pack(side=tk.LEFT, padx=6)


# customer data section



root.mainloop()
