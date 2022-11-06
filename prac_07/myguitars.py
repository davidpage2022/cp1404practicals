"""Guitars exercise"""

import csv
from collections import namedtuple
from prac_06.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read guitars from a file and display them."""
    guitars = load_guitars(FILENAME)
    for guitar in guitars:
        print(guitar)


def load_guitars(filename):
    """Read guitar data from a file and return a list of Guitars"""
    guitars = []
    GuitarRow = namedtuple("GuitarRow", "name, year, cost")
    with open(filename, "r") as in_file:
        for guitar in map(GuitarRow._make, csv.reader(in_file)):
            guitars.append(Guitar(guitar.name, int(guitar.year), float(guitar.cost)))
    return guitars


if __name__ == '__main__':
    main()
