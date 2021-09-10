from prac_06.guitar import Guitar

print("My guitars!")
guitars = []
name = input("Name: ")
while not name == "":
    year = input("Year: ")
    cost = input("Cost: $")
    guitar_to_add = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitars.append(guitar_to_add)
    print(guitar_to_add, "added.")
    name = input("Name: ")
