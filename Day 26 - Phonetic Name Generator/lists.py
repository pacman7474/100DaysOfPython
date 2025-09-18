numbers = [1,2,3]

#new_list = []
#for n in list:
#    add_1 = n + 1
#    new_list.append(add_1)

new_list = [n+1 for n in numbers]

#create list of characters from a string
name = "Phillip"
new_name = [letter for letter in name]


#double the number in a range of 1 to 5
double_list = [number * 2 for number in range(1,5)]

#Only add names 4 characters or shorter
names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
short_names = [name for name in names if len(name) <=4 ]

#change names to uppercase for names 5 characters or more
long_uppercase_names = [name.upper() for name in names if len(name) >= 5]

with open("file1.txt") as file1:
    #file1_nums = file1.readlines()
    file1_nums = []
    for line in file1:
        file1_nums.append(int(line.strip()))
with open("file2.txt") as file2:
    #file2_nums = file2.readlines()
    file2_nums = []
    for line in file2:
        file2_nums.append(int(line.strip()))
result = [num for num in file1_nums if num in file2_nums]
#result = [int(num) for num in file1_nums if num in file2_nums]
print(result)