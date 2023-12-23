"""Random name generator who pays for everyone"""
import random

names = input("Enter comma seperated names: ")
names = names.split(', ')
random_num = random.randint(0, len(names)-1)
print(f"{names[random_num]} is going to buy the meal today!")
