import tkinter as tk
from tkinter import Label, Entry, Button


def main():
    root = tk.Tk()
    root.geometry("500x300")
    root.resizable(0,0)
    root.title("Tkinter Example")

    Label(root, text="ENCODE DECODE", font="Ubuntu 20 bold").pack()
    Label(root, text="Python Project", font="Ubuntu 18 normal").pack(side=tk.BOTTOM)

    root.mainloop()


if __name__ == "__main__":
    main()
