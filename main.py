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
headingFont = ("Verdana", 20, "bold")
headingLabel = Label(root, text="C&V Encryption System", font=headingFont, anchor='w')
headingLabel.grid(row=0, column=0, padx=120, pady=0)

root.mainloop()
