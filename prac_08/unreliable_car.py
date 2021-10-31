from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """specialized Car object that will drive based on reliability"""

    def __init__(self, name="", fuel=0, reliability=0):
        """initialise an unreliable car object based on the car parent class"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """drive a unreliable car object sometimes depending on reliability"""
        if self.reliability <= randint(0, 100):
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
