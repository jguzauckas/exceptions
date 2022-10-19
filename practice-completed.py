# Ask the user to enter a number to be squared.
# As a precaution, handle any exceptions that might occur
# when we ask the user to enter something (what if they enter
# something they aren't supposed to?)
# Finally, print out their number squared, if applicable
from typing import Type


try:
    inp = int(input("Enter a number to square: "))
except ValueError as ve:
    print(ve)
else:
    print(f"Your new number is {inp ** 2}")


# Create a dictionary with you and four of your friends as keys,
# and their hair colors as values
hair = {
    "Guzauckas": "Brown",
    "Pointek": "Black",
    "Semenuk": "Blonde",
    "Harrison": "Brown",
}

# Ask the user to enter a name to find out the hair color from the dict
# As a precaution, handle any exceptions that might occur when
# we try to access a key of a dictionary
# Finally, print out the corresponding hair color if applicable
name = input("Enter a name to check hair color: ")
try:
    color = hair[name]
except KeyError as ke:
    print(ke)
else:
    print(f"The hair color of {name} is {color}")

# Create a function that will take in two inputs: a float and an integer
# This function will raise the numbers to each other 3 times:
# i.e., float ** integer ** float ** integer ** float ** integer
# Handle any exceptions that could occur when this function is called.
# This could be due to numbers too large or the wrong type!
def bigexponent(a: float, b: int) -> float:
    try:
        num = a**b**a**b**a**b
    except OverflowError as ofe:
        print(ofe)
    except TypeError as te:
        print(te)
    else:
        return num


# Test your function by calling values that should cause an exception and
# values that should not.
print(bigexponent("a", 2))
print(bigexponent(2.5, 5))
print(bigexponent(2.0, 1.5))

# Create a division function that takes in two inputs and is prepared
# to handle exceptions based around division.
def division(a: float, b: float) -> float:
    try:
        num = a / b
    except ZeroDivisionError as zde:
        print(zde)
    except TypeError as te:
        print(te)
    else:
        return num


# Test your function by calling values that should cause an exception and
# values that should not.
print(division(2, 0))
print(division("a", "b"))
print(division(2, 1))
