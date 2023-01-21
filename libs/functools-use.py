'''
'functools-use.py' contains a useful subset of imports from the 'functools' library with a few examples.

Covered:
[
  lru_cache
]

Ref:
https://docs.python.org/3/library/functools.html
'''

##################################################################
##################################################################
# lru_cache

from functools import *

# Example one
# lru_cache with maxsize kwarg set
@lru_cache(maxsize=32)
def get_pep(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = 'https://peps.python.org/pep-%04d/' % num
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'

for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
    pep = get_pep(n)
    print(n, len(pep))

get_pep.cache_info() # CacheInfo(hits=3, misses=8, maxsize=32, currsize=8)
get_pep.cache_clear() # Clear the cache and cache statistics

# Example two
# lru_cache with no maxsize kwarg set
@lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

[fib(n) for n in range(16)] # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]

fib.cache_info() # CacheInfo(hits=28, misses=16, maxsize=None, currsize=16)
fib.cache_clear() # Clear the cache and cache statistics