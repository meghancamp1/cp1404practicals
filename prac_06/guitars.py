from prac_06.guitar import Guitar

print("My guitars!")
guitars = []
name = input("Name: ")
while not name == "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar_to_add = Guitar(name, year, cost)
    guitars.append(guitar_to_add)
    print(guitar_to_add, "added.")
    name = input("Name: ")
print("These are my guitars:")
guitars.sort()
for count, guitar in enumerate(guitars, 1):
    response = "(vintage)" if guitar.is_vintage() else ""
    print("{}. {:>20} ({}), worth $ {:10,.2f} {}".format(count, guitar.name, guitar.year, guitar.cost, response))
