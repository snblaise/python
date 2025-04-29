import random
import string_utils

from traceback import print_tb

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Easy Level
#
# password = ""
# for char in range(1, nr_letters + 1): # can also be written as: for char in range(0, nr_letter):
#     password += random.choice(letters)
#
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
#
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# print(f"You Password: {password} ")
# # newpassword = ''.join(random.sample(password, len(password)))
#
# print(string_utils.shuffle(password))
#
# # Hard level Part 1
#
# password = ""
# for char in range(1, nr_letters + 1): # can also be written as: for char in range(0, nr_letter):
#     password += random.choice(letters)
#
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
#
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# print(string_utils.shuffle(password))

# Hard level Part 2

password_list = []
for char in range(1, nr_letters + 1): # can also be written as: for char in range(0, nr_letter):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your Password: {password}")
