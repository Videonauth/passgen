#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
############################################################################
#
# keyboard_list_generator.py
#
############################################################################
#
# Author: Videonauth <videonauth@googlemail.com>
# Date: 09.07.2016
# Purpose:
#     Generate a word-list for the keyboard sequence check.
# Written for: Python 3.5.1
#
############################################################################

de_lowercase = "qwertzuiopü+asdfghjkllöä#yxcvbnm,.-"
de_uppercase = "°!§$%&/()=?WERTZUIOPÜ*ASDFGHJKLÖÄ'YXCVBNM;:_"
en_lowercase = "-=qwertyuiop[]asdfghjkl;'zxcvbnm,./"
en_uppercase = "~!@#$%^&*()_QWERTYUIOP{}ASDFGHJKL:ZXCVBNM<>?"


# next line might error out if destination file does not exist
with open('../lists/keyboard.wl', 'r+') as file:
    for a in range(3, len(de_lowercase) + 1):
        for b in range(len(de_lowercase)):
            if len(de_lowercase[b: b + a]) == a:
                file.write(de_lowercase[b: b + a] + '\n')
    for a in range(3, len(de_uppercase) + 1):
        for b in range(len(de_uppercase)):
            if len(de_uppercase[b: b + a]) == a:
                file.write(de_uppercase[b: b + a] + '\n')
    for a in range(3, len(en_lowercase) + 1):
        for b in range(len(en_lowercase)):
            if len(en_lowercase[b: b + a]) == a:
                file.write(en_lowercase[b: b + a] + '\n')
    for a in range(3, len(en_uppercase) + 1):
        for b in range(len(en_uppercase)):
            if len(en_uppercase[b: b + a]) == a:
                file.write(en_uppercase[b: b + a] + '\n')
    de_lowercasere = de_lowercase[:: -1]
    de_uppercasere = de_uppercase[:: -1]
    en_lowercasere = en_lowercase[:: -1]
    en_uppercasere = en_uppercase[:: -1]
    for a in range(3, len(de_lowercasere) + 1):
        for b in range(len(de_lowercasere)):
            if len(de_lowercasere[b: b + a]) == a:
                file.write(de_lowercasere[b: b + a] + '\n')
    for a in range(3, len(de_uppercasere) + 1):
        for b in range(len(de_uppercasere)):
            if len(de_uppercasere[b: b + a]) == a:
                file.write(de_uppercasere[b: b + a] + '\n')
    for a in range(3, len(en_lowercasere) + 1):
        for b in range(len(en_lowercasere)):
            if len(en_lowercasere[b: b + a]) == a:
                file.write(en_lowercasere[b: b + a] + '\n')
    for a in range(3, len(en_uppercasere) + 1):
        for b in range(len(en_uppercasere)):
            if len(en_uppercasere[b: b + a]) == a:
                file.write(en_uppercasere[b: b + a] + '\n')
file.close()
