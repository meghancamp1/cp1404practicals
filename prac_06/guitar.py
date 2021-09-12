CURRENT_YEAR = 2021


class Guitar:
    """Represent a Guitar object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar object"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Make string of Guitar data"""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get age for Guitar object"""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Determines if Guitar is vintage or over 50 years old"""
        age = self.get_age()
        if age >= 50:
            return True
        return False

    def __lt__(self, other):
        """allows guitars ro be sorted by release year"""
        return self.year < other.year
