"""Guitar exercise - Guitar class
Time expected: 25 min
       actual: 15 min
"""

# from datetime import date
#
# CURRENT_YEAR = date.today().year

CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Describes the age and cost of a type of guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar with name (e.g. "Gibson L-5 CES"),
        year (e.g. 1922) and cost (16000.00)."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get how old the guitar is in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is considered "vintage"."""
        return self.get_age() > VINTAGE_AGE

    def __lt__(self, other: "Guitar"):
        return self.year < other.year
