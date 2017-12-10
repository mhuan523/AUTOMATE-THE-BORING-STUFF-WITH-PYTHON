
#! pychon3
# stongToken.py --- Measure the token to be strong: len >= 8, include both lower and upper digits, and at least one number.

import re

numberRegex = re.compile(r'''\d+''', re.VERBOSE)
lowerRegex = re.compile(r'''[a-z]+''', re.VERBOSE)
upperRegex = re.compile(r'''[A-Z]+''', re.VERBOSE)

print('Please input a token:')
token = str(input())

while True:
    if len(token) < 8:
        print('The token must longer than 8.')
        print('Please reinput a token:')
        token = str(input())
    if numberRegex.search(token) == None:
        print('The token must include at least one number.')
        print('Please reinput a token:')
        token = str(input())
    if lowerRegex.search(token) == None:
        print('The token must include lower.')
        print('Please reinput a token:')
        token = str(input())
    if upperRegex.search(token) == None:
        print('The token must include upper digits.')
        print('Please reinput a token:')
        token = str(input())
    else:
        print('This is a strong token.')
        break

