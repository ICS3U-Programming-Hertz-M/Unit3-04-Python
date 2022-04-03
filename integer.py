#!/usr/bin/env python3
#
# Created by: Hertz Antonella
# Created on: Mar 31, 2022
# This program asks the user to enter an interger and
# checks  if the number entered is positive, negative, or just zero.


def main():
    # get the user number
    user_numb = int(input("Enter a number: "))
    print("")

    # check if the user number entered is positive, negative or zero, then
    # Display the senario
    if user_numb > 0:
        print(" your number is positive")
    elif user_numb < 0:
        print("your number is negative")
    elif user_numb == 0:
        print("your number is zero")


if __name__ == "__main__":
    main()
