import os
from art import logo

# Clear the console
def cls():
  os.system('cls' if os.name=='nt' else 'clear')

# Print welcome message
print(logo)
print("Welcome to the secret aution program")

bidders = {}

# Add Bidders
def add_bidder():
  name = input("What is your name? ")
  bid = float(input("What is your bid? $"))
  bidders[name] = bid

  other_bidder = input("Are there any other bidders? Type 'yes' or 'no' \n")

  if other_bidder == "yes":
    cls()
    add_bidder()

add_bidder()

# Find the winner

def find_winner(bidding_record):
  highest_bid = 0
  winner = ""

  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
 
  print(f"The winner is {winner} with a bid of {bidding_record[winner]}")

find_winner(bidders)
