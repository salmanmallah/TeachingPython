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
    search_word = entry_data.get()
    if search_word == '':
        messagebox.showwarning('input status', 'please type something to search')
    else:
        sqlQuery = r'SELECT id, first_name, last_name, age FROM customer WHERE first_name LIKE "' + search_word + '" OR last_name LIKE "' + search_word + '"'
        cursor.execute(sqlQuery)
        rows = cursor.fetchall()
        update(rows)


# clear function
def clear():
    trv.delete(*trv.get_children())
    sqlQuery = "SELECT id, first_name, last_name, age FROM customer "
    cursor.execute(sqlQuery)
    rows = cursor.fetchall()
    update(rows)


# update function
def update(rows):
    trv.delete(*trv.get_children())
    for i in rows:
        trv.insert('', tk.END, values=i, )


# delete function
def delete_customer():
    customer_id = entry_one.get()
    if messagebox.askyesno('comfirm Delete?', 'Are you sure you want to delete this customer?'):
        sqlQuery = r'DELETE FROM customer WHERE id="' + customer_id + '"'
        cursor.execute(sqlQuery)
        cursor.execute('commit')
        clear()
        id_entry.delete(0, tk.END)
        fname_entry.delete(0, tk.END)
        lname_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        messagebox.showinfo('Delete Status', 'Customer is removed permanently!')


# update_customer function
def update_customer():
    customer_id = entry_one.get()
    first_name = entry_two.get()
    last_name = entry_three.get()
    age = entry_four.get()
    print(customer_id, first_name, last_name, age)

    sqlQuery = 'UPDATE customer SET first_name= "' + first_name + '", last_name="' + last_name + '", age="' + age + '" WHERE id="' + customer_id + '"'
    cursor.execute(sqlQuery)
    cursor.execute('commit')
    clear()


# add new customer function
def add_customer():
    first_name = entry_two.get()
    last_name = entry_three.get()
    age = entry_four.get()
    sqlQuery = 'INSERT INTO customer (first_name, last_name, age) VALUES ("' + first_name + '", "' + last_name + '", "' + age + '")'
    cursor.execute(sqlQuery)
    cursor.execute('commit')

    # clear entry field
    fname_entry.delete(0, tk.END)
    lname_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    clear()


# get-row function
def get_rows(event):
    # global entry_one, entry_two, entry_three, entry_four
    # rowid = trv.identify_row(event.x)
    item = trv.item(trv.focus())
    entry_one.set(item['values'][0])
    entry_two.set(item['values'][1])
    entry_three.set(item['values'][2])
    entry_four.set(item['values'][3])


# wrappers
wrapper1 = tk.LabelFrame(root, text='Customer List')
wrapper2 = tk.LabelFrame(root, text='Search')
wrapper3 = tk.LabelFrame(root, text='Customer Data')

# packing
wrapper1.pack(fill='both', expand=True, padx=20, pady=10)
wrapper2.pack(fill='both', expand=True, padx=20, pady=10)
wrapper3.pack(fill='both', expand=True, padx=20, pady=10)

# TreeView
trv = ttk.Treeview(wrapper1, columns=('1', '2', '3', '4'), show='headings', height=6)
trv.pack(fill='both', expand=True, padx=2, pady=2)

# table header
trv.heading(1, text='Customer ID', anchor=tk.W)
trv.heading(2, text='First Name', anchor=tk.W)
trv.heading(3, text='Last Name', anchor=tk.W)
trv.heading(4, text='Age', anchor=tk.W)

# column setting
trv.column(1, anchor=tk.W, width=20)
trv.column(2, anchor=tk.W, )
trv.column(3, anchor=tk.W, )
trv.column(4, anchor=tk.W, )

# Scroll-Bar of TreeView
scrollbar = ttk.Scrollbar(trv, orient='vertical', command=trv.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# communicate back to the scrollbar
trv.config(yscrollcommand=scrollbar.set)

# mysql Query
query = "SELECT id, first_name, last_name, age FROM customer "
cursor.execute(query)
row = cursor.fetchall()

update(row)

# Search Section
label = ttk.Label(wrapper2, text='Search')
label.pack(side=tk.LEFT, padx=10)

entry_data = tk.StringVar()
entry = ttk.Entry(wrapper2, textvariable=entry_data)
entry.pack(side=tk.LEFT, padx=6)

button = ttk.Button(wrapper2, text='Submit', command=search)
button.pack(side=tk.LEFT, padx=6)

clear_btn = ttk.Button(wrapper2, text='Clear', command=clear)
clear_btn.pack(side=tk.LEFT, padx=6)

# customer data section

# entry variable
entry_one = tk.StringVar()
entry_two = tk.StringVar()
entry_three = tk.StringVar()
entry_four = tk.StringVar()

id_label = ttk.Label(wrapper3, text="Customer ID", font=('Roboto Mono', 10, 'bold'))
id_label.grid(column=0, row=0, padx=20, pady=5)
id_entry = ttk.Entry(wrapper3, width=15, textvariable=entry_one)
id_entry.grid(column=1, row=0, padx=10, pady=5)

fname_label = ttk.Label(wrapper3, text="First Name", font=('Roboto Mono', 10, 'bold'))
fname_label.grid(column=0, row=1, padx=20, pady=5)
fname_entry = ttk.Entry(wrapper3, width=15, textvariable=entry_two)
fname_entry.grid(column=1, row=1, padx=10, pady=5)

lname_label = ttk.Label(wrapper3, text="Last Name", font=('Roboto Mono', 10, 'bold'))
lname_label.grid(column=0, row=2, padx=20, pady=5)
lname_entry = ttk.Entry(wrapper3, width=15, textvariable=entry_three)
lname_entry.grid(column=1, row=2, padx=10, pady=5)

age_label = ttk.Label(wrapper3, text="Age", font=('Roboto Mono', 10, 'bold'))
age_label.grid(column=0, row=3, padx=20, pady=5)
age_entry = ttk.Entry(wrapper3, width=15, textvariable=entry_four)
age_entry.grid(column=1, row=3, padx=10, pady=5)

add_button = ttk.Button(wrapper3, text='Add New', command=add_customer)
update_button = ttk.Button(wrapper3, text='Update', command=update_customer)
delete_button = ttk.Button(wrapper3, text='Delete', command=delete_customer)

add_button.grid(row=4, column=0, padx=5, pady=3)
update_button.grid(row=4, column=1, padx=5, pady=3)
delete_button.grid(row=4, column=2, padx=5, pady=3)

trv.bind('<Double 1>', get_rows)

root.mainloop()
