# chapter 22
# tutorial no. 239
# TAB Control widget

# Starter code
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('NoteBook')
win.geometry('800x300')

nb = ttk.Notebook(win)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
page3 = ttk.Frame(nb)
nb.add(page1, text='PAGE ONE')
nb.add(page2, text='PAGE TWO')
nb.add(page3, text='PAGE THREE')
nb.pack(expand=True, fill='both')

# creating label in page1
labels = ['Enter your name : ', 'Enter your Email : ', 'Enter your age : ']
for i in range(len(labels)):
    ttk.Label(page1, text=labels[i]).grid(row=i, column=0, pady=4)
    ttk.Entry(page1).grid(row=i, column=1)

win.mainloop()
