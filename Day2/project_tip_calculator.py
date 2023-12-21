""" Project to split the bill including tip."""

print("Welcome to the tip calculator")
bill_amount = float(input("What was the total bill? $"))
tip_perc = float(input("What percentage tip would you like to give? 10, 12 or 15? "))
number_of_people = int(input("How many people to split the bill? "))
final_amount = round((bill_amount + (bill_amount * tip_perc / 100)) / number_of_people, 2)
final_amount = "{:.2f}".format(final_amount)
print(f"Each person should pay: ${final_amount}")
