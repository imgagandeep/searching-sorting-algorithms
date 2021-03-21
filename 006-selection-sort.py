# Selection Sort Algorithm

def selectionsort(nums):
    for i in range(len(nums)):
        minpos = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j
        nums[i], nums[minpos] = nums[minpos], nums[i]
        # print(nums)

nums = [5, 3, 8, 9, 7, 2, 0, 4, 1, 6]
print("Unsorted list: ", nums)
selectionsort(nums)
print("Sorted list:   ", nums)
