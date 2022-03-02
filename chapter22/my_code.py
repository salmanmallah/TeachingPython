import tkinter as tk
from tkinter import ttk
from csv import DictWriter

win = tk.Tk()
win.title('My Code')
win.geometry('600x300')

# create labels
name_label = ttk.Label(win, text='Enter your Name:')
name_label.grid(row=0, column=0)

email_label = ttk.Label(win, text='Enter your Email:')
email_label.grid(row=1, column=0)

age_label = ttk.Label(win, text='Enter you Age:')
age_label.grid(row=2, column=0, sticky=tk.W)

gender_label = ttk.Label(win, text='Enter you Age:')
gender_label.grid(row=3, column=0, sticky=tk.W)


# Create EntryBox
name_var = tk.StringVar()
name_entry = ttk.Entry(win, textvariable=name_var)
name_entry.grid(row=0, column=1)
name_entry.focus()

email_var = tk.StringVar()
email_entry = ttk.Entry(win, textvariable=email_var)
email_entry.grid(row=1, column=1)

age_var = tk.StringVar()
age_entry = ttk.Entry(win, textvariable=age_var)
age_entry.grid(row=2, column=1)


# Create ComboBox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win, values=['Male', 'Female', 'Other'], textvariable=gender_var, state='readonly')
gender_combobox.grid(row=3, column=1)
gender_combobox.current(0)


# Create RadioButton
usertype_var = tk.StringVar()

radio_button1 = ttk.Radiobutton(win, text='Teacher', value='Teacher', variable=usertype_var)
radio_button1.grid(row=4, column=0)

radio_button2 = ttk.Radiobutton(win, text='Student', value='Student', variable=usertype_var)
radio_button2.grid(row=4, column=1)


# Create CheckBox
checkbox_var = tk.StringVar()
check_button = ttk.Checkbutton(win, text='Agree Terms and Conditions', variable=checkbox_var)
check_button.grid(row=5, columnspan=3)

# Create Submit Button


def action():
    name = name_var.get()
    email = email_var.get()
    age = age_var.get()
    gender = gender_var.get()
    usertype = usertype_var.get()
    useragree = checkbox_var.get()
    print(name, email, age, gender, usertype, useragree)

    with open('salman.csv', 'a', newline="") as wf:
        csv_writer = DictWriter(wf, fieldnames=['User Name', 'User Email', 'User Age', 'User Gender', 'User Type', 'Terms & Conditions'])
        csv_writer.writeheader()


submit_button = tk.Button(win, text='Submit', width=40, activebackground='#2596be', height=2, command=action)
submit_button.grid(row=6, columnspan=5)

win.mainloop()
