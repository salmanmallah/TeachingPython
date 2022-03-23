import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.geometry('1200x800')
win.title('V Pad')
#
# # ------------------- Main Menu
main_menu = tk.Menu(win)
#
# file menu
# icon
new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')

file_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N')
file_menu.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O')
file_menu.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S')
file_menu.add_command(label='Save as', image=save_as_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S')
file_menu.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q')


# Edit menu
# icon
copy_icon = tk.PhotoImage(file='icons2/copy.png')
past_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')

edit_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+C')
edit_menu.add_command(label='Past', image=past_icon, compound=tk.LEFT, accelerator='Ctrl+V')
edit_menu.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X')
edit_menu.add_command(label='Clear', image=clear_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+X')
edit_menu.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F')

# View menu
toolbar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
statusbar_icon = tk.PhotoImage(file='icons2/status_bar.png')

view_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='View', menu=view_menu)

view_menu.add_checkbutton(label='ToolBar', image=toolbar_icon, compound=tk.LEFT)
view_menu.add_checkbutton(label='Status Bar', image=statusbar_icon, compound=tk.LEFT)

# Theme menu
theme_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Theme', menu=theme_menu)



win.config(menu=main_menu)

# ------------------- End Main Menu


win.mainloop()
