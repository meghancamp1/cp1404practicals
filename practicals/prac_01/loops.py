for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1,):
    print(i, end=' ')
print()

number_of_stars = int(input("enter the number of stars: "))
for i in range(0, number_of_stars, 1):
    print("*", end=' ')
print()

final_number_of_stars = int(input("enter the number of stars in the final row: "))
for i in range(0, final_number_of_stars, 1):
    for j in range(0, i+1, 1):
        print("*", end=' ')
    print()
