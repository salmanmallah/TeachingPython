import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box

win = tk.Tk()
win.title("MessageBox")
win.geometry('800x300')
win.config(bg='#52ab98')

# Label Frame
label_frame = tk.LabelFrame(win, text='Contact Details', background='#2b6777')

# Labels
name_label = ttk.Label(label_frame, text='Enter your name: ', font=('Helvetica', 14, ''))
age_label = ttk.Label(label_frame, text='Enter your Age: ', font=('Helvetica', 14, ''))

# EntryBox Variables
name_var = tk.StringVar()
age_var = tk.StringVar()

# Entry Boxes
name_entry = ttk.Entry(label_frame, width=36, textvariable=name_var)
age_entry = ttk.Entry(label_frame, width=36, textvariable=age_var)


# grid
label_frame.pack(pady=50)
name_label.grid(row=0, column=0, pady=5, padx=5)
name_entry.grid(row=1, column=0, pady=5, padx=5)

age_label.grid(row=0, column=1, pady=5, padx=5)
age_entry.grid(row=1, column=1, pady=5, padx=5)


# Submit Button
def message_box():
    name = name_var.get()
    age = age_var.get()
    if name == '' and age == '':
        m_box.showerror('Error', "Please fill the form first")
    else:
        try:
            age = int(age)
        except ValueError:
            m_box.showerror('Invalid input', 'Please enter your age in digits')
        else:
            print(f'Hello {name} your age is {age}')
            m_box.showinfo('Login Successful', f'Hello sir {name}\nYour age is {age}')


submit_button = ttk.Button(label_frame, text='Submit', width=40, command=message_box)
submit_button.grid(row=2, columnspan=2)


win.mainloop()
