import os
import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox


# starter code
main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('Vpad Text Editor')


# #########################  main menu  ##############################
main_menu = tk.Menu()
# --------File----------
# file icons
new_icon = tk.PhotoImage(file='icons2/new.png')
open_icon = tk.PhotoImage(file='icons2/open.png')
save_icon = tk.PhotoImage(file='icons2/save.png')
save_as_icon = tk.PhotoImage(file='icons2/save_as.png')
exit_icon = tk.PhotoImage(file='icons2/exit.png')

file = tk.Menu(main_menu, tearoff=False)

# ------ End File ---------

# -------- Edit ---------
# icons
copy_icon = tk.PhotoImage(file='icons2/copy.png')
paste_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_all_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')

edit = tk.Menu(main_menu, tearoff=False)


# -------- End Edit ----------

# -------- StatusBar ---------
# icons
tool_bar_icon = tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon = tk.PhotoImage(file='icons2/status_bar.png')

view = tk.Menu(main_menu, tearoff=False)

# -------- End StatusBar ---------

# ----------- Color Chooser --------------
# icons
light_defualt_icon = tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')

color_theme = tk.Menu(main_menu, tearoff=False)
theme_choice = tk.StringVar()
color_icons = (light_defualt_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)
color_dict = {
    'Light Default': ('#000000', '#ffffff'),
    'Light Plus': ('#474747', '#e0e0e0'),
    'Dark': ('#c4c4c4', '#2d2d2d'),
    'red': ('#2d2d2d', '#ffe8e8'),
    'Monokai': ('#d3b774', '#474747'),
    'Night Blue': ('#ededed', '#6b9dc2')
}

# ----------- End Color Chooser --------------

# cascade
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='ColorTheme', menu=color_theme)


# ------------&&&&&&&&&&&&&  End main menu  &&&&&&&&&&&&--------------
#
# #########################  Toolbar  ##############################

# Toolbar font setting
tool_bar = ttk.Label(main_application)
tool_bar.pack(side=tk.TOP, fill=tk.X, padx=5)

# Font Box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.grid(row=0, column=0)
font_box.current(font_tuple.index('Arial'))

# Size Box
size_var = tk.StringVar()
font_size = ttk.Combobox(tool_bar, textvariable=size_var, width=14, state='readonly')
font_size['values'] = tuple(range(8, 81, 2))
font_size.grid(row=0, column=1, padx=5)
font_size.current(4)


# Bold Button
bold_icon = tk.PhotoImage(file='icons2/bold.png')
bold_btn = ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

# Italic Button
italic_icon = tk.PhotoImage(file='icons2/italic.png')
italic_btn = ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

# Underline Button
underline_icon = tk.PhotoImage(file='icons2/underline.png')
underline_btn = ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

# Font Color Button
font_color_icon = tk.PhotoImage(file='icons2/font_color.png')
font_color_btn = ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=5, padx=5)

# Align Left Button
left_align_icon = tk.PhotoImage(file='icons2/align_left.png')
left_align_btn = ttk.Button(tool_bar, image=left_align_icon)
left_align_btn.grid(row=0, column=6, padx=5)

# Align Center Button
center_align_icon = tk.PhotoImage(file='icons2/align_center.png')
center_align_btn = ttk.Button(tool_bar, image=center_align_icon)
center_align_btn.grid(row=0, column=7, padx=5)

# Align Right Button
right_align_icon = tk.PhotoImage(file='icons2/align_right.png')
right_align_btn = ttk.Button(tool_bar, image=right_align_icon)
right_align_btn.grid(row=0, column=8, padx=5)

# ------------&&&&&&&&&&&&&  End Toolbar  &&&&&&&&&&&&--------------

# #########################  Text Editor  ##############################
# ------------&&&&&&&&&&&&&  End Text Editor  &&&&&&&&&&&&--------------

# #########################  Main Status Bar  ##############################
# ------------&&&&&&&&&&&&&  End Status Bar  &&&&&&&&&&&&--------------

# #########################  Main Menu Functionality  ##############################

# File commands
file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N')
file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O')
file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S')
file.add_command(label='Save as', image=save_as_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S')
file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Alt+F4')

# Edit Commands
edit.add_command(label='Copy', accelerator='Ctrl+C', image=copy_icon, compound=tk.LEFT)
edit.add_command(label='Past', accelerator='Ctrl+V', image=paste_icon, compound=tk.LEFT)
edit.add_command(label='Cut', accelerator='Ctrl+X', image=cut_icon, compound=tk.LEFT)
edit.add_command(label='Clear All', accelerator='Ctrl+Alt+X', image=clear_all_icon, compound=tk.LEFT)
edit.add_command(label='Find', accelerator='Ctrl+F', image=find_icon, compound=tk.LEFT)

# View Check Button
view.add_checkbutton(label='ToolBar', image=tool_bar_icon, compound=tk.LEFT)
view.add_checkbutton(label='StatusBar', image=status_bar_icon, compound=tk.LEFT)

# Color Chooser
count = 0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT)
    count += 1

# ------------&&&&&&&&&&&&&  End Main Menu Functionality  &&&&&&&&&&&&--------------

main_application.config(menu=main_menu)
main_application.mainloop()
