"""
Random number questions and exercise


What did you see on line 1?
5, 20, 20, 19

What was the smallest number you could have seen, what was the largest?
Smallest: 5, largest: 20


What did you see on line 2?
7, 9, 7, 5

What was the smallest number you could have seen, what was the largest?
Smallest: 3, largest: 9   (Possible values: [3, 5, 7, 9])

Could line 2 have produced a 4?
No


What did you see on line 3?
5.26356246410921, 2.7149248283643326, 2.5403073099329987

What was the smallest number you could have seen, what was the largest?
Smallest: 2.5, largest: 5.5
Python documentation says that due to rounding caused by floating point imprecision
the largest value may not be included as a possible outcome.

"""

import random


def main():
    """Print random integer between 1 and 100 inclusive."""
    print(random.randint(1, 100))


main()
