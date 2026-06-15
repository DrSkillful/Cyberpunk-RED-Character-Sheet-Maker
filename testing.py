# This file is for testing code, before putting it in the main file

import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont

image_first_page = Image.open("assets/1-1.png")
image_second_page = Image.open("assets/1-2.png")
image_third_page = Image.open("assets/1-3.png")

root = tk.Tk()

tk.Label(root, text="Cyberpunk RED Character Sheet Maker - by DrSkillful").grid(row=0, column=3)

def select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)

label = tk.Label(root, text="Selected Item:")
label.grid(row=1, column=1)

combo_box = ttk.Combobox(
    root,
    values=["Option 1", "Option 2", "Option 3"],
    state="readonly"
)
combo_box.grid(row=1, column=2)

combo_box.set("Option 1")

combo_box.bind("<<ComboboxSelected>>", select)

root.mainloop()