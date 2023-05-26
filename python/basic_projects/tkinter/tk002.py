import tkinter as tk

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

message = tk.Label(root, text="Hello, Tkinter World!")
message.pack()

root.mainloop()
