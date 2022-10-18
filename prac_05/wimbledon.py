"""
Wimbledon
Estimate:  55 minutes
Actual:
"""

import csv

FILENAME = "wimbledon.csv"


def main():
    """Display information about Wimbledon gentlemen's singles champions."""

    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip header.
        csv_reader = csv.reader(in_file)

        rows = []
        for row in csv_reader:
            rows.append(row)
        print(rows)

    pass


main()
