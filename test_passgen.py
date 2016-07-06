#!/usr/bin/env python3

import argparse
from passgen import make_parser, sanitize_input
import unittest


class PassGenTestCase(unittest.TestCase):

    def setUp(self):
        self.parse_args = make_parser().parse_args

    def test_duplicate_flags(self):
        with self.assertRaises(ValueError):
            for duplicate_flag in ['dd', 'll', 'uu', 'pp', 'ss']:
                sanitize_input(self.parse_args(['-f', duplicate_flag]))

    def test_no_valid_flags(self):
        with self.assertRaises(ValueError):
            for invalid_flag in ['a', 'b', 'c']:
                sanitize_input(self.parse_args(['-f', invalid_flag]))

    def test_mixed_valid_invalid_flags(self):
        with self.assertRaises(ValueError):
            for mixed_flags in ['dq']:
                sanitize_input(self.parse_args(['-f', mixed_flags]))

    def test_duplicate_characters_blacklist(self):
        with self.assertRaises(ValueError):
            for duplicate_characters in ['aa', 'bb', 'cc']:
                sanitize_input(self.parse_args(['-f', 'l', '-b', duplicate_characters]))

    def test_invalid_character_blacklist(self):
        with self.assertRaises(ValueError):
            sanitize_input(self.parse_args(['-f', 'd', '-b', 'a']))
            sanitize_input(self.parse_args(['-f', 'l', '-b', '1']))

    def test_number_valid_characters(self):
        with self.assertRaises(ValueError):
            sanitize_input(self.parse_args(['-f', 'd', '-b', '0123456789']))

    def test_length_lower_bound(self):
        dictionary = sanitize_input(self.parse_args(['-e', '7']))
        self.assertEqual(dictionary['length'], 8)

    def test_limit_lower_bound(self):
        with self.assertRaises(ValueError):
            sanitize_input(self.parse_args(['-i', '0']))

    def test_limit_upper_bound(self):
        with self.assertRaises(ValueError):
            sanitize_input(self.parse_args(['-i', '9']))

    def test_sufficiently_large_limit(self):
        dictionary = sanitize_input(self.parse_args(['-f', 'd', '-e', '11']))
        self.assertEqual(dictionary['limit'], 2)

    def test_valid_flags(self):
        for valid_flag in ['dl', 'du', 'dp', 'ds', 'dlu', 'dlup', 'dlups']:
            dictionary = sanitize_input(self.parse_args(['-f', valid_flag]))
            self.assertIsInstance(dictionary, dict)

    def test_valid_blacklist(self):
        dictionary = sanitize_input(self.parse_args(['-f', 'd', '-b', '012345678']))
        self.assertIsInstance(dictionary, dict)

if __name__ == '__main__':
    unittest.main(buffer=True)
