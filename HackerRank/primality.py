# -*- coding: utf-8 -*-
"""
Time complexity problem : "Primality"
Question from https://www.hackerrank.com/challenges/ctci-big-o/problem
Implemented code's complexity :
- Time : O(log(n))
"""

f = open("primality_input.txt", 'r')
def is_prime(n):
    if n<2: #edge case
        return False
    sqrt = int(n**0.5) #(n**(1/2)) is 1, thus use decimal.
    for i in range(2, sqrt+1):
        if (n%i==0):
            return(False)
    return(True)

p = int(f.readline())
for i in range(p):
    n = int(f.readline().strip())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")
