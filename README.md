# A simple password generator

Usage:
`./passgen.py [-h] [-f FLAGS] [-e LENGTH] [-i LIMIT] [-b BLACKLIST] [-v]`

Generate a password of given length. If no arguments are given, the program will default to a password length of 8 characters and limit the maximum occurrences of single characters to 1.

Example:
`passgen.py --flags dlups --length 15 --limit 1` will result in a password containing digits (`d`),
lowercase letters (`l`), uppercase letters(`u`), punctuation (`p`) and space (`s`) character, being 15 characters long, and
having each character maximally occur once. `passgen.py -f dlups -e 15 -i 1` will do the same.

Optional arguments:

```
-h, --help                              show this help message and exit
-f FLAGS, --flags FLAGS                 which characters to include into the character pool
-e LENGTH, --length LENGTH              the length of the generated password
-i LIMIT, --limit LIMIT                 how often a single character can occur in the password
-b BLACKLIST, --blacklist BLACKLIST     the characters to be excluded from password generation
-v, --version                           program's version number and exit
```

## Unit testing

To run the unit tests, run either `python3 -m unittest` or `python -m unittest` (e.g. when using a virtual environment for Python 3)
