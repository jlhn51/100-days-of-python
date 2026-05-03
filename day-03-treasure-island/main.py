"""
Day 3: Treasure Island
A choose-your-own adventure game where the playere navigates choices to find the treasure.
Concepts: control flow, conditionals (if/elif/else), nested logic, string methods.
"""

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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Do you want to go left or right? ").lower()

if direction == "left":
    swim = input("You come across a river. Do you want to swim or wait? ").lower()
    if swim == "wait":
        door_color = input("There are three doors of different colors. 'red', 'blue' and 'yellow'. Which door do you open? ").lower()

        if door_color == "red":
            print('You are burned by fire. Game Over!')
        elif door_color == "blue":
            print("You are eaten by beasts. Game Over!")
        elif door_color == "yellow":
            print("You found the treasure. Congratulations - you win!")
        else:
            print("You picked a door that doesn't exist. Game Over!")

    else:
        print("You are attacked by trouts. Game Over!")

else:
    print("You fell into a hole. Game Over!")