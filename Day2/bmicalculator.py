"""BMI Calculator"""

weight = float(input("Enter your weight in KG: "))
feet = int(input("Enter your height in Feet and inches \nFeet: "))
inches = int(input("Inches: "))

height_in_meter = (feet * 12 + inches) * 0.0254
print("BMI is", int(weight / (height_in_meter ** 2)))
