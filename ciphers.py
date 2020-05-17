#   Author: Swaraj Pande
#
#   File Name : ciphers
#
#   Date:


# Function to Caesar Encrypt a String
# The Same function can be used to Decrypt a Caesar Cipher using key = 26 - key
def caesarEncrypt(text, key):
    encrypted = ""

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
