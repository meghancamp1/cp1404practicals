class ProgrammingLanguage:
    """Represent a Programming Language object"""

    def __init__(self, name, typing, reflection, year):
        """initialise a Programming Language object"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """check if Programming Language object is dynamic"""
        if self.typing != "Dynamic":
            return False
        return True

    def __str__(self):
        """make string of Programming Language object data"""
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                          self.year)
