class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        musician_strings = [str(musician) for musician in self.musicians]
        return f"{self.name} ({', '.join(musician_strings)})"

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        play_string = ""
        for musician in self.musicians:
            play_string = "".join([play_string, musician.play(), "\n"])
        return play_string
