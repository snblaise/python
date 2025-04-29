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

rps_choices = [rock, paper, scissors]

user_choices = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if user_choices >= 0 and user_choices <= 2:
    print(rps_choices[user_choices])

computer_choice = random.randint(0,2)
print("Computer Choose:")
print(rps_choices[computer_choice])

if user_choices <0 or user_choices >= 3:
    print("You Entered and Invalid Number! You Loose")

elif user_choices == computer_choice:
    print("It was a Draw")
elif user_choices == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_choices == 2:
    print("You Loose!")
elif computer_choice > user_choices:
    print("You Loose!")
elif user_choices > computer_choice:
    print("You Win!")

