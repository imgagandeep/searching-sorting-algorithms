# Merge Sort Algorithm

def mergesort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        mergesort(left)
        mergesort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1

list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergesort(list)
print(list)
