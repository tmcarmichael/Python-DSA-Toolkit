'''
'math-use.py' contains a useful subset of imports from the 'math' library with a few examples.

Covered:
[
  ceil,
  comb,
  floor,
  perm,
  inf
]

Ref:
https://docs.python.org/3/library/math.html
'''

##################################################################
##################################################################
# ceil - round up

from math import ceil

ceil(3.14) # 4

##################################################################
##################################################################
# comb - combinations

from math import comb

comb(6, 2) # 15 (6 choose 2)

##################################################################
##################################################################
# floor - round down

from math import floor

floor(3.14) # 3

##################################################################
##################################################################
# perm - permutations

from math import perm

perm(6, 2) # 30 (6 permute 2)

##################################################################
##################################################################
# inf - infinity

from math import inf

n = inf() # inf