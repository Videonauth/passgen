import argparse
from passgen import make_parser, sanitize_input
import unittest


class PassGenTestCase(unittest.TestCase):

    def setUp(self):
        self.parse_args = make_parser().parse_args


    def test_duplicate_flags(self):
        for duplicate_flag in ['dd', 'll', 'uu', 'pp', 'ss']:
            with self.assertRaises(ValueError):
                sanitize_input(self.parse_args(['-f', duplicate_flag]))

    def test_no_valid_flags(self):
        for invalid_flag in ['a', 'b', 'c']:
            with self.assertRaises(ValueError):
                sanitize_input(self.parse_args(['-f', invalid_flag]))

    def test_limit_lower_bound(self):
        with self.assertRaises(ValueError):
            sanitize_input(self.parse_args(['-i', '0']))

    def test_limit_upper_bound(self):
        with self.assertRaises(ValueError):
            sanitize_input(self.parse_args(['-i', '9']))

    def test_valid_flags(self):
        for valid_flag in ['dl', 'du', 'dp', 'ds', 'dlu', 'dlup', 'dlups']:
            dictionary = sanitize_input(self.parse_args(['-f', valid_flag]))
            self.assertIsInstance(dictionary, argparse.Namespace)

if __name__ == '__main__':
    unittest.main()
