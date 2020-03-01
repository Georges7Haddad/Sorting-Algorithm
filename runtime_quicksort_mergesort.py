""" Give an array of size n
    sorts array using
    quick sort or merge sort
    and gives the time needed"""

import random
import time
from sort.quick_sort import quicksort
from sort.merge_sort import mergesort

array_sizes = [0, 1, 2, 3, 10, 100, 10000]
# Testing
def mergesort_vs_quicksort():
    """ Tests merge sort and quick sort
    param size: size of array """
    runtime_merge = []
    runtime_quick = []
    runtime_system = []

    for size in array_sizes:

        array = [random.uniform(-1000, 1000) for x in range(0, size)]
        array_copy = list(array)
        array_copy2 = list(array)

        start_mergesort = time.time()
        mergesort(array)
        end_mergesort = time.time()

        quicksort(array_copy)
        end_quicksort = time.time()

        array_copy2.sort()
        end_systemsort = time.time()

        runtime_mergesort = end_mergesort - start_mergesort
        runtime_quicksort = end_quicksort - end_mergesort
        runtime_systemsort = end_systemsort - end_quicksort

        runtime_merge.append(runtime_mergesort)
        runtime_quick.append(runtime_quicksort)
        runtime_system.append(runtime_systemsort)
        if __name__ == '__main__':
            print ('Time for sorting using Merge Sort', runtime_mergesort)
            print ('Time for sorting using Quick Sort', runtime_quicksort)
            print ('Time for sorting using System Sort', runtime_systemsort)

    return runtime_merge, runtime_quick, runtime_system
