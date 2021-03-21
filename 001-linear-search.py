# Linear Search Algorithm

pos = 0
def linearsearch(list, n):
    i = 0
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1
    return False

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 6
if linearsearch(list, n):
    print("Found at position: ", pos)
else:
    print("Not Found in list")
