# Shell Sort Algorithm

def shellsort(list):
    interval = len(list) // 2
    while interval > 0:
        for index in range(interval, len(list)):
            current_element = list[index]
            pos = index
            while pos >= interval and current_element < list[pos - interval]:
                list[pos] = list[pos - interval]
                pos -= interval
            list[pos] = current_element
        interval = interval // 2

list = [9, 8, 3, 7, 5, 6, 4, 1]
shellsort(list)
print(list)
