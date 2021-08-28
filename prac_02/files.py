name = input("enter name: ")
out_file = open("name.txt", "w")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read()
print("Your name is {}".format(name))
in_file.close()

in_file_new = open("numbers.txt", "r")
result1 = int(in_file_new.readline())
result2 = int(in_file_new.readline())
print(result1 + result2)
in_file_new.close()

total = 0
in_file_new = open("numbers.txt", "r")
for line in in_file_new:
    number = int(line)
    total = total + number
print(total)
in_file_new.close()
