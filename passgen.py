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

import sys
import math
import random
import argparse
from string import digits, ascii_letters, punctuation


def make_password(blacklist="", flags="dlps", char_num=8, char_limit=1):
    """
    creating a password of a given length randomizing characters contained in charset variable.

    :param blacklist: blacklisted characters which will not being used for a password
    :param flags: a string containing the settings for the character pool
    :param char_num: integer value defining the length of the password
    :param char_limit: integer value defining the max occurrences of a single character in the end result
    :return: a string containing the password
    """
    # defining the characters which are valid for making a password
    charset = ""
    if "d" in flags:
        charset += digits
    if "l" in flags:
        charset += ascii_letters
    if "p" in flags:
        charset += punctuation
    if "s" in flags:
        charset += " "
    # preventing an infinite loop
    if char_num > len(charset) * char_limit:
        char_limit = math.ceil(char_num / len(charset))
    # putting the password together
    return_value = []
    password = ""
    while len(return_value) < char_num:
        tmp_char = random.choice(charset)
        if return_value.count(tmp_char) < char_limit and tmp_char not in blacklist:
            return_value.append(tmp_char)
    return password.join(return_value)


if __name__ == "__main__":
    # declare the help text and variables
    parser = argparse.ArgumentParser(
        prog=sys.argv[0],
        description="""
Generates a password of given length.
If no arguments are given the program will default to a password length of 8 characters and
limit the maximum occurrences of single characters to 1.

    Example:
    \"passgen.py --flags 'dlps' --length 15 --limit 1\" will result in a password containing digits(d),
    letters(l), punctuation(p) and space(s) character being 15 characters long and having each character
    maximal occur once.
    \"passgen.py -f 'dlps' -e 15 -i 1\" will do the same.
        """,
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("-f", "--flags", action="store", dest="flags", type=str, default="dlps",
                        help="defining which characters to include into the character pool")
    parser.add_argument("-e", "--length", action="store", dest="length", type=int, default=8,
                        help="defining the length of the generated password")
    parser.add_argument("-i", "--limit", action="store", dest="limit", type=int, default=1,
                        help="defining how often a single character can occur in the password")
    parser.add_argument("-b", "--blacklist", action="store", dest="blacklist", type=str, default="",
                        help="defining the characters to be excluded from password generation")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.00.04")
    results = parser.parse_args()
    # sanitize input
    try:
        for i in results.flags:
            if results.flags.count(i) > 1:
                raise ValueError("Flags can occur only once in the statement!")
        count = 4
        for i in ["d", "l", "p", "s"]:
            if i not in results.flags:
                count -=1
        if count < 1:
            raise ValueError("No valid flags given!")
        if results.limit < 1 or results.limit > results.length:
            raise ValueError("The limit has to have at least a value of 1 and makes no sense if longer than length!")
        if results.length < 8:
            results.length = 8
            print("For your own safety the password has been set to be at least 8 characters long!")
    except ValueError as error:
        print("An error occurred: {0}".format(error))
    else:
        # output password
        print("==== Your password is ... ====")
        print(make_password(results.blacklist, results.flags, results.length, results.limit))
        print("==============================")
