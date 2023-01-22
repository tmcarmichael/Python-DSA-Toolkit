'''
'itertools-use.py' contains a useful subset of imports from the 'itertools' library with a few examples.

Iterator methods:
[
  accumulate,
  chain,
  chain.from_iterable,
  pairwise,
  starmap
]

Combinatorics methods:
[
  product,
  permutations,
  combinations,
  combinations_with_replacement
]

Ref:
https://docs.python.org/3/library/itertools.html
'''

##################################################################
##################################################################
# accumulate

from itertools import accumulate

a = [1, 2, 3, 4, 5]
list(accumulate(a)) # [1, 3, 6, 10, 15]

##################################################################
##################################################################
# chain
# chain.from_iterable

from itertools import chain

a = [1, 2, 3]
b = [4, 5, 6]
list(chain(a, b)) # [1, 2, 3, 4, 5, 6]

a = [[1, 2, 3], [4, 5, 6]]
list(chain.from_iterable(a)) # [1, 2, 3, 4, 5, 6]

##################################################################
##################################################################
# pairwise

from itertools import pairwise

a = [1, 2, 3, 4, 5]
list(pairwise(a)) # [(1, 2), (2, 3), (3, 4), (4, 5)]

##################################################################
##################################################################
# starmap - map with multiple arguments
# Return an iterator whose values are returned from the function evaluated with an argument tuple taken from the given sequence.

from itertools import starmap

a = [(1, 2), (3, 4), (5, 6)]
list(starmap(lambda x, y: x + y, a)) # [3, 7, 11]

##################################################################
##################################################################
# product - cartesian product of two input iterables

from itertools import product

a = [1, 2]
b = [3, 4]
list(product(a, b)) # [(1, 3), (1, 4), (2, 3), (2, 4)]

##################################################################
##################################################################
# permutations - all possible permutations of a given iterable

from itertools import permutations

a = [1, 2, 3]
list(permutations(a)) # [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

##################################################################
##################################################################
# combinations - all possible combinations of a given iterable

from itertools import combinations

a = [1, 2, 3]
list(combinations(a, 2)) # [(1, 2), (1, 3), (2, 3)]

##################################################################
##################################################################
# combinations_with_replacement - all possible combinations of a given iterable with replacement

from itertools import combinations_with_replacement

a = [1, 2, 3]

list(combinations_with_replacement(a, 1)) # [(1,), (2,), (3,)]
list(combinations_with_replacement(a, 2)) # [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
list(combinations_with_replacement(a, 3)) # [(1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 2), (1, 2, 3), (1, 3, 3), (2, 2, 2), (2, 2, 3), (2, 3, 3), (3, 3, 3)]

