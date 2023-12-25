"""
    Fizz Buzz Game
    From numbers 1 to 100
    if the number is divisible by 3 print Fizz
    if the number is divisible by 5 print Buzz
    if the number is divisible by both 3 and 5 print FizzBuzz
    in all other cases print number.
"""

print("Let's start!")

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
