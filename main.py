#   Author : Swaraj Pande
#
#   C&V Encryption System (Caesar and Vigenère Cipher)
#
#   Date : 20 May 2020


from ciphers import *
from tkinter import *
from tkinter import messagebox


# Execute Button Function
def executeButtonFunction():
    inputText = enterText.get("1.0", "end")
    inputKey = enterKey.get("1.0", "end")
    resultText.delete("1.0", "end")

    try:
        # Caesar Cipher Call
        if cipherChoice.get() == 1:
            if operationChoice.get() == 1:
                encrypted = caesarEncrypt(inputText, inputKey)
                resultText.insert("1.0", encrypted)
            elif operationChoice.get() == 2:
                decrypted = caesarEncrypt(inputText, 26 - int(inputKey))
                resultText.insert("1.0", decrypted)
        # Vigenere Cipher Call
        elif cipherChoice.get() == 2:
            if operationChoice.get() == 1:
                encrypted = vigenereEncrypt(inputText, inputKey)
                resultText.insert("1.0", encrypted)
            elif operationChoice.get() == 2:
                decrypted = vigenereDecrypt(inputText, inputKey)
                resultText.insert("1.0", decrypted)

    # Invalid Key
    except:
        messagebox.showerror("Error", "Invalid Key")
        enterKey.delete("1.0", "end")


# Reset Button Function
def resetButtonFunction():
    cipherChoice.set("1")
    operationChoice.set("1")
    enterText.delete("1.0", "end")
    enterKey.delete("1.0", "end")
    resultText.delete("1.0", "end")


# Execute Button Hover effect Functions
def executeEnterHover(event):
    executeButton['background'] = 'green'


def executeLeaveHover(event):
    executeButton['background'] = 'SystemButtonFace'


# Reset Button Hover effect Functions
def resetEnterHover(event):
    resetButton['background'] = 'red'


def resetLeaveHover(event):
    resetButton['background'] = 'SystemButtonFace'


# Creating the Window
root = Tk()
root.title("C&V Encryption System")
root.geometry("600x750")
root.resizable(False, False)

# Setting the Icon
root.iconbitmap('img/icon.ico')

# Heading Label
headingFont = ("Verdana", 20, "bold")
headingLabel = Label(root, text="C&V Encryption System", font=headingFont)
headingLabel.pack(side=TOP)

# General Font
generalFont = ("Times", 12)

# Button Font
buttonFont = ("Times", 12, "bold")

# Cipher Choice
cipherChoice = IntVar()
cipherChoice.set("1")
cipherChoiceLabel = Label(
    root,
    text="Choose Cipher : ",
    font=generalFont,
    anchor='w'
)
cipherChoiceLabel.place(x=170, y=50)
caesarCipherRadiobutton = Radiobutton(
    root,
    text="Caesar Cipher",
    font=generalFont,
    variable=cipherChoice,
    value=1
)
caesarCipherRadiobutton.place(x=290, y=49)
vigenereCipherRadiobutton = Radiobutton(
    root,
    text="Vigenere Cipher",
    font=generalFont,
    variable=cipherChoice,
    value=2
)
vigenereCipherRadiobutton.place(x=290, y=74)


# Operation Choice
operationChoice = IntVar()
operationChoice.set("1")
operationChoiceLabel = Label(
    root,
    text="Choose Operation : ",
    font=generalFont,
    anchor='w'
)
operationChoiceLabel.place(x=151, y=119)
encryptionRadiobutton = Radiobutton(
    root,
    text="Encryption",
    font=generalFont,
    variable=operationChoice,
    value=1
)
encryptionRadiobutton.place(x=290, y=118)
decryptionRadiobutton = Radiobutton(
    root,
    text="Decryption",
    font=generalFont,
    variable=operationChoice,
    value=2
)
decryptionRadiobutton.place(x=290, y=143)


# Enter Text Field
enterTextLabel = Label(
    root,
    text="Enter Text : ",
    font=generalFont,
    anchor='w'
)
enterTextLabel.place(x=30, y=200)
enterText = Text(root, height=8, width=67)
enterText.place(x=30, y=225)


# Enter Key Field
enterKeyLabel = Label(
    root,
    text="Enter Key : ",
    font=generalFont,
    anchor='w'
)
enterKeyLabel.place(x=30, y=425)
enterKey = Text(root, height=1, width=67)
enterKey.place(x=30, y=450)


# Key Instructions Labels
instructionFont = ("Times", 12, "bold")
caesarInstructionLabel = Label(
    root,
    text="Note : Caesar Numeric Key = Integer",
    font=instructionFont,
    anchor='w'
)
caesarInstructionLabel.place(x=30, y=365)
vigenereInstructionLabel = Label(
    root,
    text="Vigenere Text Key = String",
    font=instructionFont,
    anchor='w'
)
vigenereInstructionLabel.place(x=76, y=389)


# Execute Button
executeButton = Button(
    root,
    text="Execute",
    font=buttonFont,
    height=2,
    width=10,
    borderwidth=3,
    relief=RAISED,
    command=executeButtonFunction
    )
executeButton.place(x=239, y=480)
executeButton.bind("<Enter>", executeEnterHover)
executeButton.bind("<Leave>", executeLeaveHover)


# Result Text Field
resultTextLabel = Label(
    root,
    text="Result Text : ",
    font=generalFont,
    anchor='w'
)
resultTextLabel.place(x=30, y=515)
resultText = Text(root, height=8, width=67)
resultText.place(x=30, y=540)


# Reset Button
resetButton = Button(
    root,
    text="Reset",
    font=buttonFont,
    height=2,
    width=10,
    borderwidth=3,
    relief=RAISED,
    command=resetButtonFunction
    )
resetButton.place(x=240, y=680)
resetButton.bind("<Enter>", resetEnterHover)
resetButton.bind("<Leave>", resetLeaveHover)


# Credit Label
creditFont = ("Verdana", 8, "bold")
creditLabel = Label(
    root,
    text="Developed by : Swaraj Pande",
    font=creditFont,
    anchor='e'
)
creditLabel.place(x=400, y=730)

root.mainloop()