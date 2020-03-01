""" This function tests merge_sort"""

import random


from sort.merge_sort import mergesort

array_sizes = [0, 1, 2, 3, 10, 100, 1000]
array=[]
for size in array_sizes:
    array = [random.uniform(-1000, 1000) for x in range(0, size)]
    array_copy = list(array)
    mergesort(array)
    array_copy.sort()
    assert array == array_copy, 'The sort function does not work'
    print 'The sort function works properly'
