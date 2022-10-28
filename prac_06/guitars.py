"""Guitar exercise - Program using Guitar class
Time expected: 30 min
       actual: 40 min
"""
from prac_06.guitar import Guitar


def main():
    """Ask user for guitar data and then present information
    in a nicely formatted table."""
    guitars = []
    # guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40),
    #            Guitar("Line 6 JTV-59", 2010, 1512.90),
    #            Guitar("Fender Stratocaster", 2014, 765.40)]

    print("My guitars!")
    name = input("Name: ").strip()
    while name != "":
        year = get_positive_integer("Year: ")
        cost = get_positive_float("Cost: $")

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")

        name = input("Name: ").strip()

    print()
    print("... snip ...")
    print()
    print("These are my guitars:")
    display_guitars(guitars)


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


def display_guitars(guitars):
    """ Displays information about a list of Guitars, nicely formatted. """
    max_length = max(len(guitar.name) for guitar in guitars)
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}:  "
              f"{guitar.name:>{max_length}} ({guitar.year}),"
              f" worth ${guitar.cost:10,.2f}{vintage_string}")


if __name__ == '__main__':
    main()
