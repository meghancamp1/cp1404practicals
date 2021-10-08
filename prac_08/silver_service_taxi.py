from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """specialised Taxi class with fanciness attribute which influences price_per_km"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=0):
        """initialise SilverServiceTaxi object based on Taxi parent class"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        return super().__str__() + f"plus flagfall of ${self.flagfall}"
