#   Author: Swaraj Pande
#
#   File Name : ciphers
#
#   Date: 20 May 2020


# Function to Caesar Encrypt a String
# The Same function can be used to Decrypt a Caesar Cipher using key = 26 - key
def caesarEncrypt(text, key):
    encrypted = ""
    key = int(key)
    # Traversing text
    for i in range(len(text)):
        currChar = text[i]

        # Encrypting Uppercase Characters
        if currChar.isupper():
            encrypted = encrypted + chr((ord(currChar) + key - 65) % 26 + 65)

        # Encrypting Lowercase Characters
        elif currChar.islower():
            encrypted = encrypted + chr((ord(currChar) + key - 97) % 26 + 97)

        # Other characters are not encrypted
        else:
            encrypted = encrypted + currChar

    return encrypted


# Functions to Vigenere Encrypt a String
# Generating the Vigenere Key
def generateVigenereKey(text, key):

    vigenereKey = ""
    textLength = len(text)
    keyLength = len(key)
    i = 0
    j = 0
    # Adding the required characters to make the length of text and key equal
    while i < textLength:
        if j == keyLength:
            j = 0

        # The characters are made uppercase
        vigenereKey = vigenereKey + key[j].upper()
        i = i + 1
        j = j + 1

    return vigenereKey


def vigenereEncrypt(text, key):
    # Generating the Vigenere Key
    vigenereKey = generateVigenereKey(text, key)
    encrypted = ""

    # Traversing text
    for i in range(len(text)):
        currChar = text[i]
        currKeyChar = vigenereKey[i]

        # Encrypting Uppercase Characters
        if currChar.isupper():
            encrypted = encrypted + chr((ord(currChar) + ord(currKeyChar)) % 26 + 65)

        # Encrytping Lowercase Characters
        elif currChar.islower():
            currChar = currChar.upper()
            upperChar = chr((ord(currChar) + ord(currKeyChar)) % 26 + 65)
            encrypted = encrypted + upperChar.lower()

        # Other Characters are not Encrypted
        else:
            encrypted = encrypted + currChar

    return encrypted


def vigenereDecrypt(encrypted, key):
    # Generating the Vigenere Key
    vigenereKey = generateVigenereKey(encrypted, key)
    text = ""

    # Traversing encrypted
    for i in range(len(encrypted)):
        currChar = encrypted[i]
        currKeyChar = vigenereKey[i]

        # Decrypting Uppercase Characters
        if currChar.isupper():
            text = text + chr((ord(currChar) - ord(currKeyChar) + 26) % 26 + 65)
        
        # Decrypting Lowercase Characters
        elif currChar.islower():
            currChar = currChar.upper()
            upperChar = chr((ord(currChar) - ord(currKeyChar) + 26) % 26 + 65)
            text = text + upperChar.lower()

        # Other Characters are not Decrypted
        else:
            text = text + currChar

    return text

def columnarEncrypt(text, key, padding="Spaces"):


    # Remove Spaces from text. 
    text = text.replace(" ", "")

    # Pad text if columns are not filled by either using spaces at the end or by adding random characters.
    while (len(text) % len(key) != 0):

        if padding == "Spaces":
            text += " "
        elif padding == "Random":
            text += random.choice(string.ascii_letters)
        else:
            raise Exception("Padding setting is not valid.")

    rowLen = len(key)
    colLen = len(text) // len(key)

    # Split text into sections of same size as key
    textSplit = ([text[i:i + rowLen] for i in range(0, len(text), rowLen)])

    # Get the positions of characters according to key
    order = [sorted(key).index(c) for c in key]
    charPos = [order.index(i) for i in range(len(order))]

    ciphertext = ""

    # Add characters to the ciphertext
    for x in charPos:

        for i in range(colLen):

            ciphertext += textSplit[i][x]

        ciphertext += " "

    return ciphertext

def columnarDecrypt(ciphertext, key):

    rowLen = len(key)
    colLen = len(ciphertext) // len(key)

    # Split text into sections of same size as key
    textSplit = ([ciphertext[i:i + rowLen] for i in range(0, len(ciphertext), rowLen)])

    # Rearrange columns into original positions
    order = [sorted(key).index(c) for c in key]
    reformedColumns = [textSplit[i] for i in order]

    text = ""

    # Add characters to the text
    for i in range(colLen):

        for j in range(rowLen):

            text += reformedColumns[j][i]

    return text