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
# heappush - push item onto heap, maintaining the heap invariant

a = [3,5,7,2,4]
a.heappush(1) # [1, 2, 3, 4, 5, 7]
a.heappush(9) # [1, 2, 3, 4, 5, 7, 9]

##################################################################
##################################################################
# heappop - pop the smallest item off the heap, maintaining the heap invariant

a.heappop() # 1
a.heappop() # 2

##################################################################
##################################################################
# heapify - transform list into a heap, in-place, in linear time

a = [5,3,8,3,6,2,1]
a.heapify() # [1, 2, 3, 3, 5, 6, 8]

##################################################################
##################################################################
# heapsort - return a new sorted list, leaving the original data unaltered

def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
    return [heappop(h) for i in range(len(h))]

heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

##################################################################
##################################################################
# merge - Merge multiple (sorted) inputs into a single sorted output.

a = [1,5,7,9]
b = [2,3,4,6,8]
list(merge(a, b)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

##################################################################
##################################################################
# nlargest - return a list with the n largest elements from the dataset defined by iterable

nlargest(3, a) # [9, 8, 7]

##################################################################
##################################################################
# nsmallest - return a list with the n smallest elements from the dataset defined by iterable

nsmallest(3, a) # [1, 2, 3]
