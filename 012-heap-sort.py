# Heap Sort Algorithm

from heapq import heappop, heappush
def heapsort(array):
    heap = []
    for element in array:
        heappush(heap, element)
    
    ordered = []

    # while we have elements left in the heap
    while heap:
        ordered.append(heappop(heap))
    return ordered

array = [13, 21, 15, 5, 26, 4, 17, 18, 24, 2, 1, 0, 7, 49]
print(heapsort(array))
