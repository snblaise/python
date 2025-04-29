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

direction = input("Pick a direction: Right or Left: ")

if direction.lower() == "right":
    print("Fall into hole.\n")
    print("Game Over.")
elif direction.lower() == "left":
    print("You are one step closer to the your treasure.\n")
    next_direction = input("What will you do next: SWIM or WAIT: ")

    if next_direction.lower() == "swim" or next_direction.lower() != "wait":
        print("Ops, Attacked by Trout.\nGame Over")
        print("")
    elif next_direction.lower() == "wait":
        print("Keep Going. You are one step away from your Treasure\n")
        final_round = input("Select the Right Door to your Treasure: RED, BLUE, or YELLOW: ")

        if final_round.lower() == "red":
            print("OH No!. Burned by fire.\nGame Over.")
            print("")
        elif final_round.lower() == "blue":
            print("OH No!. Eaten by Beats.\n Game Over.")
            print("")
        elif final_round.lower() == "yellow":
            print("Hurray!! You found your Treasure.\n Good Job")
            print("")
    else:
        print("Game Over")
else:
    print("Game Over")









