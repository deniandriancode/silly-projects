import base64
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd


def select_file():
    f = fd.askopenfilename()
    with open(f, "rb") as fp:
        print(fp.read())


def output_select():
    f = fd.asksaveasfilename()
    with open(f, "w") as fp:
        pass


def create_window():
    root = tk.Tk()
    root.title("Encode Decode File")
    root.resizable(False, False)

    w_width = 300
    w_height = 300

    scr_w = root.winfo_screenwidth()
    scr_h = root.winfo_screenheight()

    x_ctr = int((scr_w - w_width) / 2)
    y_ctr = int((scr_h - w_height) / 2)

    root.geometry(f"{w_width}x{w_height}+{x_ctr}+{y_ctr}")

    main_frame = ttk.Frame(root)
    main_frame.pack(fill="both", expand=True, anchor="c")

    open_btn = ttk.Button(main_frame, text="Open File", command=select_file)
    open_btn.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W+tk.E)

    output_btn = ttk.Button(main_frame, text="Select Output Name", command=output_select)
    output_btn.grid(row=1, column=0, padx=10, pady=10, columnspan=2, sticky=tk.W+tk.E)

    encode_btn = ttk.Button(main_frame, text="Encode", command=None)
    encode_btn.grid(row=2, column=1, padx=10, pady=10, sticky=tk.E)

    root.mainloop()


def main():
    create_window()



if __name__ == "__main__":
    main()
