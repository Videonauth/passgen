#!/usr/bin/env python3.5
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
#
# Copyright: Videonauth , 2016
#
#     Permission to use, copy, modify, and distribute this software is
#     hereby granted without fee, provided that the copyright notice above
#     and this permission statement appears in all copies.
#
#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#     EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#     OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#     NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#     HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#     WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#     FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#     OTHER DEALINGS IN THE SOFTWARE.
#
############################################################################
#
#    Changelog:
#       - 30.06.2016 <--> 0.0.01
#               Initial script release
#       - 01.07.2016 <--> 0.0.02
#               Fixing bugs and documentation
#       - 03.07.2016 <--> 0.00.03
#               Added argument parser
#               Provided blacklist for blacklisting characters
#       - 03.07.2016 <--> 0.00.04
#               Fixed help output
#               Fixed errors in help description
#
############################################################################

import argparse
import math
import random
from string import digits, ascii_letters, punctuation
import sys
import textwrap


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
    parser.add_argument("-f", "--flags", action="store", dest="flags", type=str, default="dlps",
                        help="defining which characters to include into the character pool")
    parser.add_argument("-e", "--length", action="store", dest="length", type=int, default=8,
                        help="defining the length of the generated password")
    parser.add_argument("-i", "--limit", action="store", dest="limit", type=int, default=1,
                        help="defining how often a single character can occur in the password")
    parser.add_argument("-b", "--blacklist", action="store", dest="blacklist", type=str, default="",
                        help="defining the charactes to be excluded from password generation")
    parser.add_argument("-v", "--version", action="version", version="%(prog)s 0.00.04")
    results = parser.parse_args()
    print(make_password(results.blacklist, results.flags, results.length, results.limit))
