#   Author : Swaraj Pande
#
#   C&V Encryption System (Caesar and Vigenère Cipher)
#
#   Date :


import ciphers
from tkinter import *
from tkinter.messagebox import *

# Creating the Window
root = Tk()
root.title("C&V Encryption System")
root.geometry("600x750")

# Heading Label
headingFont = ("Verdana", 18, "bold")
heading = Label(root, text="C&V Encryption System", font=headingFont)
heading.pack(side=TOP, pady=10)

root.mainloop()
