import random
import my_module

# random_integer = random.randint(1, 10)
# print(my_module.my_favourite_number)

# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1,10)
# print(random_float)

random_tails_or_heads = random.randint(0, 1)
if random_tails_or_heads == 0:
    print("Heads")
else:
    print("Tails")