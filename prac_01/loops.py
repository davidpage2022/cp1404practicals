# Example
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Loop A
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# Loop B
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Loop C
number_of_stars = int(input("Number of stars: "))
for i in range(number_of_stars):
    print("*", end='')
print()

# Loop D
for i in range(1, number_of_stars + 1):
    print("*" * i)
print()
