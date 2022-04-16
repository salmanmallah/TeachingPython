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
id_entry = ttk.Entry(root, width=40, textvariable=id_var, )
id_entry.place(x=200, y=30)

name_var = tk.StringVar()
name_entry = ttk.Entry(root, width=40, textvariable=name_var, )
name_entry.place(x=200, y=60)

phone_var = tk.StringVar()
phone_entry = ttk.Entry(root, width=40, textvariable=phone_var, )
phone_entry.place(x=200, y=90)

submit = tk.Button(root, text='Submit', width=60, command=lambda: insert())
submit.config(background='green', height=2)
submit.place(x=20, y=120)


# function to insert data in Mysql
def insert(event=None):
    id = id_var.get()
    name = name_var.get()
    phone = phone_var.get()

    if id == '' or name == '' or phone == '':
        messagebox.showwarning('Error', 'All field are Required*')
    else:
        print(id, name, phone)
        # con = mysql.connect(host='localhost', user=root, password='!salman06', database='python-tkinter')
        # cursor = con.cursor()
        # cursor.execute("INSERT INTO student VALUES('" + id + "','" + name + "','" + phone + "')")
        # cursor.execute('commit');
        #
        # messagebox.showinfo('Status','Data Inserted Successfully')
        # con.close();

root.mainloop()
