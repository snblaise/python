print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print(f"Please pay {bill} .")
    elif age <= 18:
        bill = 7
        print(f"Please pay {bill}.")
    else:
        bill = 12
        print(f"Please pay {bill}.")

    want_photo = input("Do you want a photo? Enter Y or N: ")
    if want_photo == "y":
        bill += 3
    print(f"You final Bill is {bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
