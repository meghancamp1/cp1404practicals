# question 1: basic list operations
numbers = []
for i in range(5):
    numbers.append(int(input("number: ")))
first_number = numbers[0]
print("the first number is {}".format(numbers[0]))
print("the last number is {}".format(numbers[4]))
print("the smallest number is {}".format(min(numbers)))
print("the largest number is {}".format(max(numbers)))
average_number = sum(numbers)/len(numbers)
print("the average of the numbers is {}".format(average_number))


# question 2: woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("enter username:")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
