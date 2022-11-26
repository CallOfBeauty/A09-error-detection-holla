######################################################################
# Author: Dr. Patrick Shepherd      TODO: Change this to your names
# Username: shepherdp               TODO: Change this to your usernames
#
# Purpose: This program is designed to demonstrate the use of Python's string capabilities
# as a method for peeling digits from an integer
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Mario Nakazawa and Dr. Jan Pearce
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################


import random


def peel_digits(num):
    """
    Given a positive integer num, peel_digits returns a list filled with the digits
    eg. given 1984, peel_digits returns the list [1, 9, 8, 4]

    :param num: a positive integer
    :return: a list with each digit as an element in the list
    """
    str_num = str(num)                      # Converts to string to utilize Python's strong string features
    digit_list = []                         # Creates empty list
    for letter in str_num:
        digit_list.append(int(letter))      # Puts each digits into list
    # print(digit_list)                     # Testing
    return digit_list


def print_digits(digit_list): # takes a Python list as input
    """
    Given any Python list, this function prints each list element

    :param digit_list: a list
    :return: None
    """
    for digit in digit_list:
        print(digit)


def main():
    """
    This main function is intended to display the capabilities of the peel_digits() and print_digit() functions

    :return: None
    """
    year = random.randint(1000, 2018)
    print("\nYear = "+ str(year))
    year_list = peel_digits(year)           # Put list returned from function into year_list
    print("\nDigits:")
    print_digits(year_list)

main() # call main()
