#Step 3
from dis import dis
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []

for letter in chosen_word:
    display.append("_")

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position, letter in enumerate(chosen_word):
        if letter == guess:
            display[position] = letter
    
    print(display)
    
    #Check end of game
    if "_" not in display:
        end_of_game = True
        print("You win")

   