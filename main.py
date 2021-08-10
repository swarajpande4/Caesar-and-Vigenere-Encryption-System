#   Author : Swaraj Pande
#
#   C&V Encryption System (Caesar and Vigenère Cipher)
#
#   Date : 20 May 2020


from ciphers import *
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import os


# Execute Button Function
def executeButtonFunction():
    inputText = enterText.get("1.0", "end-1c")
    inputKey = enterKey.get("1.0", "end-1c")
    resultText.delete("1.0", "end")

    try:
        # Caesar Cipher Call
        if cipherChoice.get() == cipherOptions[0]:
            if operationChoice.get() == 1:
                encrypted = caesarEncrypt(inputText, inputKey)
                resultText.insert("1.0", encrypted)
            elif operationChoice.get() == 2:
                decrypted = caesarEncrypt(inputText, 26 - int(inputKey))
                resultText.insert("1.0", decrypted)
        # Vigenere Cipher Call
        elif cipherChoice.get() == cipherOptions[1]:
            if operationChoice.get() == 1:
                encrypted = vigenereEncrypt(inputText, inputKey)
                resultText.insert("1.0", encrypted)
            elif operationChoice.get() == 2:
                decrypted = vigenereDecrypt(inputText, inputKey)
                resultText.insert("1.0", decrypted)
        # Columnar Cipher Call
        elif cipherChoice.get() == cipherOptions[2]:
            if operationChoice.get() == 1:
                encrypted = columnarEncrypt(inputText, inputKey)
                resultText.insert("1.0", encrypted)
            elif operationChoice.get() == 2:
                decrypted = columnarDecrypt(inputText, inputKey)
                resultText.insert("1.0", encrypted)

    # Invalid Key
    except:
        messagebox.showerror("Error", "Invalid Key")
        enterKey.delete("1.0", "end")


# Reset Button Function
def resetButtonFunction():
    cipherChoice.set(cipherOptions[0])
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


# Right Click Menu Functions
def rightClickMenu(event):
    global menu
    menu = Menu(root, tearoff=0)
    menu.add_command(label="Cut")
    menu.add_command(label="Copy")
    menu.add_command(label="Paste")


def showRightClickMenu(event):
    eventWidget = event.widget
    menu.entryconfigure(
        "Cut",
        command=lambda: eventWidget.event_generate("<<Cut>>")
    )
    menu.entryconfigure(
        "Copy",
        command=lambda: eventWidget.event_generate("<<Copy>>")
    )
    menu.entryconfigure(
        "Paste",
        command=lambda: eventWidget.event_generate("<<Paste>>")
    )
    menu.tk.call("tk_popup", menu, event.x_root, event.y_root)

# Creating the Window
root = Tk()
root.title("C&V Encryption System")
root.geometry("600x750")
root.resizable(False, False)

# Calling rightClick Menu
rightClickMenu(root)

# Setting the Icon
# root.iconbitmap(os.path.abspath('img\\icon.ico'))
root.iconbitmap(".\\img\\icon.ico")

# Heading Label
headingFont = ("Verdana", 20, "bold")
headingLabel = Label(root, text="C&V Encryption System", font=headingFont)
headingLabel.pack(side=TOP)

# General Font
generalFont = ("Times", 12)

# Button Font
buttonFont = ("Times", 12, "bold")

# Cipher Choice
cipherChoice = StringVar()

cipherChoiceLabel = Label(
    root,
    text="Choose Cipher : ",
    font=generalFont,
    anchor='w'
)

cipherChoiceLabel.place(x=170, y=50)

# Drop Down Box For Selecting Ciphers
cipherOptions = ["Caesar Cipher", "Vigenere Cipher", "Columnar Cipher"]
cipherChoice.set(cipherOptions[0])
drop = OptionMenu(root, cipherChoice, *cipherOptions)
drop.config(width=20)
drop.config(height=1)
drop.place(x=290, y=50)

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
enterText = ScrolledText(root, height=8, width=67)
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
columnarInstructionLabel = Label(
    root,
    text="Columnar Text Key = String",
    font=instructionFont,
    anchor='w'
)
columnarInstructionLabel.place(x=300, y=365)


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
resultText = ScrolledText(root, height=8, width=67)
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

# Binding Right Click menu to Right button (Mouse)
root.bind_class("Text", "<Button-3><ButtonRelease-3>", showRightClickMenu)

root.mainloop()
