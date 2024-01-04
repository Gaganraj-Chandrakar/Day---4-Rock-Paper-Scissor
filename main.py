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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor: "))

list=["rock", "paper", "scissor"]
if user_input >= 0 and user_input<=2:
  print(f"You chose:\n{globals()[list[user_input]]}")    # global()[list[index]] changes the list item to variable of same name

  random_choice = random.randint(0,2)
  
  print(f"Computer chose:\n{globals()[list[random_choice]]}")
  
  if user_input == 0 and random_choice ==2:
    print("You won")
  elif user_input == 2 and random_choice ==0:
    print("You lose")
  elif user_input > random_choice:
    print("You won")
  elif user_input < random_choice:
    print("You lose")
  elif user_input == random_choice:
    print("Draw")
else:
  print("Enter a valid number.")


#Method 2

# You can make a list for game images instead of list of strings