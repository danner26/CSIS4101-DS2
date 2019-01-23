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
    iterator = iter(A) # create a new iterator
    next(iterator) # progress the iterator so the for loop with compare position 0 and 1
    for x in A: # loop through all objects in the array
        try: # we need the try loop to catch the end where there is nothing else to compare
            if (x > next(iterator)): # if the current index value is greater than the next index value to the right
                del iterator # deconstruct the iterator
                return False # return false as it is not sorted
        except StopIteration: # catch the end case where you cannot compare anything else (the last position)
            pass # let the function end

    del iterator # deconstruct the iterator
    return True # return true as it is sorted


def random_list(length, low_value=0, high_value=100) :
    """Generates and returns a Python list of random integer values.
    The integers in the list are generated uniformly at random from
    the interval [low_value, high_value].

    Keyword arguments:
    length - the length of the list.
    low_value - the lower bound for the random integers.
    high_value - the upper bound for the random integers.
    """
    # Single line that returns an array of length with random integers between low_value and high_value
    return [random.randint(low_value, high_value) for _ in range(length)]


def insertion_sort(A) :
    """Implementation of the insertion sort algorithm
    as specified on page 18 of the textbook.

    Keyword arguments:
    A - a Python list.
    """
    for i in range(1,len(A)): #loop through entire array using i as the position
        curVal = A[i]; pos = i; #initiate variables

        while (pos > 0) and (A[pos-1] > curVal): #while the positions is gt 0 and the previous position is gt the current value
            A[pos] = A[pos-1] #swap the variables
            pos = pos-1 #move back to compare again

        A[pos]=curVal


def merge_sort(A) :
    """Implementation of the mergesort algorithm.

    Keyword arguments:
    A - a Python list.
    """

    if len(A) == 0 or len(A) == 1: #if the array is empty or only contains one item
        return #return and do not execute the merge sort
    _merge_sort(A, 0, len(A)-1) #call the _merge_sort function and pass the list, left most index, and right most index



def _merge_sort(A, p, r) :
    """The mergesort algorithm as specified on page 34 of the textbook.

    Keyword arguments:
    A - a Python list
    p - left most index of portion of list to sort
    r - the right most index of portion of list to sort
    """
    if p < r: #check if list is greater than 1
        mid = math.floor((p + r)/2) #split the list in half
        #merge left and right halves
        _merge_sort(A, p, mid) #left half
        _merge_sort(A, mid + 1, r) #right half
        _merge(A, p, mid, r) #merge function to join the left and right halves together


def _merge(A, p, q, r) :
    """The merge operation for mergesort, as specified on page 31
    of the textbook.

    Keyword arguments:
    A - a Python list
    p - left most index of left sublist
    q - right most index of left sublist
    r - right most index of right sublist
    """

    left = A[p:q + 1]; right = A[q + 1:r + 1]; #assign left and right halves of the list
    left.append(1000000); right.append(1000000); #append a large so we know when to stop
    i = j = 0 #create Pointers i and j

    for k in range(p, r + 1): #for loop to compare left and right halves of the list
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1



if __name__ == "__main__" :
    ## Step 1
    unsortedArray = [2,5,3,6,4] #init an unsorted array to test the is_sorted function
    sortedArray = [2,3,4,5,6] #init a sorted array to test the is_sorted function
    print("Unsorted Array %a: %s" % (unsortedArray, is_sorted(unsortedArray))) #is_sorted returns False
    print("Sorted Array %a: %s" % (sortedArray, is_sorted(sortedArray))) #is_sorted returns True

    ## Step 2
    print() #blank space for output
    print() #blank space for output
    randomList = random_list(random.randint(2, 20)) #init new randomList for insertion_sort
    print("List before insertion sorting: %s" % randomList) #print randomList before insertion_sort'ing
    insertion_sort(randomList) #insertion_sort the randomList
    print("List after insertion sort: %s" % randomList) #print randomList after insertion_sort'ing
    if is_sorted(randomList): #check if the list is sorted
        print("The list is sorted!") #expected print result
    else:
        print("The list is not sorted.") #this should not be printed

    # Step 3
    print() #blank space for output
    print() #blank space for output
    randomList = random_list(random.randint(5, 20)) #recycle randomList for merge_sort
    print("List before merge sorting: %s" % randomList) #print randomList before merge_sort'ing
    merge_sort(randomList) #merge_sort the randomList
    print("List after merge sorting: %s" % randomList) #print randomList after merge_sort'ing
    if is_sorted(randomList): #check if the list is sorted
        print("The list is sorted!") #expected print result
    else:
        print("The list is not sorted."); #this should not be printed
