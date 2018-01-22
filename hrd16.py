
#!/bin/python

import sys


S = raw_input().strip()

try:
    number = int(S)
except ValueError:
    print('Bad String')
    sys.exit()

print number