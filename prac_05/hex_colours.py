"""Look up the hex values for given colour names"""

NAME_TO_HEX = {"Absolute Zero": "#0048ba",
               "Acid Green": "#b0bf1a",
               "Alice Blue": "#f0f8ff",
               "Alizarin Crimson": "#e32636",
               "Amaranth": "#e52b50",
               "Amber": "#ffbf00",
               "Amethyst": "#9966cc",
               "Antique White": "#faebd7",
               "Antique White 1": "#ffefdb",
               "Antique White 2": "#eedfcc"}

max_length = max(len(name) for name in list(NAME_TO_HEX.keys()))
for name, hex_code in NAME_TO_HEX.items():
    print(f"{name:{max_length}} is {hex_code}")

name = input("Enter colour name: ").title()
while name != "":
    try:
        print(name, "is", NAME_TO_HEX[name])
    except KeyError:
        print("Invalid colour name")
    name = input("Enter colour name: ").title()
