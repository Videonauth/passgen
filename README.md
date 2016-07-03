A simple password generator.


usage:  
`./passgen.py [-h] [-f FLAGS] [-e LENGTH] [-i LIMIT] [-b BLACKLIST] [-v]`  

Generates a password of given length. If no arguments are given the program will default to a password length of 8 characters and limit the maximum occurrences of single characters to 1.  

Example:  
`passgen.py --flags 'dlps' --length 15 --limit 1` will result in a password containing digits(d),
letters(l), punctuation(p) and space(s) character being 15 characters long and
having each character maximal occur once.  
`passgen.py -f 'dlps' -e 15 -i 1` will do the same.  

optional arguments:  
  `-h, --help`            
                        show this help message and exit  
  `-f FLAGS, --flags FLAGS`  
                        defining which characters to include into the character pool  
  `-e LENGTH, --length LENGTH`  
                        defining the length of the generated password  
  -`i LIMIT, --limit LIMIT`  
                        defining how often a single character can occur in the password  
  `-b BLACKLIST, --blacklist BLACKLIST`  
                        defining the charactes to be excluded from password generation  
  `-v, --version`         
                        show program's version number and exit  
