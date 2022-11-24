"""Band class."""


class Band:
    """Describes a band, including musicians in the band."""

    def __init__(self, name):
        """Construct band."""
        self.name = name
        self.musicians = []

    def __str__(self):
        musician_strings = [str(musician) for musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strings)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Returns a string containing the results of all musicians playing their instruments."""
        play_string = ""
        for musician in self.musicians:
            play_string = "".join([play_string, musician.play(), "\n"])
        return play_string
