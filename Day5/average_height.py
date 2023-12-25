"""Average Height"""
student_heights = input("Enter space seperated heights of all student\n")
student_heights = student_heights.split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_height = 0
for height in student_heights:
    total_height += height

average_height = round(total_height / len(student_heights), 2)
print(f"Average Height: {average_height}")
