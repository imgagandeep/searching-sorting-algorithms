# Quick Sort Algorithm

""" 
# In this program pivot = first
def pivot_place(list, first, last):
    pivot = list[first]
    print(pivot)
    left = first + 1
    right = last
    while True:
        while left <= right and list[left] <= pivot:
            left += 1
        while left <= right and list[right] >= pivot:
            right -= 1
        if right < left:
            break
        else:
            list[left], list[right] = list[right], list[left]
    list[first], list[right] = list[right], list[first]
    return right

def quicksort(list, first, last):
    if first < last:
        p = pivot_place(list, first, last)
        quicksort(list, first, p - 1)
        quicksort(list, p + 1, last)

list = [56, 26, 93, 17, 31, 44]
n = len(list)
quicksort(list, 0, n - 1)
print(list)
 """


# In this program pivot = last
import random
def pivot_place(list, first, last):
    rindex = random.randint(first, last)
    list[rindex], list[last] = list[last], list[rindex]
    pivot = list[last]
    print(pivot)
    left = first
    right = last - 1
    while True:
        while left <= right and list[left] <= pivot:
            left += 1
        while left <= right and list[right] >= pivot:
            right -= 1
        if right < left:
            break
        else:
            list[left], list[right] = list[right], list[left]
    list[last], list[left] = list[left], list[last]
    return left

def quicksort(list, first, last):
    if first < last:
        p = pivot_place(list, first, last)
        quicksort(list, first, p - 1)
        quicksort(list, p + 1, last)

list = [56, 26, 93, 17, 31, 44]
n = len(list)
quicksort(list, 0, n - 1)
print(list)
