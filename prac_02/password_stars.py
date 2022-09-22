"""Check that passwords are long enough, then display them as stars (e.g. *********). """
MINIMUM_LENGTH = 8


def main():
    """Validate user input, then print as stars."""
    password = get_password()
    display_password(password)


def display_password(password):
    """Displays the given password using stars (e.g. *******)."""
    print("*" * len(password))


def get_password():
    """Repeatedly asks the user for a password until a valid one is provided. Returns the password."""
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be at least {MINIMUM_LENGTH} characters long")
        password = input("Enter password: ")
    return password


main()
