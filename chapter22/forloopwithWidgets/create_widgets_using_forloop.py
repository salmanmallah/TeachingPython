import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("widgets With For loops")
win.geometry('400x200')

# Create Labels

labels = ['Enter your Name: ', 'Enter your Email: ', 'Enter your Age: ']
for label in range(len(labels)):
    current_label = 'label' + str(label)
    current_label = ttk.Label(win, text=labels[label])
    current_label.grid(row=label, column=0, sticky=tk.W)

# Create EntryBox
userinfo = {
    'name': tk.StringVar(),
    'email': tk.StringVar(),
    'age': tk.StringVar()
}
counter = 0
for i in userinfo:
    cur_entrybox = i + '_entry'
    cur_entrybox = ttk.Entry(win, textvariable=userinfo[i])
    cur_entrybox.grid(row=counter, column=1)
    counter += 1


# Submit Button
def action():
    print(userinfo['name'].get())
    print(userinfo['email'].get())
    print(userinfo['age'].get())


ttk.Button(win, text='Click Me', command=action).grid(row=3)


win.mainloop()
