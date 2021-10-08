from prac_08.taxi import Taxi

prius_taxi = Taxi("Prius 1", 100)
print(prius_taxi.drive(40))
# should print 40
print(prius_taxi, ", current fare is ${:.2f}".format(prius_taxi.get_fare()))
# fare should be $49.20
prius_taxi.start_fare()
prius_taxi.drive(100)
# should print 60
print(prius_taxi, ", current fare is ${:.2f}".format(prius_taxi.get_fare()))
# fare should be $73.80

