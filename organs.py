#GUI File
import tkinter as tk
from tkinter.ttk import Label
import tkinter.font as tkFont


root = tk.Tk()

# – – – – – – – – – – – – – – DIMENSIONS – – – – – – – – – – – – – – – – –
root.title("Unit Converter")
root.configure(background="#041775")
root.minsize(500,500)
root.maxsize(500,500)

# – – – – – – – – – – – – – – FRAMES – – – – – – – – – – – – – – – – –
custom_font = tkFont.Font(family="Arial",size=20)
Label(root, text="Unit Converter",font=custom_font).pack()








root.mainloop()
