"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


# problem 1: ask the user for their score and print the result


def main():
    score = float(input("Enter score: "))
    result = return_result_from_score(score)
    print(result)

    # 2: generate random score and print result

    score = random.randint(0, 100)
    result = return_result_from_score(score)
    print(result)


def return_result_from_score(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "passable"
    else:
        return "Bad"


main()




