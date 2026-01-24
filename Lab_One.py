print("This is Lab One, Part Two, Problem One, Python Coding Exercises;")
import math
radius = 5
area = math.pi * radius**2
volume = (4 / 3) * math.pi * radius**3
a_side = 3
b_side = 4
c_side_sq = a_side**2 + b_side**2
pythagorean_theorem = math.sqrt(c_side_sq)
print("The area of the circle with the radius of five is:", area)
print("The volume of the sphere with radius of three is:", volume)
print("The hypotenuse of a right angled triangle with the sides of 3 and four is:", pythagorean_theorem)

print("This is Problem Two, String Manipulation;")

first_name = "David"
last_name = "Martinez Toribio"
full_name = first_name + " " + last_name
name_len = len(full_name)
print("The number of characters in my full name are:",name_len)
print ("MY FULL NAME CONVERTED TO UPPERCASE IS:", full_name.upper())
print ("my full name converted to lowercase is:", full_name.lower())

print("This is Problem Three, Variable and Data Types;")

age = 26
height = 69
weight = 290.0
print ("The data type of each variable are:", type(age), type(height), type(weight))

BMI = (weight / height**2) * 703
print ("My Body Mass Index is:", BMI)

print("End of Lab One.")
