import tkinter as tk
from tkinter import colorchooser

root = tk.Tk()
root.title('Color Chooser')
root.geometry('1350x700+0+0')
root.config(background='#283593')

# Color Chooser Button
color_button = tk.Button(root, text='ColorChoose', background='#5f5fc4', fg='#ffffff', padx='25', pady='25', command=lambda: choose_theme())
color_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


def choose_theme():
    rgb_value = colorchooser.askcolor()
    hex_color = rgb_value[1]
    # print(hex_color)

    # def opposite_color(Hex):
    #     if Hex[0] == '#':
    #         Hex = Hex[1:]
    #     rgb = (Hex[0:2], Hex[2:4], Hex[4:6])
    #     comp = ['%02x' % (255 - int(a, 16)) for a in rgb]
    #     return ''.join(comp)

    # set_button_color = opposite_color(hex_color)
    root.config(background=rgb_value[1])
    # color_button.config(background='#' +set_button_color)


root.mainloop()
