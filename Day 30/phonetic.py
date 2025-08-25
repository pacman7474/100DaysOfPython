#FileNotFound
#with open("a_file.txt") as file:
#    file.read()

#KeyError
#a_dictionary = {"key": "value"}
#value = a_dictionary["non_existant_key"]

#IndexError
#fruit_list = ["Apple","Banana","Pear"]
#fruit = fruit_list[3]

#TypeError
#text = "abc"
#print(text + 5)
#try:
#    file = open("a_file.txt")
#except:
#    file = open("a_file.txt","w")

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index,row) in data.iterrows()}
print(phonetic_dict)
invalid = True
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Please enter only letters")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()