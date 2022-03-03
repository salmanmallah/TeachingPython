import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os

win = tk.Tk()
win.title('My Code')
win.geometry('600x300')

# create labels
labels = ['Enter your Name : ', 'Enter your Email : ', 'Enter you Age : ', 'Enter you Gender : ']
for i in range(len(labels)):
    name_label = ttk.Label(win, text=labels[i])
    name_label.grid(row=i, column=0, sticky=tk.W)


# Create EntryBox
entryBox_var = {
    'name': tk.StringVar(),
    'email': tk.StringVar(),
    'age': tk.StringVar()
}
counter = 0
for i in entryBox_var:
    cur_entrybox = ttk.Entry(win, textvariable=entryBox_var[i])
    cur_entrybox.grid(row=counter, column=1)
    counter += 1


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
checkbox_var = tk.IntVar()
check_button = ttk.Checkbutton(win, text='Agree Terms and Conditions', variable=checkbox_var)
check_button.grid(row=5, columnspan=3)

# Create Submit Button


def action():
    name = entryBox_var['name'].get()
    email = entryBox_var['email'].get()
    age = entryBox_var['age'].get()
    gender = gender_var.get()
    usertype = usertype_var.get()
    if checkbox_var.get() != 0:
        user_agree = 'YES'
    else:
        user_agree = 'NO'
    print(name, email, age, gender, usertype, user_agree)

    with open('salman.csv', 'a', newline="") as wf:
        csv_writer = DictWriter(wf, fieldnames=['UserName', 'UserEmail', 'UserAge', 'UserGender', 'UserType',
                                                'AcceptTerm'])
        if os.stat('salman.csv').st_size == 0:
            csv_writer.writeheader()
        csv_writer.writerow({
          'UserName': name,
          'UserEmail': email,
          'UserAge': age,
          'UserGender': gender,
          'UserType': usertype,
          'AcceptTerm': user_agree,
        })
    win.destroy()


submit_button = tk.Button(win, text='Submit', width=40, activebackground='#2596be', height=2, command=action)
submit_button.grid(row=6, columnspan=5)

win.mainloop()
