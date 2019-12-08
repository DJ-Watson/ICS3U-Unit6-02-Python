#!/usr/bin/env python3

# Created by: DJ Watson
# Created on: December 2019
# This program passes an array as a parameter

import random


def calculate(numberlist):

    total = 0

    for count in range(0, len(numberlist)):
        total += numberlist[count]
    return total


def main():
    # function holds list

    # variables
    numbers = []
    total = 0

    # input
    print("numbers are: ")
    for loop_c in range(0, 9):
        single_number = random.randint(0, 20)
        numbers.append(single_number)
        print("{}".format(single_number))
    print("")

    total = calculate(numbers)

    print("total = {}".format(total))


if __name__ == "__main__":
    main()
