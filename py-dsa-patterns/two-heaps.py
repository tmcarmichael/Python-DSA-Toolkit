# Example of two heaps pattern

import heapq

def find_median_of_a_number_stream(nums):
    max_heap = []
    min_heap = []
    result = []

    for num in nums:
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        # either both the heaps will have equal number of elements or max-heap will have one more element than the min-heap
        if len(max_heap) == len(min_heap) + 2:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(max_heap) == len(min_heap) - 1:
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # add the median to the result array
        if len(max_heap) == len(min_heap):
            # we have even number of elements, take the average of middle two elements
            result.append(-max_heap[0] / 2.0 + min_heap[0] / 2.0)
        else:
            # because max-heap will have one more element than the min-heap
            result.append(-max_heap[0] / 1.0)

    return result