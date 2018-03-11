# -*- coding: utf-8 -*-

import itertools

"""
BCR : O(n*k) where n = length of side, k = total # of given array. (k>=n)
Time complexity :
Space complexity :

Edge cases
- Are all rows length n?
- need to check size of each word before v[r][c] == v[c][r]
- no need to check things twice.
- length 0 or 1 input.
- ***word more than once? (Wow, really need to clearify question before solving.)
"""

f = open("word_squares_input.txt", 'r')

a_in = f.readline().strip()[1:-1].split(", ")

k = len(a_in) #total elems in given array. No need for edges.

def is_word_square(a): #O(n^2)...obvious.
    local_n = len(a)
    for i in range(local_n): #0~n-1
        if len(a[i])!=local_n: #edge case
            return False
        for j in range(i+1, local_n): #i~n-1
            if a[i][j] != a[j][i]: #strings... treat as matrices. early false.
                return False
    return True

def find_word_square_n(a, n):
    result = []
    combinations = list(itertools.product(a, repeat=n))
    for comb in combinations:
        if is_word_square(comb):
            result.append(comb)
    return(result)

def meta(a):
    dict1 = {}
    for elem in a:
        if len(elem) in dict1:
            dict1[len(elem)].append(elem)
        else:
            dict1[len(elem)] = [elem] #check if better method exists.
    total_list = []
    for length in dict1: #length are lengths.
        total_list.extend(find_word_square_n(dict1[length], length))
    return total_list

print(meta(a_in))
