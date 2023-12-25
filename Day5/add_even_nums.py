"""Add Even numbers"""

number = int(input("Enter the max num : "))

even_sum = 0

for even_num in range(0, number+1, 2):
    even_sum += even_num

print(f"Even numbers sum {even_sum}")
