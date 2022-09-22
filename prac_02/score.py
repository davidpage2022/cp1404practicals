"""
CP1404/CP5632 - Practical
Determine score status
"""


def main():
    """Ask the user for their score, then print the result"""
    score = float(input("Enter score: "))
    print(get_result(score))


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


main()
