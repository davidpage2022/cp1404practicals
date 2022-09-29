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
    print(f"Your name is {name}")
    in_file.close()

    # Exercise 3:
    # Open "numbers.txt", reads only the first two numbers and add them together then prints the result (59).
    in_file = open("numbers.txt", "r")
    sum = 0
    for i in range(LINES_TO_READ):
        sum += int(in_file.readline())
    print(f"The sum of the first {LINES_TO_READ} numbers is: {sum}")
    in_file.close()

    # Exercise 4:
    # Todo


main()
