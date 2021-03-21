# Bubble Sort Algorithm

def bubblesort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

nums = [5, 45, 8, 6, 7, 3, 2, 1, 0]
bubblesort(nums)
print("Sorted Array in asc order: ", nums)
