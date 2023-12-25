"""Pizza order delivery"""

print("Thank you for choosing Python Pizza Deliveries!")
size = input('Enter size of the Pizza, L: Large, M: Medium, S:Small\n')
add_pepperoni = input('Do you want pepperoni? Enter Y or N\n')
extra_cheese = input('Do you want extra cheese? Enter Y or N\n')

bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
elif size == 'L':
    bill += 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(f"Please pay the bill ${bill}")
