# -*- coding: utf-8 -*-

"""
Q
You're given an unsorted array of integers where every integer appears exactly  twice, except for one integer which appears only once.  Write an algorithm (in a  language of your choice) that finds the integer that appears only once.

BCR : O(n)
Time Complexity : O(n) ; 2 O(n)
Space Complexity : dict O(n)
Cannot premature end, as need to see till end to find single.
"""

f = open("B_2_input.txt", "r")
arrayy = [int(x) for x in f.readline().strip()[1:-1].split(", ")]

def oddman(a):
    d = dict.fromkeys(a, 0)
    for elem in a:
        d[elem] += 1
    for key in d:
        if d[key]==1:
            print(key)
            break

def oddman2(a):
    d = dict.fromkeys(a, 0)
    summ = 0
    for elem in a:
        if d[elem]==0:
            d[elem]=1
            summ+=elem
        elif d[elem]==1:
            summ-=elem
    return(summ)

def oddman3(a):
    pass
    #bitwise xor is possible;
    

print(oddman2(arrayy))
