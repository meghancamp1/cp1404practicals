from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """specialised Taxi class with fanciness attribute which influences price_per_km"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=0):
        """initialise SilverServiceTaxi object based on Taxi parent class"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """get fare for SilverServiceTaxi object"""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """return a str like Taxi but with flagfall added"""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)
