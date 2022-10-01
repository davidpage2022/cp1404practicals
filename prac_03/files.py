"""File exercises"""

LINES_TO_READ = 2


def main():
    """File exercises"""

    # Exercise 1:
    # Asks the user for their name, then open a file called "name.txt" and write that name to it.
    name = input("Enter name: ")
    out_file = open(f"{name}.txt", "w")
    print(name, file=out_file)
    out_file.close()

    # Exercise 2:
    # Open "name.txt" and read the name (as above) then prints, "Your name is Bob" (Bob is name).
    in_file = open(f"{name}.txt", "r")
    name = in_file.readline()
    print(f"Your name is {name}")
    in_file.close()

    # Exercise 3:
    # Open "numbers.txt", reads only the first two numbers and add them together then prints the result (59).
    in_file = open("numbers.txt", "r")
    total = 0
    for i in range(LINES_TO_READ):
        total += int(in_file.readline())
    in_file.close()
    print(f"The total of the first {LINES_TO_READ} numbers is: {total}")

    # Exercise 4:
    # Print the total for all lines in numbers.txt or a file with any number of numbers.
    in_file = open("numbers.txt", "r")
    total = 0
    for line in in_file:
        total += int(line)
    in_file.close()
    print(f"The total of all lines is: {total}")


main()
