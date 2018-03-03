# -*- coding: utf-8 -*-

"""
- Need to nullify rows without generating consecutive action
- BCR & time complexity : O(m*n)), need to touch all.
- If space efficiency is to be considered, make use of first rows/cols after extracting necessary information.
"""

s_input = input()

#just save the col's / row's with zero.
def zero_colrow(a_in):
    n = len(a_in)
    row = [False]*n
    col = [False]*n
    for i in range(n):
        for j in range(n):
            if a_in[i][j]==0:
                row[i] = True
                col[j] = True
    for i in range(n):
        if row[i]:
            a_in = a_in[:i] + [[0]*n] + a_in[i+1:]
    for j in range(n):
        if col[j]:
            a_in = [a_in[i][:j] + [0] + a_in[i][j+1:] for i in range(n)]
    return a_in

print(zero_colrow(s_input))
