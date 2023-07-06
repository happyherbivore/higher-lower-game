from game_data import data
from art import logo
from art import vs
from random import randint
from os import system

# options are name, followers, description, country
def clear():
   system('clear')

def more_followers():
  if data[item_A]['followers'] > data[item_B]['followers']:
    return "a"
  else:
    return "b"
print(f"{logo}\n")

playing = True
  # Defining variables and introduce game
score = 0
item_A = randint(0 , len(data) -1)
item_B = randint(0 , len(data) -1)
while playing:
  
  # ensuring both values are always different
  if item_A == item_B:
    item_B = randint(0 , len(data) -1)
  
  print(f" Compare A: {data[item_A]['name']}, a {data[item_A]['description']} from {data[item_A]['country']}.\n")
  print(f"{vs}\n") 
  print(f"Against B: {data[item_B]['name']}, a {data[item_B]['description']} from {data[item_B]['country']}.")
  guess = input("Who has more followers, A or B: ").lower()
  clear()
  print(f"{logo}\n")
  if more_followers() == guess and guess == "a":
    score += 1
    print(f"You're right! Current score: {score}.")
    item_B = randint(0 , len(data) -1)
  elif more_followers() == guess and guess == "b":
    score += 1
    print(f"You're right! Current score: {score}.")
    item_A = item_B
    item_B = randint(0 , len(data) -1)
  else:
    print(f"Incorrect. Final score was {score}.")
    playing = False
