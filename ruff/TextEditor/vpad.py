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

family = tk.StringVar()
font_family = font.families()

choose_font = ttk.Combobox(toolbar, width=30, state='readonly', textvariable=family)
choose_font['values'] = font_family
choose_font.current(2)
choose_font.grid(row=0, column=0, padx=5)

# choose font size
font_size_var = tk.StringVar()
size_tuple = tuple(range(8, 81, 2))

choose_font_size = ttk.Combobox(toolbar, width=15, state='readonly', textvariable=font_size_var)
choose_font_size['values'] = size_tuple
choose_font_size.current(2)
choose_font_size.grid(row=0, column=1, padx=5)

# ToolBar Buttons
# icons
bold_icon = tk.PhotoImage(file='icons2/bold.png')
italic_icon = tk.PhotoImage(file='icons2/italic.png')
underline_icon = tk.PhotoImage(file='icons2/underline.png')
color_chooser_icon = tk.PhotoImage(file='icons2/font_color.png')
align_left_icon = tk.PhotoImage(file='icons2/align_left.png')
align_center_icon = tk.PhotoImage(file='icons2/align_center.png')
align_right_icon = tk.PhotoImage(file='icons2/align_right.png')

bold_button = ttk.Button(toolbar, image=bold_icon)
bold_button.grid(row=0, column=2, padx=5)

italic_button = ttk.Button(toolbar, image=italic_icon)
italic_button.grid(row=0, column=3, padx=5)

underline_button = ttk.Button(toolbar, image=underline_icon)
underline_button.grid(row=0, column=4, padx=5)

color_chooser_button = ttk.Button(toolbar, image=color_chooser_icon)
color_chooser_button.grid(row=0, column=5, padx=5)

# alignment Button
left_align_button = ttk.Button(toolbar, image=align_left_icon)
left_align_button.grid(row=0, column=6, padx=5)

center_align_button = ttk.Button(toolbar, image=align_left_icon)
center_align_button.grid(row=0, column=7, padx=5)

right_align_button = ttk.Button(toolbar, image=align_left_icon)
right_align_button.grid(row=0, column=8, padx=5)

# ------------------------------------ End Toolbar -----------------------------------------------

# ------------------------------------ Start of Text Editor -----------------------------------------------

text_editor = tk.Text(win)
text_editor.config(wrap='word', relief=tk.FLAT)

scrollbar = tk.Scrollbar(win)
text_editor.focus()
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill='both', expand=tk.TRUE)
scrollbar.config(command=text_editor.yview())
text_editor.config(yscrollcommand=scrollbar.set)

# font family and font size
current_font_family = 'Lobster'
current_font_size = 30
text_editor.config(font=(current_font_family, current_font_size))

# ------------------------------------ End of Text Editor  -----------------------------------------------

# ------------------------------------ START OF STATUS BAR ---------------------------------------------

status_bar = tk.Label(win, text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

# ------------------------------------ END OF STATUS BAR -----------------------------------------------

win.mainloop()
