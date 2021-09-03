email_to_name = {}
email = input("Email: ")
while email != "":
    names = email.split("@")[0].split(".")
    name = " ".join(names).title()
    confirmation = input("Is your name {}? (Y/n) ".format(name))
    if confirmation.lower() != "y" and confirmation != "":
        name = input("Name: ")
        while name == "":
            print("Input cannot be blank")
            name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")

for email, name in email_to_name.items():
    print("{} ({})".format(name, email))
