import random
from operator import index
from traceback import print_tb

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1st Option
# print(random.choice(friends))
#
#
# # 2nd Option
#
# print(friends[random.randint(0, 1)])

first_choice = random.choice(friends)
second_choice = random.choice(friends)
if first_choice == second_choice:
    print("We know each other too well")
else:
    print("We don't know each other too well")
