"""Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all the interval lengths. Overlapping intervals should only be counted once.

Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

>>> sum_of_intervals([
        [1,2],
        [6, 10],
        [11, 15]
        ]); // => 9

>>> sum_of_intervals([
        [1,4],
        [7, 10],
        [3, 5]
        ]); // => 7

>>> sum_of_intervals([
        [1,5],
        [10, 20],
        [1, 6],
        [16, 19],
        [5, 11]
        ]); // => 19
"""

def sum_of_intervals(intervals):
    s = 0                           # sum of intervals lengths
    top = float("-inf")             # "top" is the upper bound of the previous interval, initialized as negative infinity

    for a, b in sorted(intervals):  # by sorting the list, overlaps will happen in the next element, if not, then there is a gap in intervals (no need to check every interval with each other)
        if top < a:                 # if the upper bound of the previous interval is smaller than the lower bound of the current interval, then there is a gap
            top = a                 # "top" is set to the lower bound of the current interval

        if top < b:                 # if the upper bound of the previous interval is smaller than the upper bound of the current interval, then they are a valid interval (ignores a sub set of a previous interval, e.g.[(1,10), (3,6)] the (3,6) interval will be ignored)
            s = s + b - top         # total sum equals current sum + (upper bound - lower bound)
            top = b                 # by updating top to the upper bound of the current set, if a overlap happens with the next interval, the overlapped part will not be counted
    return s                        # return the total sum at the end

print(sum_of_intervals([(1, 5), (1, 5), (7, 11)]))
