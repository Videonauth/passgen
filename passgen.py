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
#        - 30.06.2016 <--> 0.0.01
#                Initial script release
#        - 01.07.2016 <--> 0.0.02
#                Fixing bugs and documentation
#
############################################################################

import sys
import math
import random
from string import digits, ascii_letters, punctuation

# defining the characters which are valid for making a password
charset = digits + ascii_letters + punctuation + " "


def make_password(char_num=8, char_limit=1):
    """
    creating a password of a given length randomizing characters contained in charset variable.

    :param char_num: integer value defining the length of the password
    :param char_limit: integer value defining the max occurrences of a single character in the end result
    :return: a string containing the password
    """
    # preventing an infinite loop
    if char_num > len(charset) * char_limit:
        char_limit = math.ceil(char_num / len(charset))
    # putting the password together
    return_value = []
    while len(return_value) < char_num:
        tmp_char = random.choice(charset)
        if return_value.count(tmp_char) < char_limit:
            return_value.append(tmp_char)
    return "".join(return_value)


if __name__ == "__main__":
    argv = [int(i) for i in sys.argv[1:3]]
    print(make_password(*argv))
