"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        parts = line.split(',')  # Separate the data into its parts
        data.append([parts[0], parts[1], int(parts[2])])
    input_file.close()
    return data


main()
