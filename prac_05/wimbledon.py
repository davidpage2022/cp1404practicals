"""
Wimbledon
Estimate:  55 minutes
Actual:    41 minutes
"""

import csv

FILENAME = "wimbledon.csv"
COUNTRY_COLUMN = 1
CHAMPION_COLUMN = 2


def main():
    """Display information about Wimbledon gentlemen's singles champions."""
    data = load_data(FILENAME)
    display_champions_info(data)
    print()
    display_country_info(data)


def load_data(filename):
    """
    Load data from a .csv file with filename provided.
    Returns a list of rows, each containing a list of columns.
    """
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip header.
        csv_reader = csv.reader(in_file)
        for row in csv_reader:
            data.append(row)
    return data


def display_champions_info(data):
    """Displays information about Wimbledon champions."""
    champion_to_wins = {}
    for row in data:
        champion = row[CHAMPION_COLUMN]
        try:
            champion_to_wins[champion] += 1
        except KeyError:
            champion_to_wins[champion] = 1

    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion} {wins}")


def display_country_info(data):
    """Display information about countries that have won wimbledon."""
    countries = set(row[COUNTRY_COLUMN] for row in data)
    countries = sorted(list(countries))

    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(countries))


main()
