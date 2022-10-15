"""Generate lottery "quick picks" based on user input."""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    """Ask user how many "Quick picks" they wish to generate then output the generated picks."""
    number_of_picks = int(input("How many quick picks? "))

    lines = []
    for i in range(number_of_picks):
        numbers = [random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(NUMBERS_PER_LINE)]
        lines.append(numbers)

    for line in lines:
        print(" ".join(f"{number:2}" for number in line))


main()
