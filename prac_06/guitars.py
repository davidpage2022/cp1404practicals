"""Guitar exercise - Program using Guitar class
Time expected: 30 min
       actual:  min
"""
from prac_06.guitar import Guitar


def main():
    """Ask user for guitar data and then present information
    in a nicely formatted table."""
    guitars = []

    print("My guitars!")
    name = input("Name: ").strip()
    while name != "":
        year = get_positive_integer("Year: ")
        cost = get_positive_float("Cost: $")

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")

        name = input("Name: ").strip()


def get_positive_integer(prompt):
    """Get a positive integer from the user with prompt message.
    Continues to ask until valid input is given."""
    while True:
        try:
            integer = int(input(prompt))
            if integer >= 0:
                return integer
            else:
                print("Must be a positive number")
        except ValueError:
            print("Must be a valid integer")


def get_positive_float(prompt):
    """Get a positive floating-point number from the user with prompt message.
    Continues to ask until valid input is given."""
    while True:
        try:
            number = float(input(prompt).replace(",", ""))
            if number >= 0:
                return number
            else:
                print("Must be a positive number")
        except ValueError:
            print("Must be a valid decimal number")


if __name__ == '__main__':
    main()
