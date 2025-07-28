#def greet(name):
#    print("Welcome to the Greeting!")
#    print(f"{name}, How are you today?")
#    print("It's such a nice day today.")

#greet(input("What is your name?> "))

#def greet_with(name,location):
#    print(f"Hi {name}")
#    print(f"What is it like in {location}?")

#greet_with(name="Phillip",location="Sunnyvale")
#greet_with(location="Cupertino",name="John")

import string


def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for char in original_text:
        if char in string.ascii_letters:
            char_index = string.ascii_letters.index(char)
            shifted_index = char_index + shift_amount
            shifted_index %= len(string.ascii_letters)
            encrypted_text += string.ascii_letters[shifted_index]
        else:
            encrypted_text += char
    print(encrypted_text)

def decrypt(encrypted_text, shift_amount):
    decrypted_text = ""
    for char in encrypted_text:
        if char in string.ascii_letters:
            char_index = string.ascii_letters.index(char)
            shifted_index = char_index - shift_amount
            shifted_index %= len(string.ascii_letters)
            decrypted_text += string.ascii_letters[shifted_index]
        else:
            decrypted_text += char

def casesar(text,shift_amount,direction):
    if direction == "decode":
        shift_amount = -shift_amount
    coded_text = ""
    for char in text:
        if char in string.ascii_letters:
            char_index = string.ascii_letters.index(char)
            shifted_index = char_index + shift_amount
            shifted_index %= len(string.ascii_letters)
            coded_text += string.ascii_letters[shifted_index]
        else:
            coded_text += char
    print(coded_text)

my_continue = True
while my_continue == True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift amount:\n"))
    casesar(text,shift,direction)
    cont = input("Would you like to continue?> Y or N").upper()
    if cont == "N":
        my_continue = False


#if direction == "encode":
#    encrypt(text,shift)
#elif direction == "decode":
#    decrypt(text,shift)
