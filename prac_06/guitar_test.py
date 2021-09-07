from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013)
print(gibson)
print(gibson.get_age())
# expected 99, got 99
print(gibson.is_vintage())
# expected True, got True
print(another_guitar)
print(another_guitar.get_age())
# expected 8, got 8
print(another_guitar.is_vintage())
# expected False, got False

