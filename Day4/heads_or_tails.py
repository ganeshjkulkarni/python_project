import random

print("Welcome to the toss")
input("Hit enter to flip the coin")
rand_int = random.randint(0, 1)
if rand_int == 1:
    print("Heads")
else:
    print("Tails")
