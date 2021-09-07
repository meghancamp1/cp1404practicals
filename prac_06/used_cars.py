"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))
    # modifications:
    # no. 1
    limo = Car("Limo", 100)
    # no. 2
    limo.add_fuel(20)
    # no. 3
    print("fuel =", limo.fuel)
    # no. 4
    limo.drive(115)
    # no. 5
    print("odo =", limo.odometer)
    print(limo)


main()
