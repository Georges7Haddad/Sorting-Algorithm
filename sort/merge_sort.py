""" Merge Sort """


# Merge
def merge(left, right, arr):
    """ Merge for merging many arrays into one sorted
    param left: left subarray
    param right: right subarray
    param arr: array where final values are stored """

    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i = i+1
            k = k+1
        else:
            arr[k] = right[j]
            j = j+1
            k = k+1

    while i < len(left):

        arr[k] = left[i]
        i = i+1
        k = k+1
    while j < len(right):

        arr[k] = right[j]
        j = j+1
        k = k+1
def mergesort(arr):
    """ Sorting a given array
    param arr: array to be sorted """

    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        mergesort(left)
        mergesort(right)
        merge(left, right, arr)
