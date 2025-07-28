import random
from hangman_words import word_list
from hangmen_stages import HANGMANPICS


chosen_word = random.choice(word_list)
print(chosen_word)
my_guess = ""
for x in chosen_word:
    my_guess += "_"
max_incorrect_guesses = 6
num_guesses = 0
game_over = False

while not game_over:
    guess = input("Please guess a letter: ").lower()
    if guess not in chosen_word:
        num_guesses += 1
    if num_guesses == max_incorrect_guesses:
        game_over = True
        print("I'm, sorry you have run out of guesses")
    for x,char in enumerate(chosen_word):
        if guess == chosen_word[x]:
            my_guess = my_guess[0:x] + char + my_guess[x+1:]
    print(my_guess)
    if my_guess == chosen_word:
        print("Congratulations! You guessed the word.")
        game_over = True
    print(HANGMANPICS[num_guesses])

print(my_guess)