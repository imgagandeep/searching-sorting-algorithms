# Counting Sort Algorithm

def countingsort(array, high):
    m = high + 1
    count = [0] * m
    for a in array:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array[i] = a
            i += 1
    return array

array = [1, 2, 7, 3, 2, 1, 4, 2, 3, 2, 1, 8, 7, 9, 0]
high = max(array)
countingsort(array, high)
print(array)
