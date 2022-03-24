import tkinter as tk
from tkinter import ttk, font


win = tk.Tk()
win.geometry('1200x800')
win.title('V Pad')
#
# # ------------------------------------ Main Menu -----------------------------------------
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

# icons
light_default_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')

theme_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Theme', menu=theme_menu)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

color_dict = {
    'Light Default ': ('#000000', '#ffffff'),
    'Light Plus': ('#474747', '#e0e0e0'),
    'Dark': ('#c4c4c4', '#2d2d2d'),
    'Red': ('#2d2d2d', '#ffe8e8'),
    'Monokai': ('#d3b774', '#474747'),
    'Night Blue': ('#ededed', '#6b9dc2')
}


def chooseTheme():
    print(theme_choice.get())


counter = 0
for i in color_dict:
    theme_menu.add_radiobutton(label=i, image=color_icons[counter], compound=tk.LEFT, variable=theme_choice, command=chooseTheme)
    counter += 1

win.config(menu=main_menu)

# ------------------------------------ End Main Menu -----------------------------------------


# ------------------------------------ Toolbar -----------------------------------------------

# choose font family
toolbar = ttk.Label(win)
toolbar.pack(fill=tk.X, side=tk.TOP)

fonts = tk.StringVar()
font_family = font.families()

choose_font = ttk.Combobox(toolbar, width=30, state='readonly', textvariable=fonts)
choose_font['values'] = font_family
choose_font.current(4)
choose_font.grid(row=0, column=0, padx=5)

# choose font size
font_size_var = tk.StringVar()
size_tuple = tuple(range(8, 81, 2))

choose_font_size = ttk.Combobox(toolbar, width=15, state='readonly', textvariable=font_size_var)
choose_font_size['values'] = size_tuple
choose_font_size.current(2)
choose_font_size.grid(row=0, column=1, padx=5)


# ToolBar Buttons
bold_icon = tk.PhotoImage(file='icons2/bold.png')
italic_icon = tk.PhotoImage(file='icons2/italic.png')
underline_icon = tk.PhotoImage(file='icons2/underline.png')

bold_button = ttk.Button(toolbar, image=bold_icon).grid(row=0, column=2)
win.mainloop()
