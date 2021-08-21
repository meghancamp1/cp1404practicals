min_length = 5


def main():
    """get a password then print length in *"""
    password = get_password()
    print_asterisk(password)


def get_password():
    """get a password from user"""
    password = input("enter password:")
    while len(password) < min_length:
        print(f"password is less than {min_length} characters")
        password = input("enter password:")
    return password


def print_asterisk(password):
    """print the length in asterisks"""
    for i in range(0, len(password), 1):
        print("*", end='')


main()
