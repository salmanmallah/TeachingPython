import tkinter as tk
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import os
import sys
# import time

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

file_menu.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N', command=lambda: new_file())
file_menu.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O', command=lambda: open_file())
file_menu.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S', command=lambda: save_file())
file_menu.add_command(label='Save as', image=save_as_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S', command=lambda: save_as_file())
file_menu.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q', command=lambda: exit_file())

# Edit menu
# icon
copy_icon = tk.PhotoImage(file='icons2/copy.png')
past_icon = tk.PhotoImage(file='icons2/paste.png')
cut_icon = tk.PhotoImage(file='icons2/cut.png')
clear_icon = tk.PhotoImage(file='icons2/clear_all.png')
find_icon = tk.PhotoImage(file='icons2/find.png')

edit_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+C', command=lambda: copy_text())
edit_menu.add_command(label='Paste', image=past_icon, compound=tk.LEFT, accelerator='Ctrl+V', command=lambda: paste_text())
edit_menu.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X', command=lambda: cut_text())
edit_menu.add_command(label='Clear ALL', image=clear_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+X', command=lambda: clear_all())
edit_menu.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F', command=lambda: find_func())

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

font_size_combobox = ttk.Combobox(toolbar, width=15, state='readonly', textvariable=font_size_var)
font_size_combobox['values'] = size_tuple
font_size_combobox.current(2)
font_size_combobox.grid(row=0, column=1, padx=5)

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

# color-chooser Button
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
text_editor.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scrollbar.set)


# font family and font size


# font family functionality
def change_font_family(event=None):
    global current_font_family
    current_family = family.get()

    current_font_family = current_family
    text_editor.config(font=(current_font_family, current_font_size))


# font size functionality
def change_font_size(event=None):
    global current_font_size
    current_size = font_size_var.get()
    current_font_size = current_size
    text_editor.config(font=(current_font_family, current_font_size))


choose_font.bind('<<ComboboxSelected>>', change_font_family)
font_size_combobox.bind('<<ComboboxSelected>>', change_font_size)


# text_editor.config(font=(current_font_family, current_font_size))

# Bold Button functionality
def bold_Button():
    font_dict = font.Font(font=text_editor['font']).actual()
    if font_dict['weight'] == 'normal':
        text_editor.config(font=(current_font_family, current_font_size, 'bold'))
    elif font_dict['weight'] == 'bold':
        text_editor.config(font=(current_font_family, current_font_size, 'normal'))


bold_button.config(command=bold_Button)


# Italic Button functionality
def Italic_Button():
    font_dict = font.Font(font=text_editor['font']).actual()
    print(font_dict)
    if font_dict['slant'] == 'roman':
        text_editor.config(font=(current_font_family, current_font_size, 'italic'))
    elif font_dict['slant'] == 'italic':
        text_editor.config(font=(current_font_family, current_font_size, 'roman'))


italic_button.config(command=Italic_Button)


# Underline Button functionality
def Underline_Button():
    font_dict = font.Font(font=text_editor['font']).actual()
    print(font_dict)
    if font_dict['underline'] == 0:
        text_editor.config(font=(current_font_family, current_font_size, 'underline'))
    elif font_dict['underline'] == 1:
        text_editor.config(font=(current_font_family, current_font_size, 'normal'))


underline_button.config(command=Underline_Button)


# color-chooser functionality
def colorChooser():
    color = colorchooser.askcolor()
    text_editor.config(foreground=color[1])


color_chooser_button.config(command=colorChooser)


# Align Button Functionality

# LEFT
def align_left():
    content = text_editor.get(1.0, tk.END)
    text_editor.tag_config('left', justify=tk.LEFT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, content, 'left')


left_align_button.configure(command=align_left)


# CENTER
def align_center():
    content = text_editor.get(1.0, tk.END)
    text_editor.tag_config('center', justify=tk.CENTER)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, content, 'center')


