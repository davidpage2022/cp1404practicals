"""Programming Language exercise - ProgrammingLanguage class
Time expected: 20 min
       actual: 6 min
"""


class ProgrammingLanguage:
    """Information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialise programming language.

        name: Name of the language.
        typing: Typing style: can be "static" or "dynamic".
        reflection: boolean, if reflection is supported.
        year: integer, year of creation. (e.g. 2022)
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if the programming language uses dynamic typing."""
        return self.typing.title() == "Dynamic"
