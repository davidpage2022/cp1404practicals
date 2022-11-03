"""Guitar exercise - Tests for Guitar class
Time expected: 10 min
       actual: 8 min
"""
from prac_06.guitar import Guitar


def main():
    """Tests for Guitar class."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 3200.20)

    print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age()}")
    print(f"{another.name} get_age() - Expected 9. Got {another.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")


if __name__ == '__main__':
    main()
