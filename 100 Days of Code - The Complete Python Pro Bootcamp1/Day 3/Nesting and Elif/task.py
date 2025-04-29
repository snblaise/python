print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height <= 120:
    if height <=12:
        print("You will pay $5")
    elif height <=15:
        print("You will pay $12")
    elif height <=22:
        print("You will pay $15")
    else:
        print("You will pay $20")

else:
    print("Sorry this rollercoaster is not save for you.")
