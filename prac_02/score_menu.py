"""Program for interacting with scores"""

MENU = """(G)et score
(P)rint result
Print (s)tars
(Q)uit"""


def main():
    """Program for interacting with scores"""
    score = 0
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter score: "))
            while score < 0 or score > 100:
                print("Invalid score")
                score = int(input("Enter score: "))
        elif choice == "P":
            print(get_result(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>>").upper()
    print("Thank you")


def get_result(score):
    """Returns the result description for a score value between 0 and 100"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    else:
        return "Excellent"


def print_stars(score):
    """Print as many stars as the score"""
    print("*" * score)


main()
