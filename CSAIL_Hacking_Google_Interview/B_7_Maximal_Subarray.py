# -*- coding: utf-8 -*-

"""Q :
Given an array, describe an algorithm to identify the subarray with the maximum  sum.
For example, if the input is [1, ‐3, 5, ‐2, 9, ‐8, ‐6, 4], the output would be [5, ‐2,  9].

"subarray" with the maximum sum.

BCR : O(n)
Time Complexity :
Brute Force : O(n^2)

1 : 1, -2, 3, 1, 10, 2, -4, 0
-3 : -3, 2, 0, 9, 1, -7, -3
5 : 5, 3, 12, 4, -2, 2
-2 : -2, 7, -1, -7, -3
9 : 9, 1, -5, -1
-8 : -8, -14, -10
-6 : -6, -2
4 : 4

5, -2, 9 is max.

O(n^2).

[1, ‐3, 5, ‐2, 9, ‐8, ‐6, 4]
MINUS ? PLUS? MATTERS.
  - if minus && current val minus, don't cont?!?
  - if minus && current val not minus, continue.
Other Answer :
N : NEW / CONT / OLD
1 :   1 / - / -
-3 :  - / - / 1
5 :   5 / - / 1
-2 :  - / 3 / 5
9 :   9 / 12 / 5
-8 :  - / 4 / 12
-6 :  - / - / 12
4 :   - / - / 12
"""

def maxSubArraySum(a,size):

    maxint = 999999999
    max_so_far = -maxint - 1
    max_ending_here = 0

    for i in range(0, size):
        print(max_so_far, max_ending_here)
        print("%d is cur!" %(a[i]))
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


a = [1, -3, 5, -2, 9, -8, -6, 4]
size = len(a)
print(maxSubArraySum(a, size))
