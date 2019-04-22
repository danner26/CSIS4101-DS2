# Programming Assignment 5
#
# Don't rename any functions, although feel free to implement any helper functions
# you find useful.
#
# 1) Implement the naive_string_matcher function as specified in its docstring.
#    This is a variation of the algorithm on page 988 of the textbook.
#    Read the docstring below carefully so you know what I've changed.
#
# 2) Implement the function print_results below.
#
# 3) Implement the p_naive_string_matcher function as specified in its docstring.
#
# 4) In the time_results function below, implement any code needed to compare the runtimes
#    of the sequential and parallel version on string of varying lengths and with varying number of matches.
#    You will need to figure out how to generate strings of varying lengths.  And with a varying number of matches.
#    This is not as hard as it might seem at first.  Recall that you can use the multiplication operator * with
#    a string and an integer as follows:  "abc" * 5 will evaluate to "abcabcabcabcabc"
#
# 5) Answer the following questions here in a comment based on #4:
#
#    Q1: After running time_results, fill in this table in this comment for whatever P and T lengths
#        you tried (make sure you vary lengths from short to longer:
#        T-length   P-Length   Sequential   Parallel
#        Text Length         String Length              Sequential Time         Parallel Time
#          988                     1                        0.005058            1.9547728
#          6273                    3                  0.04049329999999984       1.9401059000000003
#          17535                   4                  0.08526839999999991       2.0561283
#          400080                  8                   2.027870499999999        3.2754221
#          2100042                14                   22.553352600000004       10.027697799999999
#
#    Q2: How do the times (of both versions) vary by string length?  If T is held constant, and pattern P length varied, how does
#        that affect runtime?  If P length is held constant, and text T length varied, how does that affect runtimes?
#
#        As the text length grew, the runtime increased at the same rate. AS the pattern length grew, the runtime also increated
#        at the same rate. The runtimes increase of the pattern was lesser than the text increate.
#
#    Q3: At what lengths of P and/or T is the sequential version faster?
#    When the text and patters were smaller, the sequential was smaller. When the lengths got larger, specificall string length 4, parallelism was faster.
#
#    Q4: At what lengths of P and/or T is the parallel version faster?
#    As the text and patterns got larger, parallel time became faster.
#
#    Q5: Are the results consistent with the speedup you computed in Problem Set 4?  If not, what do you think caused
#        the inconsistency with the theoretical speedup?
#        The results are different from prblem set 4, as the costs time to add the processor should be in linear speedup times.


# These are imports you will likely need.  Feel free to add any other imports that are necessary.
from multiprocessing import Process, Pool
import multiprocessing  # as mp
import timeit
from functools import partial


def time_results() :
    """Write any code needed to compare the timing of the sequential and parallel versions
    with a variety of string lengths.  Have this print a table of the following form:

    T-length   P-Length   SequentialTime  ParallelTime
    """
    def parallel_Time(T, P):
        """Uses timeit to time the parallel run time of any T and P. Returns the time. Note: The number is set to 10 which is not the most accurate however my computer started chugging after increasing passed 10 """
        time = timeit.timeit(lambda: p_naive_string_matcher(T, P), number=10)
        return time

    def sequential_Time(T, P):
        time = timeit.timeit(lambda: naive_string_matcher(T, P), number=10)
        return time

    def increase_T(T, amount):
        copyOfT = T
        for i in range(amount):
            copyOfT += T * 5
        return copyOfT

    if __name__ == "__main__":
        attempt1_increased = increase_T(attempt1_txt, 5)
        attempt1_sequential = sequential_Time(attempt1_increased, attempt1_ptrn)
        attempt1_parallel = parallel_Time(attempt1_increased, attempt1_ptrn)

        attempt2_increased = increase_T(attempt2_txt, 10)
        attempt2_sequential = sequential_Time(attempt2_increased, attempt2_ptrn)
        attempt2_parallel = parallel_Time(attempt2_increased, attempt2_ptrn)

        attempt3_increased = increase_T(attempt3_txt, 100)
        attempt3_sequential = sequential_Time(attempt3_increased, attempt3_ptrn)
        attempt3_parallel = parallel_Time(attempt3_increased, attempt3_ptrn)

        attempt4_increased = increase_T(attempt4_txt, 1000)
        attempt4_sequential = sequential_Time(attempt4_increased, attempt4_ptrn)
        attempt4_parallel = parallel_Time(attempt4_increased, attempt4_ptrn)

        attempt5_increased = increase_T(attempt5_txt, 10000)
        attempt5_sequential = sequential_Time(attempt5_increased, attempt5_ptrn)
        attempt5_parallel = parallel_Time(attempt5_increased, attempt5_ptrn)

        print('{:^15} {:^25} {:^30} {:^10}'.format("Text Length", "String Length", "Sequential Time", "Parallel Time"))
        print('{:^15} {:^25} {:^30} {:^10}'.format(len(attempt1_increased), len(attempt1_ptrn), attempt1_sequential, attempt1_parallel))
        print('{:^15} {:^25} {:^30} {:^10}'.format(len(attempt2_increased), len(attempt2_ptrn), attempt2_sequential, attempt2_parallel))
        print('{:^15} {:^25} {:^30} {:^10}'.format(len(attempt3_increased), len(attempt3_ptrn), attempt3_sequential, attempt3_parallel))
        print('{:^15} {:^25} {:^30} {:^10}'.format(len(attempt4_increased), len(attempt4_ptrn), attempt4_sequential, attempt4_parallel))
        print('{:^15} {:^25} {:^30} {:^10}'.format(len(attempt5_increased), len(attempt5_ptrn), attempt5_sequential, attempt5_parallel))

