import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("widgets With For loops")
win.geometry('1200x800')


# Create Labels Frames
frame = ttk.LabelFrame(win, text='Enter your details below')
frame.grid(row=0, column=0, padx=40)
# style = ttk.Style()
# style.configure('TLabelframe', background='Black')

labels = ['Enter your Name: ', 'Enter your Email: ', 'Enter your Age: ', 'Your Country : ', 'Your Province : ',
          'Your City', 'Your Number : ']
for label in range(len(labels)):
    current_label = 'label' + str(label)
    current_label = ttk.Label(frame, text=labels[label])
    current_label.grid(row=label, column=0, sticky=tk.W)

# Create EntryBox
userinfo = {
    'name': tk.StringVar(),
    'email': tk.StringVar(),
    'age': tk.StringVar(),
    'country': tk.StringVar(),
    'province': tk.StringVar(),
    'city': tk.StringVar(),
    'number': tk.StringVar()
}
counter = 0
for i in userinfo:
    # cur_entrybox = i + '_entry'
    ttk.Entry(frame, textvariable=userinfo[i]).grid(row=counter, column=1)
    counter += 1


# Submit Button
def action():
    print(userinfo['name'].get())
    print(userinfo['email'].get())
    print(userinfo['age'].get())
    print(userinfo['country'].get())
    print(userinfo['province'].get())
    print(userinfo['city'].get())
    print(userinfo['number'].get())
    win.destroy()


for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

ttk.Button(win, text='Click Me', command=action, width=50).grid(row=1, sticky=tk.W)

win.mainloop()
