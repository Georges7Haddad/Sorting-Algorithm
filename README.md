
# Sorting Algorithms

This is an implementation of two famous sorting algorithms with a simple test and a plot to compare them.

## QuickSort
QuickSort is a Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. This implementation always picks the last element as pivot. This partition(arr, first, last) iterates over the array to find the right place of the pivot. All values smaller than the pivot are at his left and the rest at his right.

## Merge Sort

Like QuickSort, Merge Sort is a  Divide and Conquer  algorithm. It takes an array and divides it in two halves, calls itself for the two halves and then merges the two sorted halves.  The merge(*left*, *right* ,*arr*) function go through the left and right subarrays and add their elements in **arr** while sorting them.




## Test
It's a simple test where we compare the output of Merge Sort and QuickSort against the system's sort function.


## Plot
  I plotted their runtime against the system's sort runtime.

![sort plot](https://user-images.githubusercontent.com/41213058/53041545-f1e6a080-348c-11e9-9a57-ddf08e990979.png)


