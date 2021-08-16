from random import randint
from timeit import repeat


def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the 
    # algorithm function if it's not the built-in `sorted()`.

    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and th
    # minumum time it took to run
    print(times)
    print(f"Algorithm: {algorithm}. Mininum execution time: {min(times)}")



def bubble_sort(iarray):
    # worst case happens on sorted array
    arr_len = len(iarray)
    for i in range(arr_len - 1):
        for j in range(arr_len - i - 1):
            if iarray[j] > iarray[j+1]:
                iarray[j], iarray[j+1] = iarray[j+1], iarray[j]

    # a[i] is loop invariant 
    # The above function always runs O(n^2) time even if the array is sorted
    return iarray

def insertion_sort(iarray):
    # Worst case happens when array i sorted in reverse ORDER
    arr_len = len(iarray)
    for i in range(1, arr_len):
        # compare if less compare with previous
        # if position found insert and move others to right
        temp = iarray[i]
        j = i - 1
        while j >= 0 and iarray[j] > temp:
            iarray[j+1] = iarray[j]
            j-=1
        # When you finish shifting the elements, you can position
        # `temp` in its correct location
        array[j+1] = temp
    # Some Quicksort implementations even use insertion sort 
    # internally if the list is small enough to provide a faster overall implementation.
    return iarray
 
def selection_sort():
    pass

def merge(left, right):
    if len(left) < 1:
        return right
    
    if len(right) < 1:
        return left

    arr = []
    left_index = right_index = 0

    while len(arr) < len(left) + len(right):
        if left[left_index] <= right[right_index]:
            arr.append(left[left_index])
            left_index+=1
        else:
            arr.append(right[right_index])
            right_index+=1
            
        # If you reach the end of either array, then you can
        # add the remaining elements from the other array to
        # the result and break the loop
        if right_index == len(right):
            arr += left[left_index:]
            break

        if left_index == len(left):
            arr += right[right_index:]
            break

    return arr


def merge_sort(iarray):
    arr_len = len(iarray)
    if arr_len < 2:
        return iarray
    
    mid = arr_len // 2
    # we get a total runtime of O(n log2n).
    # Both bubble sort and insertion sort beat merge 
    # sort when sorting a ten-element list.
    return merge(left=merge_sort(iarray[:mid]), 
                right=merge_sort(iarray[mid:]))



def heap_sort():
    pass

def radix_sort():
    pass

def bucket_sort():
    pass

def quick_sort(iarray):
    if len(iarray) < 2:
        return iarray

    left , mid , right = [], [], []

    # find pivot
    pivot = iarray[randint(0, len(iarray) - 1)]
    #  In the best-case scenario, the algorithm consistently picks 
    #  the median element as the pivot. T
    #  worst case of O(n2) is when pivot is too small or too large
    for item in iarray:
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
        elif item == pivot:
            mid.append(item)

    return quick_sort(left) + mid + quick_sort(right)


ARRAY_LENGTH = 10000

if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    # Call the function using the name of the sorting algorithm
    # and the array you just created
    run_sorting_algorithm(algorithm="quick_sort", array=array)