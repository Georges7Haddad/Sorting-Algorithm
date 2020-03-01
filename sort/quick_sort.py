"""Quick Sort """

# Quick sort
def partition(arr, first, last):
    """ Divides the array into 2 subarrays
    param arr: array to be sorted
    param first: first index of array
    param last: last index of arrays
    return: index of pivot """

    i = (first-1)
    pivot = arr[last]
    for j in range(first, last):
        if   arr[j] <= pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    arr[i+1], arr[last] = arr[last], arr[i+1]
    return i+1

def quick_sort(arr, first_index=0, last_index=None):
    """ Sorts a given array
    param arr: array to be sorted
    param first_index: first index of array
    param last_index: last index of arrays """

    if first_index < last_index:
        part = partition(arr, first_index, last_index)
        quick_sort(arr, first_index, part-1)
        quick_sort(arr, part+1, last_index)
def quicksort(arr):
    """This function allow you
    to pass only the array to sort as an argument
    param arr: array to be sorted"""
    quick_sort(arr, 0, len(arr)-1)
