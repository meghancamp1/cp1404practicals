from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            pass
        elif choice == "d":
            pass
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").lower()
    print("Total trip cost: {}")
