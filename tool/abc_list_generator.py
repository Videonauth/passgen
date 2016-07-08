#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
############################################################################
#
# abc_list_generator.py
#
############################################################################
#
# Author: Videonauth <videonauth@googlemail.com>
# Date: 08.07.2016
# Purpose:
#     Generate a word-list for the abc and digit check.
# Written for: Python 3.5.1
#
############################################################################

from string import ascii_lowercase, ascii_uppercase, digits

natural = digits[1:] + '0'


with open('../lists/abc.wl', 'r+') as file:
    for a in range(3, len(ascii_lowercase) + 1):
        for b in range(len(ascii_lowercase)):
            if len(ascii_lowercase[b: b + a]) == a:
                file.write(ascii_lowercase[b: b + a] + '\n')
    for a in range(3, len(ascii_uppercase) + 1):
        for b in range(len(ascii_uppercase)):
            if len(ascii_uppercase[b: b + a]) == a:
                file.write(ascii_uppercase[b: b + a] + '\n')
    for a in range(3, len(digits) + 1):
        for b in range(len(digits)):
            if len(digits[b: b + a]) == a:
                file.write(digits[b: b + a] + '\n')
    for a in range(3, len(natural) + 1):
        for b in range(len(natural)):
            if len(natural[b: b + a]) == a:
                file.write(natural[b: b + a] + '\n')
    reversed_lowercase = ascii_lowercase[:: -1]
    reversed_uppercase = ascii_uppercase[:: -1]
    reversed_digits = digits[:: -1]
    reversed_natural = natural[:: -1]
    for a in range(3, len(reversed_lowercase) + 1):
        for b in range(len(reversed_lowercase)):
            if len(reversed_lowercase[b: b + a]) == a:
                file.write(reversed_lowercase[b: b + a] + '\n')
    for a in range(3, len(reversed_uppercase) + 1):
        for b in range(len(reversed_uppercase)):
            if len(reversed_uppercase[b: b + a]) == a:
                file.write(reversed_uppercase[b: b + a] + '\n')
    for a in range(3, len(reversed_digits) + 1):
        for b in range(len(reversed_digits)):
            if len(reversed_digits[b: b + a]) == a:
                file.write(reversed_digits[b: b + a] + '\n')
    for a in range(3, len(reversed_natural) + 1):
        for b in range(len(reversed_natural)):
            if len(reversed_natural[b: b + a]) == a:
                file.write(reversed_natural[b: b + a] + '\n')

file.close()
