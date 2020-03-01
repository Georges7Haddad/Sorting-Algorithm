"""This will draw a plot to see which sort
function is the best for multiple array sizes"""

import matplotlib.pyplot as plt
from runtime_quicksort_mergesort import mergesort_vs_quicksort, array_sizes


def draw_plot():
    """This is the function to draw the plot of each sort function"""

    plot = plt.figure("Sort")
    plot.text(0.40, 0.95, "Merge", color="blue")
    plot.text(0.50, 0.95, "Quick", color="green")
    plot.text(0.60, 0.95, "System", color="red")

    M, Q, S = mergesort_vs_quicksort()
    plt.plot(array_sizes, M, label='Merge')
    plt.plot(array_sizes, Q, label='Quick')
    plt.plot(array_sizes, S, label='System')


    plt.xlabel('Array Size')
    plt.ylabel('Time Needed')


    plt.legend()
    plt.show()

draw_plot()