def print_results(L) :
    """Prints the list of indices for the matches."""
    print(L)

def naive_string_matcher(T, P) :
    """Naive string matcher algorithm from textbook page 988.

    Slight variation of the naive string matcher algorithm from
    textbook page 988.  Specifically, the textbook version prints the
    results.  This python function does not print the results.
    Instead, it generates and returns a list of the indices at the start
    of each match.  For example, if T="abcabcabc" and P="def", this function
    will return the empty list [] since the pattern doesn't appear in T.
    For that same T, if the pattern P="abc", then this function will return
    the list [0, 3, 6] since the pattern appears 3 times, beginning on indices
    0, 3, and 6.

    Keyword arguments:
    T -- the text string to search for patterns.
    P -- the pattern string.
    """
    p = len(P)
    t = len(T)
    list = []
    for i in range((t - p) + 1):
        for j in range(p):
            if T[i + j] != P[j]:
                break
        if j == p - 1:
            list.append(i)
    # print_results(list)
    return list


def p_naive_string_matcher(T, P) :
    """Parallel naive string matcher algorithm from Problem Set 4.

    This function implements the parallel naive string matcher algorithm that you specified in
    Problem Set 4.  You may assume in your implementation that there are 4 processor cores.
    If you want to write this more generally, you may add a parameter to the function for number
    of processes.  If you do, don't change the order of the existing parameters, and your new parameters
    must follow, and must have default values such that if the only parameters I pass are T and P, that
    you default to 4 processes.

    Like the sequential implementation from step 1 of assignment, this function should not
    print results.  Instead, have it return a list of the indices where the matches begin.
    For example, if T="abcabcabc" and P="def", this function
    will return the empty list [] since the pattern doesn't appear in T.
    For that same T, if the pattern P="abc", then this function will return
    the list [0, 3, 6] since the pattern appears 3 times, beginning on indices
    0, 3, and 6.

    You must use Process objects (or a Pool of processes) from the multiprocessing module and not Threads from threading because
    in the next step of the assignment, you're going to investigate performance relative to the sequential
    implementation.  And due to Python's global interpreter lock, you won't see any gain if you use threads.
    I recommend using a Pool, and its map method.

    Hints related to using Pool.map: 1) You'll need a function of one argument
    to pass to Pool.map, and a list of the values for that argument.  This list can be a list of the starting indices
    to check for matches (i.e., the indices from the outer loop of the naive string matcher).  The one argument function's
    one argument can be the index to check, and can then check if a match starts at that index. 2) But wait, wouldn't that
    function need 3 arguments, T, P, and the index? Yes. Start by creating a helper function with those 3 arguments, with
    index as the last argument.  Your helper can simply return a boolean indicating whether it is a match.
    Then, look up the documentation for a function named partial in the Python module functools.
    partial takes as arguments a function and some of the arguments for it, and returns to you a function where those arguments
    will be passed by default.  E.g., you can pass your helper function, and T and P to partial, and it will return to you a
    function that you simply need to pass index (the remaining argument).  3) Your last hint.  If you follow hints 1 and 2, you'll
    end up with a list of booleans, true if that corresponding index was a match and false otherwise.  The final step would
    be to use that to generate what this string matcher is actually supposed to return.

    Keyword arguments:
    T -- the text string to search for patterns.
    P -- the pattern string.
    """
    p = len(P)
    t = len(T)
    initList = []
    checkList = []
    matches = []
    multipool = multiprocessing.Pool()

    for i in range(t - p + 1):
        checkList.append(i)

    help = partial(helper, T, P, p)

    for i in multipool.map(help, checkList):
        if i is not None:
            matches.append(i)

    initList.append(matches)
    return matches

def helper(T, P, p, i):
    if P == T[i:i + p]:
        return i

# Pattern size 1
attempt1_txt = "dddddddddddddddddddddddddddddddddddddd"
attempt1_ptrn = "d"
# Pattern size 3
attempt2_txt = "HelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloByeHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHello"
attempt2_ptrn = "Bye"
# Pattern size 4 (Large Text size)
attempt3_txt = "WelcomeToTheShowWeAreHappyToHaveYou"
attempt3_ptrn = "Show"
# Pattern size 8
attempt4_txt = "QuickFoxQuickFoxQuickFoxQuickFoxQuickFoxQuickFoxQuickFoxQuickFoxQuickFoxQuickFox"
attempt4_ptrn = "QuickFox"
# Pattern size 14
attempt5_txt = "==============--------------=============="
attempt5_ptrn = "=============="

time_results()
