#num = 1
#for x in range(1,101):
    #if x % 3 == 0 and x % 5==0:
        #print("FizzBuzz")
    #elif x % 3==0:
        #print("Fizz")
    #elif x % 5==0:
        #print("Buzz")
    #else:
        #print(x)
#

import random
import string
length = int(input("How long of a password would you like?> "))
numbers = int(input("Whats the maximum numbers would you like it to have?> "))
special_chars = int(input("Whats the maximum special characters would you like it to have?> "))
num_char_left = special_chars
num_numbers_left = numbers
special_chars_available = ['!','@','#','$','%','^','&']
password = ""

for x in range(0,numbers):
    password += str(random.randint(0,9))

for x in range(0,special_chars):
    password += random.choice(special_chars_available)

if length > numbers + special_chars:
    for x in range(0,length - numbers - special_chars):
        password += random.choice(string.ascii_letters)

print(password)
char_list = list(password)
random.shuffle(char_list)
password = ''.join(char_list)
print(password)
#for x in range(0,length):
    #if num_numbers_left > 0 and num_char_left > 0:
        #char_type = random.randint(1,3)
        #if char_type == 1:
            #password = password + random.choice(string.ascii_letters)
        #elif char_type == 2:
            #password = password + str(random.randint(0,9))
            #num_numbers_left -= 1
        #else:
            #password = password + random.choice(special_chars_available)
            #num_char_left -= 1
    #elif num_numbers_left > 0:
        #char_type = random.choice([1,2])
        #if char_type == 1:
            #password = password + random.choice(string.ascii_letters)
        #else:
            #password = password + str(random.randint(0, 9))
            #num_numbers_left -= 1
    #elif num_char_left > 0:
        #char_type = random.choice([1, 3])
        #if char_type == 1:
            #password = password + random.choice(string.ascii_letters)
        #else:
            #password = password + random.choice(special_chars_available)
            #num_char_left -= 1
    #else:
        #password = password + random.choice(string.ascii_letters)



print(f"Your password is : {password}")
