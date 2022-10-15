"""Generate lottery "quick picks" based on user input."""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    """Ask user how many "Quick picks" they wish to generate then output the generated picks."""
    number_of_picks = int(input("How many quick picks? "))

    lines = []
    for i in range(number_of_picks):
        picks = [random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(NUMBERS_PER_PICK)]
        lines.append(picks)

    print(lines)


main()
