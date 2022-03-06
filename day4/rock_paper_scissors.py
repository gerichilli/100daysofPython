import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]
your_choice = choices[int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n'))]
print(your_choice)
computer_choice = random.choice(choices)
print('Computer chose', computer_choice)

if your_choice == computer_choice:
    print('Drawn')

if (your_choice == rock and computer_choice == paper) or (your_choice == paper and computer_choice == scissors) or (your_choice == scissors and computer_choice == rock):
    print('You lose')

if (your_choice == rock and computer_choice == scissors) or (your_choice == paper and computer_choice == rock) or (your_choice == scissors and computer_choice == paper):
    print('You win')
