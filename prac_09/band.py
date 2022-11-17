class Band:
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        return ""

    def add(self, musician):
        self.musicians.append(musician)

    def play(self):
        pass
