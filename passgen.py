#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
############################################################################
#
# passgen.py
#
############################################################################
#
# Author: Videonauth <videonauth@googlemail.com>
# Author: edwinksl <edwinksl@gmail.com>
# Date: 30.06.2016
# Purpose:
#     Generate a randomized password of given length.
# Written for: Python 3.5.1
#
############################################################################

"""Module/Script to generate randomized passwords."""

import argparse
from collections import Counter
import math
import random
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import textwrap

__version__ = "0.0.8"

# Define the characters which are valid for making a password
char_all = {"d": digits, "l": ascii_lowercase, "u": ascii_uppercase, "p": punctuation, "s": " "}


def sanitize_input(dictionary):
    """Sanitize the input for the make_password function.

    :param dictionary: contains a namespace of the users' or other programs' input
    :return: a dictionary containing entries for sanitized string, length and limit
             or stops the program in case of malicious input
    """
    try:
        c_flags = Counter(dictionary.flags)
        c_blacklist = Counter(dictionary.blacklist)
        char_set = ''

        for key, value in c_flags.items():
            # Prevent duplicate flags
            if value > 1:
                raise ValueError("Flags can occur only once in the statement!")
            # Prevent program from running with no valid flags or a mix of valid and invalid flags
            if key not in char_all.keys():
                raise ValueError("Invalid flags given!")
            char_set += char_all[key]

        for key, value in c_blacklist.items():
            # Prevent duplicate characters in blacklist
            if value > 1:
                raise ValueError('Duplicate characters in blacklist!')
            # Raise ValueError when character in blacklist does not exist in any of the valid flags
            if key not in char_set:
                raise ValueError('Character in blacklist is invalid for flags given!')
            char_set = char_set.replace(key, '')  # note that assignment is required because strings are immutable

        # Check that length of char_set is valid
        # Length of char_set is 0 when all characters in blacklist are the same as that specified by all flags
        if len(char_set) == 0:
            raise ValueError('Number of valid characters is zero!')

        # Prevent passwords below the length of 8
        if dictionary.length < 8:
            dictionary.length = 8
            print("For your own safety, the password has been set to be 8 characters long!")

        # Prevent incorrect values for limit
        if not 1 <= dictionary.limit <= dictionary.length:
            raise ValueError("The limit has to have at least a value of 1 and makes no sense if longer than length!")

        # Ensure limit is sufficiently large for length to prevent infinite loop
        if dictionary.length > len(char_set) * dictionary.limit:
            invalid_limit = dictionary.limit
            dictionary.limit = math.ceil(dictionary.length / len(char_set))
            print('Limit has been increased from {} to {}!'.format(invalid_limit, dictionary.limit))

    except ValueError as error:
        print("An error occurred: {}".format(error))
        raise
    else:
        return {'char_set': char_set, 'length': dictionary.length, 'limit': dictionary.limit}


def make_password(dictionary):
    """Make a password of a given length randomizing characters contained in char_set variable.

    :param dictionary: a dictionary containing entries for sanitized string, length and limit
    :var dictionary.char_set: a sanitized string containing the settings for the character pool
    :var dictionary.length: integer value defining the length of the password
    :var dictionary.limit: integer value defining the maximum occurrences of a single character in the end result
    :return: a string containing the password
    """
    # Put the password together
    return_value = []
    password = ""
    while len(return_value) < dictionary['length']:
        tmp_char = random.choice(dictionary['char_set'])
        if return_value.count(tmp_char) < dictionary['limit']:
            return_value.append(tmp_char)
    return password.join(return_value)


def make_parser():
    """Make parser."""
    # Declare the help text and variables
    parser = argparse.ArgumentParser(
        description=textwrap.dedent("""\
            Generate a password of given length.
            If no arguments are given, the program will default to a password length of 8 characters and
            limit the maximum occurrences of single characters to 1.

            Example:
            "passgen.py --flags dlups --length 15 --limit 1" will result in a password containing digits ("d"),
            lowercase letters ("l"), uppercase letters ("u"), punctuation ("p") and space ("s") character,
            being 15 characters long, and having each character maximally occur once.
            "passgen.py -f dlups -e 15 -i 1" will do the same.
            """),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-f", "--flags", type=str, default="dlups",
                        help="which characters to include into the character pool")
    parser.add_argument("-e", "--length", type=int, default=8,
                        help="the length of the generated password")
    parser.add_argument("-i", "--limit", type=int, default=1,
                        help="how often a single character can occur in the password")
    parser.add_argument("-b", "--blacklist", type=str, default="",
                        help="the characters to be excluded from password generation")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s "+__version__)
    return parser

def check_password(password, dictionary):
    """Checks the password for its strength.

    :param password: a string containing the password
    :return: an integer containing the final calculated score (temporary)
    """
    score = 0
    # test for proper length
    if len(password) < 10:
        score -= (10 - len(password)) * 5
        print("Is not 15 characters or more: Length: {} Result: {}".format(-(10 - len(password)),
                                                                           -((10 - len(password)) * 5)))
    else:
        score += (len(password) - 10) * 5
        print("Is not 15 characters or more: Length: {} Result: {}".format((len(password) - 10),
                                                                           ((len(password) - 10) * 5)))
    # test for lowercase
    if any(char in ascii_lowercase for char in password):
        score += 20
        print("Contains lowercase letters: Result: +20")
    else:
        score -= 20
        print("Contains no lowercase letters: Result: -20")
    # test for uppercase
    if any(char in ascii_uppercase for char in password):
        score += 20
        print("Contains uppercase letters: Result: +20")
    else:
        score -= 20
        print("Contains no uppercase letters: Result: -20")
    # test for punctuation
    if any(char in punctuation for char in password):
        score += 20
        print("Contains punctuation letters: Result: +20")
    else:
        score -= 20
        print("Contains no punctuation letters: Result: -20")
    # test for digits
    if any(char in digits for char in password):
        score += 20
        print("Contains numerical digits: Result: +20")
    else:
        score -= 20
        print("Contains no numerical digits: Result: -20")
    # test for special characters
        # left out for now
    # test for identical characters 3 or more identical in sequence
    count = 0
    for i in dictionary['char_set']:
        if i in password and dictionary['limit'] > 1:
            if password.count(i) > 2:
                for j in range(3, dictionary['limit'] + 1):
                    if i * j in password:
                        count += 1
    if count > 0:
        score -= count * 5
        print("Contains characters in sequence: Result: {}".format(-(count * 5)))
    else:
        score += dictionary['limit'] * 5
        print("Contains no characters in sequence: Result: {}".format((dictionary['limit'] * 5)))
    # test for character chains keyboard 3 or more identical in sequence
        # TODO: implement it
    # test for 'abc' or digit rows 3 or more in sequence
        # TODO: implement it
    # test for word list vulnerability
        # TODO: implement it
    return score


if __name__ == "__main__":
    options = make_parser()
    # Output password
    passwd = make_password(sanitize_input(options.parse_args()))
    print("==== Your password is ... ====")
    print(passwd)
    print("==============================")
    print(check_password(passwd, sanitize_input(options.parse_args())))
