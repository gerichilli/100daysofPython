#Step 4

import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list

end_of_game = False
chosen_word = random.choice(word_list)

#Update the word list to use the 'word_list' from hangman_words.py
lives = len(stages) - 1

#Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for letter in chosen_word:
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You has entered this letter: {guess}")

    #Check guessed letter
    for position, letter in enumerate(chosen_word):
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives = lives - 1
        print(f"Your guess {guess} is not in the word")
        if lives <= 0:
            end_of_game = True
            print("You lose")
           
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])