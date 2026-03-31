"""write a python program that calculates the area and circumference of a circle given its radius."""

"""The program should:
    Prompt the user to enter the radius of the circle as an integer
    Use the math module to calculate the area and circumference
    Display the area and circumference of the circle to the user using F-Strings."""


"""To calculate the area of a circle given its radius, the formula used is,
 Area is equal to Pi times radius to the power of two. """

import math

get_radius = int(input("Please enter the radius of the circle: "))


area = ( math.pi * (get_radius ** 2 ))
circumference =( 2 * math.pi * get_radius )

print(f"The area of the circle is: {area}.")
print(f"The circumference of the circle is: {circumference}.")