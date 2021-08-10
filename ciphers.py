#   Author: Swaraj Pande
#
#   File Name : ciphers
#
#   Date: 20 May 2020
from math import ceil

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


# Functions to Columnar Transform a String
def columnarEncrypt(text, key):

    text = text.replace(' ', '')

    rows = len(text)/len(key)
    text = text.ljust(ceil(rows) * len(key), 'X')

    text = list(text)
    box = []

    i = 0
    for row in range(ceil(rows)):
        box.append(text[i: i + len(key)])
        i += len(key)
 
    priority = [ord(val) for val in list(key)]
    boxEncrypted = []

    for r in box:
        rowTuples = []
        for c in range(len(r)):
            rowTuples.append((r[c], priority[c]))

        rowTuples.sort(key = lambda x: x[1])
        encryptedRow = [v[0] for v in rowTuples]
        boxEncrypted.append(encryptedRow)

    ciphertext = []
    for line in boxEncrypted:
        ciphertext.extend(line)
    
    return ''.join(ciphertext)


def columnarDecrypt(ciphertext, key):

    ciphertext = ciphertext.replace(' ', '')
    
    rows = len(ciphertext) / len(key)
    ciphertext = list(ciphertext)
    
    box = []
    i = 0
    for row in range(ceil(rows)):
        box.append(ciphertext[i: i + len(key)])
        i += len(key)
    
    
    keyList = list(key)  
    sortedKeyList = keyList
    sortedKeyList = sorted(keyList)

    sortedMessage = []

    for r in box:
        for k in keyList:
            sortedMessage.append(r[sortedKeyList.index(k)])

    return ''.join(sortedMessage)
