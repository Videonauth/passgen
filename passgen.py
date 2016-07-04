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

import argparse
import math
import random
from string import digits, ascii_letters, punctuation
import textwrap


def make_password(blacklist="", flags="dlps", length=8, limit=1):
    """Make a password of a given length randomizing characters contained in char_set variable.

    :param blacklist: blacklisted characters which are not used for password
    :param flags: a string containing the settings for the character pool
    :param length: integer value defining the length of the password
    :param limit: integer value defining the max occurrences of a single character in the end result
    :return: a string containing the password
    """
    # Define the characters which are valid for making a password
    char_all = {'d': digits, 'l': ascii_letters, 'p': punctuation, 's': ' '}
    char_set = ""
    for flag in flags:
        if flag in char_all:
            char_set += char_all[flag]
    # Prevent infinite loop
    if length > len(char_set) * limit:
        limit = math.ceil(length / len(char_set))
    # Put the password together
    return_value = []
    password = ""
    while len(return_value) < length:
        tmp_char = random.choice(char_set)
        if return_value.count(tmp_char) < limit and tmp_char not in blacklist:
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
            letters (`l`), punctuation (`p`) and space (`s`) character being 15 characters long and
            having each character maximally occur once.
            "passgen.py -f dlps -e 15 -i 1" will do the same.
            """),
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("-f", "--flags", type=str, default="dlps",
                        help="which characters to include into the character pool")
    parser.add_argument("-e", "--length", type=int, default=8,
                        help="the length of the generated password")
    parser.add_argument("-i", "--limit", type=int, default=1,
                        help="how often a single character can occur in the password")
    parser.add_argument("-b", "--blacklist", type=str, default="",
                        help="the characters to be excluded from password generation")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.00.04")
    results = parser.parse_args()
    # Sanitize input
    try:
        for i in results.flags:
            if results.flags.count(i) > 1:
                raise ValueError("Flags can occur only once in the statement!")
        count = 4
        for i in ["d", "l", "p", "s"]:
            if i not in results.flags:
                count -= 1
        if count < 1:
            raise ValueError("No valid flags given!")
        if results.limit < 1 or results.limit > results.length:
            raise ValueError("The limit has to have at least a value of 1 and makes no sense if longer than length!")
        if results.length < 8:
            results.length = 8
            print("For your own safety, the password has been set to be at least 8 characters long!")
    except ValueError as error:
        print("An error occurred: {0}".format(error))
    else:
        # Output password
        print("==== Your password is ... ====")
        print(make_password(**vars(results)))
        print("==============================")
