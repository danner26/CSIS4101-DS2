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
import random, math

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
    for i in range(1,len(A)):
        curVal = A[i]; pos = i

        while (pos > 0) and (A[pos-1] > curVal):
            A[pos] = A[pos-1]
            pos = pos-1

        A[pos]=curVal


def merge_sort(A) :
    """Implementation of the mergesort algorithm.

    Keyword arguments:
    A - a Python list.
    """

    if len(A) == 0 or len(A) == 1:
        pass
    _merge_sort(A, 0, len(A)-1)



def _merge_sort(A, p, r) :
    """The mergesort algorithm as specified on page 34 of the textbook.

    Keyword arguments:
    A - a Python list
    p - left most index of portion of list to sort
    r - the right most index of portion of list to sort
    """
    if p < r: # check if list is greater than 1
        # Split the List in half
        mid = math.floor((p + r)/2)
        # Merge Left and Right side
        # Left side
        _merge_sort(A, p, mid)
        # Right side
        _merge_sort(A, mid + 1, r)
        # Merge function to join Left and Right side together
        _merge(A, p, mid, r)


def _merge(A, p, q, r) :
    """The merge operation for mergesort, as specified on page 31
    of the textbook.

    Keyword arguments:
    A - a Python list
    p - left most index of left sublist
    q - right most index of left sublist
    r - right most index of right sublist
    """
    # Assign left and right side of List
    left = A[p:q + 1]
    right = A[q + 1:r + 1]
    # Append a number really big so program knows when to stop
    left.append(99999999)
    right.append(99999999)
    # Create Pointers i & j
    i = j = 0
    # For loop to compare left and right side of List
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1



if __name__ == "__main__" :
    ## Step 1
    unsortedArray = [2,5,3,6,4]
    sortedArray = [2,3,4,5,6]
    print("Unsorted Array %a: %s" % (unsortedArray, is_sorted(unsortedArray)))
    print("Sorted Array %a: %s" % (sortedArray, is_sorted(sortedArray)))

    ## Step 2
    print()
    print()
    randomList = random_list(random.randint(1, 20))
    print("List before insertion sorting: %s" % randomList)
    insertion_sort(randomList)
    print("List after insertion sort: %s" % randomList)
    if is_sorted(randomList):
        print("The list is sorted!")
    else:
        print("The list is not sorted.");

    # Step 3
    print()
    print()
    randomList = random_list(random.randint(5, 20))
    print("List before merge sorting: %s" % randomList)
    merge_sort(randomList)
    print("List after merge sorting: %s" % randomList)
    if is_sorted(randomList):
        print("The list is sorted!")
    else:
        print("The list is not sorted.");

    pass
