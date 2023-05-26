import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk


def select_file():
    filename = fd.askopenfilename()
    with open(filename, "r") as fp:
        print(fp.read())


root = tk.Tk()
root.title("Python - Tkinter")
root.resizable(False, False)

w_width = 500
w_height = 300

scr_w = root.winfo_screenwidth()
scr_h = root.winfo_screenheight()

x_ctr = int((scr_w - w_width) / 2)
y_ctr = int((scr_h - w_height) / 2)

root.geometry(f"{w_width}x{w_height}+{x_ctr}+{y_ctr}")


open_btn = ttk.Button(root, text="Open File", command=select_file)
open_btn.pack()

# filename = fd.askopenfilename()


root.mainloop()
