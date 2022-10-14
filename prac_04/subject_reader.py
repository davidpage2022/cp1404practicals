"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        parts = line.split(',')  # Separate the data into its parts
        data.append([parts[0], parts[1], int(parts[2])])
    input_file.close()
    return data


def display_subject_details(data):
    """Print the details for subjects in data"""
    for subject in data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()
