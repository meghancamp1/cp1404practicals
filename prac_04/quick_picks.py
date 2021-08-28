import random

NUMBERS_IN_QUICK_PICK = 6
MIN = 1
MAX = 45


def main():
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Cannot generate negative quick picks!")
        number_of_quick_picks = int(input("How many quick picks? "))
    for j in range(number_of_quick_picks):
        quick_pick = []
        for i in range(NUMBERS_IN_QUICK_PICK):
            number = random.randint(MIN, MAX)
            while number in quick_pick:
                number = random.randint(MIN, MAX)
            quick_pick.append(number)
        quick_pick.sort()
        print("{:2} {:2} {:2} {:2} {:2} {:2}".format(*quick_pick))


main()
