'''
'heapq-use.py' contains a useful subset of imports from the 'heapq' library with a few examples.

Heap queue (priority queue) algorithm and methods.

Covered:
[
  heappush,
  heappop,
  heapify,
  heapsort
  merge,
  nlargest,
  nsmallest,
]

Heapsort / heapify:
  TC: O(n log n)
  SC: O(1)

Memory usage is better than merge sort and quick sort.

Ref:
https://docs.python.org/3/library/heapq.html
'''

from heapq import *
##################################################################
##################################################################
# heappush

# TODO

##################################################################
##################################################################
# heappop

# TODO

##################################################################
##################################################################
# heapify

# TODO

##################################################################
##################################################################
# heapsort

def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

##################################################################
##################################################################
# merge

# TODO

##################################################################
##################################################################
# nlargest

# TODO

##################################################################
##################################################################
# nsmallest

# TODO
