# Binary Search Algorithm

pos = 0
def binarysearch(list, n):
    # l -> lower bound
    l = 0

    # u -> upper bound
    u = len(list) - 1

    while l <= u:
        # mid -> mid value
        mid = (l + u) // 2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False

list = [4,7,8,12,45,99,102,702,10987,56666]
n = 99
if binarysearch(list, n):
    print("Found at position: ", pos+1)
else:
    print("Not Found in list")
