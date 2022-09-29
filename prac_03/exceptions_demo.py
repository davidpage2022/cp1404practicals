"""
CP1404/CP5632 - Practical
Answer the following questions:

1. When will a ValueError occur?
When either numerator or denominator are not an integer.

2. When will a ZeroDivisionError occur?
When denominator is zero, "numerator / denominator" will raise a ZeroDivisionError exception.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
We could check if denominator is zero and handle the special case, that the result is "undefined".
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator != 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        print("Undefined")
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
