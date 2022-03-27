# starter code
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('ManuBar')
win.geometry('800x300')

# Menu

# ************  Simple MenuBar  *********************
# menubar = tk.Menu(win)
# menubar.add_command(label='File', command=lambda: print('file func called'))
# menubar.add_command(label='Edit', command=lambda: print('Edit func called'))
# menubar.add_command(label='View', command=lambda: print('Viewfunc called'))
# menubar.add_command(label='Navigate', command=lambda: print('Navigate func called'))
# menubar.add_command(label='Code', command=lambda: print('Code func called'))
# menubar.add_command(label='Refactor', command=lambda: print('Refactor func called'))
# menubar.add_command(label='Run', command=lambda: print('Run func called'))
# menubar.add_command(label='Tools', command=lambda: print('Tools func called'))
# menubar.add_command(label='Git', command=lambda: print('Git func called'))
# menubar.add_command(label='Help', command=lambda: print('Help func called'))
# menubar.add_command(label='Window', command=lambda: print('Window func called'))
# win.config(menu=menubar)

main_menu = tk.Menu(win)

# File Menu
file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='File', menu=file_menu)
# file_menu.add_command(label='New Project', command=lambda: print('new project func called'))
# file_menu.add_command(label='New', command=lambda: print('new project func called'))
# file_menu.add_command(label='New scratch file', command=lambda: print('new project func called'))
# file_menu.add_command(label='Open', command=lambda: print('new project func called'))

# Edit Menu
edit_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Edit', menu=edit_menu)
# edit_menu.add_command(label='Undo', command=lambda: print('undo func called'))
# edit_menu.add_command(label='Redo', command=lambda: print('Redo func called'))
# edit_menu.add_separator()
# edit_menu.add_command(label='Cut', command=lambda: print('Cut func called'))
# edit_menu.add_command(label='Copy', command=lambda: print('copy func called'))
# edit_menu.add_separator()
# edit_menu.add_command(label='past'.title(), command=lambda: print('Past func called'))
# edit_menu.add_command(label='delete'.title(), command=lambda: print('Delete func called'))

win.config(menu=main_menu)

win.mainloop()
