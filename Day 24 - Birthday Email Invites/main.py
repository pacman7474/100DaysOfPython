#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt

with open("Input/Names/invited_names.txt") as file:
    for line in file:
        process = line.strip()
        with open ("Input/Letters/starting_letter.txt") as letter:
            starting_letter = letter.read()
            updated_letter = starting_letter.replace("[name]",process)
            with open ("Output/ReadyToSend/" + process + "_letter.txt","w") as output_file:
                output_file.write(updated_letter)




#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp