# Day 3 Project - Treasure Island

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.")

choice_one = input("You see two separate paths in front of you. Do you want to go left or right? (Type L or R)\n-> ").upper()

if choice_one == "R":
    print("You run into a snake, get bitten and sadly pass away. Game over.")
elif choice_one == "L":
    choice_two = input("You arrive at a lake with an island in the middle. Do you want to walk around it or try to swim across? (Type W or S)\n-> ").upper()
    if choice_two == "S":
        print("You get attacked by a shark and tragically pass away. Game over.")
    elif choice_two == "W":
        choice_three = input("You find some logs and make a raft to cross the lake. You arrive at the island and find a house with 3 doors: one red, one yellow, and one blue. Which one do you want to open? (Type R, Y or B)\n-> ").upper()
        if choice_three == "R":
            print("As you enter the room, you fall into a pit and sadly pass away. Game over.")
        elif choice_three == "B":
            print("You enter a room full of booby traps and get shot with a hundred arrows. Game over.")
        elif choice_three == "Y":
            print("Congratulations, you found the treasure! You win!")
        else:
            print("Please try again and enter a valid option (R, Y or B).")
    else: 
        print("Please try again and enter a valid option (W or S).")
else: 
    print("Please try again and enter a valid option (L or R).")
