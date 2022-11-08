"""Guitars exercise"""

import csv
from collections import namedtuple
from prac_06.guitar import Guitar

# Importing from previous prac to get same error-checking behaviour.
from prac_06.guitars import get_positive_integer, get_positive_float

FILENAME = "guitars.csv"


def main():
    """Read guitars from a file and display them."""
    guitars = load_guitars(FILENAME)

    display_guitars(guitars)
    print("Please enter information for adding new guitars...")
    name = input("Name: ").strip()
    while name != "":
        year = get_positive_integer("Year: ")
        cost = get_positive_float("Cost: $")

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")

        display_guitars(guitars)
        print("Please enter information for adding new guitars...")
        name = input("Name: ").strip()

    save_guitars(guitars, FILENAME)


def load_guitars(filename):
    """Read guitar data from a file and return a list of Guitars"""
    guitars = []
    GuitarRow = namedtuple("GuitarRow", "name, year, cost")
    with open(filename, "r", newline='') as in_file:
        for guitar in map(GuitarRow._make, csv.reader(in_file)):
            guitars.append(Guitar(guitar.name, int(guitar.year), float(guitar.cost)))
    return guitars


def save_guitars(guitars, filename):
    """Save list of Guitars to a file"""
    with open(filename, "w", newline='') as out_file:
        writer = csv.writer(out_file)
        for guitar in guitars:
            # Writerow expects a list like [ "column 1", "column 2", "column 3" ].
            # To turn guitar into we do the following:
            # vars converts a Guitar to a dictionary, like:
            # { "name": "Fender", "year": 1997, "cost": 19500 }.
            # Then we get only the values and turn it into a list to get:
            # [ "Fender", 1997, 19500 ]
            writer.writerow(list(vars(guitar).values()))


def display_guitars(guitars):
    """Displays the given guitars in sorted order."""
    for guitar in sorted(guitars):
        print(guitar)


if __name__ == '__main__':
    main()
