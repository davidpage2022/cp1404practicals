"""Check that passwords are long enough, then display them as stars (e.g. *********). """
MINIMUM_LENGTH = 8


def main():
    """Validate user input, then print as stars."""
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be at least {MINIMUM_LENGTH} characters long")
        password = input("Enter password: ")
    print("*" * len(password))


main()
