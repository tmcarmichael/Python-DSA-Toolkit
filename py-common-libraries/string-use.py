'''
'string-use.py' contains a useful subset of imports from the 'string' lib with a few examples.

Covered:
[
  ascii_letters,
  ascii_lowercase,
  ascii_uppercase,
  digits,
]

Ref:
https://docs.python.org/3/library/stdtypes.html
'''

import string
##################################################################
##################################################################
# ascii_letters

s = string.ascii_letters() # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

##################################################################
##################################################################
# ascii_lowercase

s = string.ascii_lowercase() # 'abcdefghijklmnopqrstuvwxyz'

##################################################################
##################################################################
# ascii_uppercase

s = string.ascii_uppercase() # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

##################################################################
##################################################################
# digits

s = string.digits() # '0123456789'