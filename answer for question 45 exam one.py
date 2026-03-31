"""write a python program that calculates the area of a rectangle given its length and width."""

"""The program should: Display the area of the rectangle to the user using F-Strings.
Allow the user to input floating point numbers for width and height.
Call a generalized, custom function that takes 2 parameters."""


"""to calculate the area of a rectangle given its length and width, the formula used is,
 Area = width x height """

def area_finder(get_width, get_height):
    return get_width * get_height

get_width = float(input("Please enter the width of the rectangle: "))
get_height = float(input("Enter the height of the rectangle: "))

area = area_finder(get_width, get_height)
print(f"The area of the rectangle is: {area}.")