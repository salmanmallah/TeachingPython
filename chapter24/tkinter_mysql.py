import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql
import sys



root = tk.Tk()
root.geometry('800x700+500+200')
root.title('tkinter With MySql')

wrapper1 = tk.LabelFrame(root, text='Student From')
wrapper1.pack(fill='both', expand=True, pady=20, padx=10)
# labels
id_label = ttk.Label(wrapper1, text='Enter your ID : ', font=('Cinzel', 12))
id_label.place(x=20, y=30)

name = ttk.Label(wrapper1, text='Enter your Name : ', font=('Cinzel', 12))
name.place(x=20, y=60)

phone = ttk.Label(wrapper1, text='Enter your Phone : ', font=('Cinzel', 12))
phone.place(x=20, y=90)

# Entries

id_var = tk.StringVar()
id_entry = ttk.Entry(wrapper1, width=40, textvariable=id_var)
id_entry.place(x=200, y=30)


name_var = tk.StringVar()
name_entry = ttk.Entry(wrapper1, width=40, textvariable=name_var, )
name_entry.place(x=200, y=60)
name_entry.focus()

phone_var = tk.StringVar()
phone_entry = ttk.Entry(wrapper1, width=40, textvariable=phone_var, )
phone_entry.place(x=200, y=90)

# submit button
submit = tk.Button(wrapper1, text='Create', width=60, command=lambda: insert())
submit.config(background='green', height=2, foreground='yellow')
submit.place(x=20, y=120)

# Delete Button
delete_button = tk.Button(wrapper1, text='Delete', width=20, command=lambda: delete())
delete_button.config(background='red', foreground='white')
delete_button.place(x=470, y=30)

# Update Button
update_button = tk.Button(wrapper1, text='Update', width=20, command=lambda: update())
update_button.config(background='yellow', foreground='red')
update_button.place(x=470, y=60)

# GET BUTTON
get_button = tk.Button(wrapper1, text='GET', width=20, command=lambda: get())
get_button.config(background='Blue', foreground='white')
get_button.place(x=470, y=90)


wrapper2 = tk.LabelFrame(root, text='Student Record')
wrapper2.pack(fill='both', expand=True, padx=10, pady=20)

treeview = ttk.Treeview(wrapper2, show='headings', columns=(1,2,3), height=6)
treeview.pack(fill='both', expand=True, pady=5)

# headings
treeview.heading(1, text='Student Id', anchor=tk.W)
treeview.heading(2, text='Student Name', anchor=tk.W)
treeview.heading(3, text='Student Phone', anchor=tk.W)

# data = (1, 'Salman', '03002368652')
def show():
    con = mysql.connect(host='localhost', user='root', password='', database='python_tkinter')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM student')
    row = cursor.fetchall()
    # first delete all children
    for rows in treeview.get_children():
        treeview.delete(rows)

    # show all children
    for rows in row:
        treeview.insert('', tk.END, values=rows)

# ############################# USER-MADE FUNCTIONS #################################
# function to insert data in Mysql
def insert():

    id_ = id_var.get()
    name_ = name_var.get()
    phone_ = phone_var.get()

    if name_ == '' or phone_ == '':
        messagebox.showwarning('Error', 'All field are Required*')
    else:
        # make connection
        con = mysql.connect(host='localhost', user='root', password='', database='python_tkinter')
        cursor = con.cursor()

        # inserting data into database
        cursor.execute("INSERT INTO student (name, phone) VALUES('" + name_ + "','" + phone_ + "')")
        cursor.execute('commit')

        # erase form data
        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        show()
        # showing success message
        messagebox.showinfo('Status', 'Data Inserted Successfully')
        con.close()


# Delete Data from mysql database
def delete():
    id_ = id_var.get()

    if id_ == '':
        messagebox.showwarning('input info', 'Please enter your Student id to Delete')
    else:
        con = mysql.connect(host='localhost', user='root', password='', database='python_tkinter')
        cursor = con.cursor()
        cursor.execute('DELETE FROM student WHERE id="' + id_ + '"')
        cursor.execute('commit')

        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        show()
        messagebox.showinfo('status', 'Data Deleted Successfully')


# update data from mysql database.
def update():
    id_ = id_var.get()
    name = name_var.get()
    phone = phone_var.get()
    if id_ == '' or name == '' or phone == '':
        messagebox.showwarning('input status', 'All fields are Required**')
    else:
        con = mysql.connect(host='localhost', user='root', password='', database='python_tkinter')
        cursor = con.cursor()
        cursor.execute("UPDATE student SET name='" + name + "', phone='" + phone + "' WHERE id= '" + id_ + "' ")
        cursor.execute('commit')

        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        show()
        messagebox.showinfo('Status', 'Successfully updated!')


def get():
    global name_entry
    global phone_entry

    id_ = id_var.get()
    if id_ == '':
        messagebox.showwarning('input status', 'Please enter your id to fetch data')
    else:
        con = mysql.connect(host='localhost', user='root', password='', database='python_tkinter')
        cursor = con.cursor()
        cursor.execute('SELECT * FROM student WHERE id="' + id_ + '" ')
        tables = cursor.fetchall()
        # counter = 0

        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)

        for rows in tables:
            name_entry.insert(0, rows[1])
            phone_entry.insert(0, rows[2])


show()

root.mainloop()
