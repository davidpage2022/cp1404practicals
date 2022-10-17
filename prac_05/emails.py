"""
Emails
Estimate:  38 minutes
Actual:
"""


def main():
    """Get user name and emails, attempting to extract name from email automatically"""
    email_to_names = {}
    email = input("Email: ")
    while email != "":

        # Attempt to extract name from email, otherwise ask user for name.
        name = extract_name(email)
        choice = input(f"Is your name {name}? (Y/n)").upper()
        if choice != "Y":
            name = input("Name: ")

        email_to_names[email] = name
        email = input("Email: ")

    # Display name and emails entered.
    for email, name in email_to_names.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Attempt to extract a name from an email (e.g. john.doe@gmail.com returns "John Doe")"""
    return "John Doe"


main()
