# Put your name up here in a comment.
# Daniel W. Anner
# Tested with Python v3.7
#
# Then implement the insertion sort and merge sort
# algorithms in the functions that follow.  Also implement
# the is_sorted function to check if a list is sorted, and
# the random_list function to generate a list of random integers.
#
# Don't change the names of the functions or parameters.
# If you find it useful to have additional helper functions,
# you may do so.  Naming conventions in Python for helper functions
# is to begin with an _ at the start of the name.
#
# Note: You don't need the pass statements that I inserted, so you
# can delete them after you implement the functions.  I put them
# in temporarily so that you have valid syntax to start with.
#
# IMPORTANT: DO NOT have any print statements in the functions in this
# Python file (e.g., in the is_sorted, random_list, insertion_sort,
# merge_sort, and helper functions.  In general, you want to separate
# output from the computation.  You'll be outputting results
# (e.g., using print) in the if block at the bottom.
import random

def is_sorted(A) :
    """Returns True if A is sorted in non-decreasing order,
    and returns False if A is not sorted.

    Keyword arguments:
    A - a Python list.
    """
    iterator = iter(A)
    next(iterator)
    for x in A:
        try:
            if (x > next(iterator)):
                del iterator
                return False
        except StopIteration:
            pass

    del iterator
    return True


def random_list(length, low_value=0, high_value=100) :
    """Generates and returns a Python list of random integer values.
    The integers in the list are generated uniformly at random from
    the interval [low_value, high_value].

    Keyword arguments:
    length - the length of the list.
    low_value - the lower bound for the random integers.
    high_value - the upper bound for the random integers.
    """

    return [random.randint(low_value, high_value) for _ in range(length)]


def insertion_sort(A) :
    """Implementation of the insertion sort algorithm
    as specified on page 18 of the textbook.

    Keyword arguments:
    A - a Python list.
    """
    for index in range(1,len(A)):
        curVal = A[index]; pos = index

        while (pos > 0) and (A[pos-1] > curVal):
            A[pos] = A[pos-1]
            pos = pos-1

        A[pos]=curVal


def merge_sort(A) :
    """Implementation of the mergesort algorithm.

    Keyword arguments:
    A - a Python list.
    """

    ## This function is the top level call, and should simply
    ## call _merge_sort(A, p, r) passing the appropriate indices
    ## to sort the entire list.

    pass


def _merge_sort(A, p, r) :
    """The mergesort algorithm as specified on page 34 of the textbook.

    Keyword arguments:
    A - a Python list
    p - left most index of portion of list to sort
    r - the right most index of portion of list to sort
    """

    pass


def _merge(A, p, q, r) :
    """The merge operation for mergesort, as specified on page 31
    of the textbook.

    Keyword arguments:
    A - a Python list
    p - left most index of left sublist
    q - right most index of left sublist
    r - right most index of right sublist
    """

    pass



if __name__ == "__main__" :
    ## 2) Write a few lines of code to demonstrate that insertion_sort
    ##    correctly sorts a list (your random_list function will be useful
    ##    here).  Output (i.e., with print statements) the contents
    ##    odf the list before sorting, and then again after sorting).
    ## 3) Repeat 2 to demostrate that your merge_sort sorts correctly.

    ## Step 1
    unsortedArray = [2,5,3,6,4]
    sortedArray = [2,3,4,5,6]
    print("Unsorted Array %a: %s" % (unsortedArray, is_sorted(unsortedArray)))
    print("Sorted Array %a: %s" % (sortedArray, is_sorted(sortedArray)))

    ## Step 2
    print()
    randomList = random_list(12)
    print("List before insertion sorting: %s" % randomList)
    insertion_sort(randomList)
    print("List after insertion sort: %s" % randomList)

    pass
