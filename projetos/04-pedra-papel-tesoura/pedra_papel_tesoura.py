# Day 4 Project - Rock-paper-scissors

import random, os

os.system('cls' if os.name == 'nt' else 'clear')

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
---'   ____)______
          ________)
          _________)
         _________)
---.____________)
'''

scissors = '''
    _______
---'   ____)______
          ________)
       ____________)
      (_____)
---.__(____)
'''

game_images = [rock, paper, scissors]

# Taking in user input

user_input = input("What do you choose? Rock, paper, or scissors? (Type R, P, or S)\n-> ").upper()

# Converting user input to integers, and printing the matching ASCII art

if user_input == "R":
    user_choice = 0
elif user_input == "P":
    user_choice = 1
elif user_input == "S":
    user_choice = 2
else:
    print("Please type in a valid option (R, P or S).")
    
print(game_images[user_choice])
    
# Getting the CPU's "choice" and printing the matching ASCII art
    
cpu_choice = random.randint(0, 2)

print("The computer chooses:",)
print(game_images[cpu_choice])

# Deciding who won and who lost, and announcing the result

if user_choice == cpu_choice:
    print("It's a draw!")
elif (user_choice == 0 and cpu_choice == 1) or (user_choice == 1 and cpu_choice == 2) or (user_choice == 2 and cpu_choice == 0):
    print("You lose.")
elif (user_choice == 0 and cpu_choice == 2) or (user_choice == 1 and cpu_choice == 0) or (user_choice == 2 and cpu_choice == 1):
    print("You win!")
else:
    print("An error has occurred. Please try again.")
