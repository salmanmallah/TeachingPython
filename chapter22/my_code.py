import tkinter as tk
from tkinter import ttk

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
name_entry = ttk.Entry(win)
name_entry.grid(row=0, column=1)
name_entry.focus()

email_entry = ttk.Entry(win)
email_entry.grid(row=1, column=1)

age_entry = ttk.Entry(win)
age_entry.grid(row=2, column=1)


# Create ComboBox
gender_combobox = ttk.Combobox(win, values=['Male', 'Female', 'Other'])
gender_combobox.grid(row=3, column=1)
gender_combobox.current(0)


# Create RadioButton
radio_button1 = ttk.Radiobutton(win, text='Teacher', value='Teacher')
radio_button1.grid(row=4, column=0)

radio_button2 = ttk.Radiobutton(win, text='Student', value='Student')
radio_button2.grid(row=4, column=1)


# Create CheckBox
check_button = ttk.Checkbutton(win, text='Agree Terms and Conditions')
check_button.grid(row=5, columnspan=3)

# Create Submit Button
submit_button = ttk.Button(win, text='Submit')
submit_button.grid(row=6)

win.mainloop()
