from prac_08.silver_service_taxi import SilverServiceTaxi

silver = SilverServiceTaxi("Hummer", fuel=100, fanciness=2)
silver.drive(18)
print(silver.get_fare())
# should print 48.80
print(silver)
# should print Hummer, fuel=82, odometer=18, 18km on current fare, $2.46/km plus flagfall of $4.50
