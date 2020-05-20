#   Author : Swaraj Pande
#
#   C&V Encryption System (Caesar and Vigenère Cipher)
#
#   Date : 20 May 2020


import ciphers
from tkinter import *
from tkinter.messagebox import *

# Creating the Window
root = Tk()
root.title("C&V Encryption System")
root.geometry("600x700")
root.resizable(False, False)

# Heading Label
headingFont = ("Verdana", 20, "bold")
headingLabel = Label(root, text="C&V Encryption System", font=headingFont)
headingLabel.pack(side=TOP)

# General Font
generalFont = ("Times", 12)

# Cipher Choice
cipherChoice = IntVar()
cipherChoice.set("1")
cipherChoiceLabel = Label(root, text="Choose Cipher : ", font=generalFont, anchor='w')
cipherChoiceLabel.place(x=170, y=50)
caesarCipherRadiobutton = Radiobutton(root, text="Caesar Cipher", font=generalFont, variable=cipherChoice, value=1)
caesarCipherRadiobutton.place(x=290, y=49)
vigenereCipherRadiobutton = Radiobutton(root, text="Vigenere Cipher", font=generalFont, variable=cipherChoice, value=2)
vigenereCipherRadiobutton.place(x=290, y=74)

# Operation Choice
operationChoice = IntVar()
operationChoice.set("1")
operationChoiceLabel = Label(root, text="Choose Operation : ", font=generalFont, anchor='w')
operationChoiceLabel.place(x=151, y=119)
encryptionRadiobutton = Radiobutton(root, text="Encryption", font=generalFont, variable=operationChoice, value=1)
encryptionRadiobutton.place(x=290, y=118)
decryptionRadiobutton = Radiobutton(root, text="Decryption", font=generalFont, variable=operationChoice, value=2)
decryptionRadiobutton.place(x=290, y=143)

# Enter Text Field
enterTextLabel = Label(root, text="Enter Text : ", font=generalFont, anchor='w')
enterTextLabel.place(x=30, y=200)
enterText = Text(root, height=8, width=67)
enterText.place(x=30, y=225)

# Enter Key Field
enterKeyLabel = Label(root, text="Enter Key : ", font=generalFont, anchor='w')
enterKeyLabel.place(x=30, y=370)
enterKey = Text(root, height=1, width=67)
enterKey.place(x=30, y=400)

# Execute Button
executeButton = Button(root, text="Execute", font=generalFont, relief=RAISED)
executeButton.place(x=259, y=430)

# Result Text Field
resultTextLabel = Label(root, text="Result Text : ", font=generalFont, anchor='w')
resultTextLabel.place(x=30, y=465)
resultText = Text(root, height=8, width=67)
resultText.place(x=30, y=490)

# Reset Button
resetButton = Button(root, text="Reset", font=generalFont, relief=RAISED)
resetButton.place(x=265, y=630)

# Credit Label
creditFont = ("Verdana", 8, "bold")
creditLabel = Label(root, text="Developed by : Swaraj Pande", font=creditFont, anchor='e')
creditLabel.place(x=400, y=680)

root.mainloop()
