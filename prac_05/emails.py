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
        email_to_names[email] = get_name(email)
        email = input("Email: ")
    display(email_to_names)


def get_name(email):
    """Attempt to extract name from email, otherwise ask user for name."""
    name = extract_name(email)
    choice = input(f"Is your name {name}? (Y/n)").upper()
    if choice != "Y" and choice != "":
        name = input("Name: ")
    return name


def extract_name(email):
    """Extract a name from an email (e.g. john.doe@gmail.com returns "John Doe")."""
    name = " ".join(email.split("@")[0].split("."))
    return name.title()


def display(email_to_names):
    """Display names and emails entered."""
    print()
    for email, name in email_to_names.items():
        print(f"{name} ({email})")


main()
