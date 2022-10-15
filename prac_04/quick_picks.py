"""Generate lottery "quick picks" based on user input."""

import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6


def main():
    """Ask user how many "Quick picks" they wish to generate then output the generated picks."""
    number_of_picks = get_number_of_picks()
    lines = generate_lines(number_of_picks)
    display_lines(lines)


def get_number_of_picks():
    """Return the number "quick picks" to use, obtained from the user."""
    is_valid = False
    while not is_valid:
        try:
            number_of_picks = int(input("How many quick picks? "))
            if number_of_picks > 0:
                is_valid = True
            else:
                raise ValueError()
        except ValueError:
            print("Please enter a valid integer greater than zero")
    return number_of_picks


def generate_lines(number_of_lines):
    """Generate random lines ("quick picks")."""
    lines = []
    for i in range(number_of_lines):
        numbers = [random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(NUMBERS_PER_LINE)]
        lines.append(numbers)
    return lines


def display_lines(lines):
    """Display lines, formatted into columns."""
    for line in lines:
        print(" ".join(f"{number:2}" for number in line))


main()
