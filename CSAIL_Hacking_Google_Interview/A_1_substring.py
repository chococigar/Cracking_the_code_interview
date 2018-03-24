# -*- coding: utf-8 -*-

"""
Write a program to determine whether an input string x is a substring of another  input string y.
(For example, "bat" is a substring of "abate", but not of "beat".)
You may use any language you like.
(n : x (longer) length; m : y length)
"""

f = open("A_1_input.txt", 'r') #also, input is automatically taken as string.
x_in = f.readline().strip() #longer string
y_in = f.readline().strip() #inut string x



"""
BCR : O(n + m)
Time complexity : O(N)
Space complexity :

Edge case : x or y string length 0, len(x)<len(y)
Extreme case : x has all same letters, but very long,
"""
#Beauty of Robin Karp lies in that you "traverse through" n even when comparing the m.
#assuming that hashing a string to alphabet is O(n); for loop is same.
def substring(x, y):
    j = 0
    for i in range(len(x)-len(y)+1): #where in x should y be at
        if x[i]==y[j]:#also checking for 0.
            j+=1
            if j==len(y):
                print("substring")
                return
        else:
            j=0
    print("Not a substring")
    return

#substring(x_in, y_in)


"""
BCR : O(n + m)
Time complexity : O(n); faster because hash allows early detection...? Not entirely conviced, though.
Space complexity :

Edge case : x or y string length 0, len(x)<len(y)
Extreme case : x has all same letters, but very long,

Concepts to cover :
- Rabin Karp Algorithm
- hash

Most of the time your hash is going to compute in access at O(1). However, if it is a really bad hash where every value has the same hash, it will be O(n) worst case.
"""
def rabinkarp(x, y):
    y_hash = hash(y)
    for i in range(len(x)-len(y)+1): #where in x should y be at
        x_hash = hash(x[i:i+len(y)])
        if x_hash == y_hash:
            if x[i:i+len(y)]==y:
                print("substring")
                return
    print("Not a substring")
    return

rabinkarp(x_in, y_in)
