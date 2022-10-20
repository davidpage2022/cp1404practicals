"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")

short_code = input("Enter short state: ").upper()
while short_code != "":
    try:
        print(short_code, "is", CODE_TO_NAME[short_code])
    except KeyError:
        print("Invalid short state")
    short_code = input("Enter short state: ").upper()
