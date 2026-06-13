# This file is for testing code, before putting it in the main file

import tkinter as tk
from tkinter import *
from PIL import Image, ImageDraw, ImageFont

image_first_page = Image.open("assets/1-1.png")
image_second_page = Image.open("assets/1-2.png")
image_third_page = Image.open("assets/1-3.png")

stats = []

root = tk.Tk()

def imageDraw():
    draw = ImageDraw.Draw(image_first_page)
    position_y = 196
    position_start = (625, position_y)

    for i in range(10):
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
        position_y += 120 - i
        position_start = (625, position_y)

        if i == 0:
            position_y = 196
            position_start = (625, position_y)

        if i == 6 or i == 9:
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
            position_y += 20
            position_start = (670, position_y)

        draw.text(position_start, str(stats[i]), font=font)

    image_first_page.show()

def get_entry_value():

    total = int(entry1.get()) + int(entry2.get()) + int(entry3.get()) + int(entry4.get()) + int(entry5.get()) + int(entry6.get()) + int(entry7.get()) + int(entry8.get()) + int(entry9.get()) + int(entry10.get())

    tk.Label(root, text=f'Total: {total}').grid(row=11, column=1)

    if total == 62:
        stats.append(int(entry1.get()))
        stats.append(int(entry2.get()))
        stats.append(int(entry3.get()))
        stats.append(int(entry4.get()))
        stats.append(int(entry5.get()))
        stats.append(int(entry6.get()))
        stats.append(int(entry7.get()))
        stats.append(int(entry8.get()))
        stats.append(int(entry9.get()))
        stats.append(int(entry10.get()))

        print(stats)
        imageDraw()
        root.destroy()
    elif total > 62:
        ourMessage = "You have exceeded the stat point allowance of 62. Please reconfigure your stats."
        messageVar = Message(root, text=ourMessage)
        messageVar.config(bg="red")
        messageVar.grid(row=12, column=1)
        button1 = tk.Button(root, text="OK", width=15, command=lambda:[messageVar.destroy(), button1.destroy()])
        button1.grid(row=13, column=1)
    else:
        ourMessage = "Please allocate all of your stat points"
        messageVar = Message(root, text=ourMessage)
        messageVar.config(bg="red")
        messageVar.grid(row=12, column=1)
        button1 = tk.Button(root, text="OK", width=15, command=lambda: [messageVar.destroy(), button1.destroy()])
        button1.grid(row=13, column=1)

entry1 = Spinbox(root, from_=2, to=8)
entry2 = Spinbox(root, from_=2, to=8)
entry3 = Spinbox(root, from_=2, to=8)
entry4 = Spinbox(root, from_=2, to=8)
entry5 = Spinbox(root, from_=2, to=8)
entry6 = Spinbox(root, from_=2, to=8)
entry7 = Spinbox(root, from_=2, to=8)
entry8 = Spinbox(root, from_=2, to=8)
entry9 = Spinbox(root, from_=2, to=8)
entry10 = Spinbox(root, from_=2, to=8)

tk.Label(root, text="INT").grid(row=0, column=0)
tk.Label(root, text="REF").grid(row=1, column=0)
tk.Label(root, text="DEX").grid(row=2, column=0)
tk.Label(root, text="TECH").grid(row=3, column=0)
tk.Label(root, text="COOL").grid(row=4, column=0)
tk.Label(root, text="WILL").grid(row=5, column=0)
tk.Label(root, text="LUCK").grid(row=6, column=0)
tk.Label(root, text="MOVE").grid(row=7, column=0)
tk.Label(root, text="BODY").grid(row=8, column=0)
tk.Label(root, text="EMP").grid(row=9, column=0)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
entry4.grid(row=3, column=1)
entry5.grid(row=4, column=1)
entry6.grid(row=5, column=1)
entry7.grid(row=6, column=1)
entry8.grid(row=7, column=1)
entry9.grid(row=8, column=1)
entry10.grid(row=9, column=1)

button = tk.Button(root, text="Finalize stats", width=15, command=get_entry_value)
button.grid(row=10, column=1)

root.mainloop()