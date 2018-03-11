# -*- coding: utf-8 -*-

print('s'.islower())
print('s'.isdigit())
print('S'.isupper())



A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(A[1][4]==None)


"""
https://stackoverflow.com/questions/6670828/find-all-consecutive-sub-sequences-of-length-n-in-a-sequence
x = [0,1,7,3,4,5,10]
n = 3
zip(*(x[i:] for i in range(n)))
[(0, 1, 7), (1, 7, 3), (7, 3, 4), (3, 4, 5), (4, 5, 10)]
"""
