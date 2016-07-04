#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
############################################################################
#
# passgen.py
#
############################################################################
#
# Author: Videonauth <videonauth@googlemail.com>
# Date: 30.06.2016
# Purpose:
#     Generate a randomized password of given length.
# Written for: Python 3.5.1
#
############################################################################


"""Module/Script to generate randomized passwords.
"""


import argparse
import math
import random
from string import digits, ascii_lowercase, ascii_uppercase, punctuation
import textwrap


def sanitize_input(dictionary):
    """Sanitizes the input for the make_password function.

    :param dictionary: contains a namespace of the users or others programs input
    :return: a sanitized namespace or in case of malicious input stops the program
    """
    try:
        # preventing double flags
        for flag in dictionary.flags:
            if dictionary.flags.count(flag) > 1:
                raise ValueError("Flags can occur only once in the statement!")
        # preventing that the program runs with no valid flags given
        count = 4
        for flag in ["d", "l", "u", "p", "s"]:
            if flag not in dictionary.flags:
                count -= 1
        if count < 1:
            raise ValueError("No valid flags given!")
        # throwing away any incorrect flag
        tmp_flag = ""
        for flag in dictionary.flags:
            if flag in ["d", "l", "u", "p", "s"]:
                tmp_flag += flag
        dictionary.flags = tmp_flag
        # preventing incorrect values for limit
        if dictionary.limit < 1 or dictionary.limit > dictionary.length:
            raise ValueError("The limit has to have at least a value of 1 and makes no sense if longer than length!")
        # preventing passwords below the length of 8
        if dictionary.length < 8:
            dictionary.length = 8
            print("For your own safety, the password has been set to be at least 8 characters long!")
    except ValueError as error:
        print("An error occurred: {0}".format(error))
        exit()
    else:
        return dictionary


def make_password(dictionary):
    """Make a password of a given length randomizing characters contained in char_set variable.

    :param dictionary: a namespace containing entries for blacklist, flags, length and limit
    :var dictionary.blacklist: blacklisted characters which are not used for password
    :var dictionary.flags: a string containing the settings for the character pool
    :var dictionary.length: integer value defining the length of the password
    :var dictionary.limit: integer value defining the max occurrences of a single character in the end result
    :return: a string containing the password
    """

    # Define the characters which are valid for making a password
    char_all = {"d": digits, "l": ascii_lowercase, "u": ascii_uppercase, "p": punctuation, "s": " "}
    char_set = ""
    for flag in dictionary.flags:
            char_set += char_all[flag]
    # Prevent infinite loop
    if dictionary.length > len(char_set) * dictionary.limit:
        dictionary.limit = math.ceil(dictionary.length / len(char_set))
    # Put the password together
    return_value = []
    password = ""
    while len(return_value) < dictionary.length:
        tmp_char = random.choice(char_set)
        if return_value.count(tmp_char) < dictionary.limit and tmp_char not in dictionary.blacklist:
            return_value.append(tmp_char)
    return password.join(return_value)


if __name__ == "__main__":
    # declare the help text and variables
    parser = argparse.ArgumentParser(
        description=textwrap.dedent("""\
            Generate a password of given length.
            If no arguments are given, the program will default to a password length of 8 characters and
            limit the maximum occurrences of single characters to 1.

            Example:
            "passgen.py --flags dlps --length 15 --limit 1" will result in a password containing digits (`d`),
            lowercase letters (`l`), uppercase letters (`u`) punctuation (`p`) and space (`s`) character 
            being 15 characters long and having each character maximally occur once.
            "passgen.py -f dlps -e 15 -i 1" will do the same.
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
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.0.6")
    # Output password
    print("==== Your password is ... ====")
    print(make_password(sanitize_input(parser.parse_args())))
    print("==============================")
