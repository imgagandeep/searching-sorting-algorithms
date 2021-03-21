# Insertion Sort Algorithm

def insertionsort(list):
    for index in range(0, len(list)):
        current_element = list[index]
        pos = index
        while current_element < list[pos - 1] and pos > 0:
            list[pos] = list[pos - 1]
            pos -= 1
        list[pos] = current_element

list = [26, 5, 3, 78, 35, 42, 29, 66, 49]
insertionsort(list)
print(list)