center_align_button.configure(command=align_center)


# RIGHT
def align_right():
    content = text_editor.get(1.0, tk.END)
    text_editor.tag_config('right', justify=tk.RIGHT)
    text_editor.delete(1.0, tk.END)
    text_editor.insert(tk.INSERT, content, 'right')


right_align_button.configure(command=align_right)

current_font_family = 'Lobster'
current_font_size = 30

text_editor.configure(font=(current_font_family, current_font_size))
# ------------------------------------ End of Text Editor  -----------------------------------------------

# ------------------------------------ START OF STATUS BAR ---------------------------------------------

status = ttk.Label(text_editor, text="Status Bar", font=('Cinzel', 15))
status.pack(side=tk.BOTTOM)

# status bar functionality
text_changed = False


def status_bar(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0, 'end-1c').split())
        characters = len(text_editor.get(1.0, 'end-1c'))
        status.config(text=f'words: {words}, Characters: {characters}')
    text_editor.edit_modified(False)


text_editor.bind('<<Modified>>', status_bar)
# ------------------------------------ END OF STATUS BAR -----------------------------------------------

# ------------------------------------ START OF MAIN MENU FUNCTIONALITY -----------------------------------------------

url = ""


# NEW FILE
def new_file(event=None):
    global url
    url = ""
    text_editor.delete(1.0, tk.END)


# OPEN FILE
extensions = [('All Files', '*.*'), ('Text File', '.txt')]


def open_file(event=None):
    global url, extensions
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=extensions)
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        print('You did not select any file!')
    except:
        messagebox.showerror('Invalid file', f'OOPS!!! {sys.exc_info()[0]} is occurred')
    win.title(os.path.basename(url))


# SAVE FILE
def save_file(event=None):
    global url, extensions
    try:
        if url:
            content = str(text_editor.get(1.0, tk.END))
            with open(url, 'w') as fw:
                fw.write(content)
        else:
            content = str(text_editor.get(1.0, tk.END))
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=extensions)
            url = url.name
            with open(url, 'w') as fw:
                fw.write(content)
    except AttributeError:
        print('You did not Save the file')
    except:
        print(f'Error {sys.exc_info()}')


# SAVE AS FILE
def save_as_file(event=None):
    global url
    url = ''
    try:
        content = str(text_editor.get(1.0, tk.END))
        url = filedialog.asksaveasfile(mode='w', defaultextension='*.*', filetypes=extensions)
        url.write(content)
        url.close()
    except:
        print(f'Sorry {sys.exc_info()[0]}')


# EXIT FILE FUNCTIONALITY
def exit_file():
    global url, text_changed
    if text_changed:
        response = messagebox.askyesnocancel('Warning', 'Do you want to save the file')
        if response is True:
            save_file()
            win.destroy()
        elif response is False:
            print('data is not present, exiting the application in 3 seconds')
            win.destroy()
    else:
        print('data is not present, exiting the application')
        win.destroy()


# <><><><><><><><><><><><><><><><> Edit Menu functionality <><><><><><><><><><><><><><><><><><>

# copy text
# text_selected = ''


def copy_text(event=None):
    # global text_selected
    # selected = text_editor.selection_get()
    # text_selected = selected
    text_editor.event_generate('<Control c>')


def paste_text(event=None):
    # global text_selected
    # cursor_pos = text_editor.index(tk.INSERT)
    # text_editor.insert(cursor_pos, text_selected)
    text_editor.event_generate('<Control v>')


def cut_text(event=None):
    text_editor.event_generate('<Control x>')


def clear_all():
    text_editor.delete(1.0, tk.END)


def find_func(event=None):
    popup = tk.Toplevel()
    popup.geometry('450x250+500+200')
    popup.title('Find')
    popup.focus()
    lf = ttk.LabelFrame(popup, text='Find')
    lf.pack(pady=20)
    ttk.Button(lf, text='False Button').pack()


win.mainloop()
