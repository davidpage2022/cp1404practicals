"""Program that prompts the user for 5 numbers and then displays information about them."""


def main():
    """Prompt the user for 5 numbers and then displays information about them."""
    numbers = get_numbers()
    print_number_info(numbers)


def get_numbers():
    """Get 5 numbers from the user, returned as a list."""
    numbers = []
    for i in range(5):
        number = int(input("Number: "))  # TODO: Support float input.
        numbers.append(number)
    return numbers


def print_number_info(numbers):
    """Print information about a list of numbers"""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {(sum(numbers) / len(numbers))}")


main()
