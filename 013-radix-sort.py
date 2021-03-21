# Radix Sort Algorithm


# get number of digits in largest item
def __get_num_digits(array):
    m = 0
    for item in array:
        m = max(item, m)
    return len(str(m))

from functools import reduce
def __flatten(array):
    return reduce(lambda x, y : x + y, array)

def radix(array, num_digits):
    for digit in range(0, num_digits):
        bucket = [[] for i in range(10)]
        for item in array:
            # num is the bucket number that the item will be put into
            num = item // 10 ** (digit) % 10
            bucket[num].append(item)
        array = __flatten(bucket)
    return array

def main():
    array = [55, 45, 3, 289, 213, 1, 288, 53, 2, 0, 7865, 2]
    
    # find longest integer in our list
    num_digits = __get_num_digits(array)
    array = radix(array, num_digits)
    print(array)
main()
