# -*- coding: utf-8 -*-
"""
[1,3,2,4,1,3,1,4,5,2,2,1,4,2,2]

First attempt
BCR : O(n)
Time complexity : O(n^2)
#data structure : span!
"""
f = open("rainwater_input.txt", 'r')
#input always valid.

a_in = [int(x) for x in f.readline().strip()[1:-1].split(",")]

#[[][]]
span_a = [[] for _ in range(len(a_in))]

def rainarea(a): #First attempt
    #Put into span_a; was O(n^2).
    for i in range(len(a)):
        left_a = []
        for left in range(0, i):
            if a[left]>a[i]:
                left_a.append(a[left]) #appended value.
        span_a[i].append(left_a)
        right_a = []
        for right in range(i+1, len(a)):
            if a[right]>a[i]:
                right_a.append(a[right])#append value
        span_a[i].append(right_a)
    area = 0
    #Read from span_a.
    for i in range(1, len(span_a)-1): #exclude either side.
        if (len(span_a[i][0])>0 and len(span_a[i][1])>0): #if any of the two arrays are empty : don't consider.
            left_v = max(span_a[i][0]) #max value, index found.
            right_v = max(span_a[i][1]) #max value, index found.
            area += min(left_v, right_v) - a[i]
    return(area)
#print(rainarea(a_in))

"""
Second Attempt
Time complexity : O(n), because the computation part is max n.
This was Dynamic Programming :

Solution link for check : https://leetcode.com/problems/trapping-rain-water/solution/
"""

def rainarea2(a):
    #span
    span_max = -1 #init
    max_ind = []
    for i in range(1, len(a)-1): #exclude either side
        if a[i]>span_max:
            max_ind.append(i) #index appended. Index only grows.
            span_max = a[i]
    span_max = -1
    max_ind2 = []
    for i in range(len(a)-2, max_ind[-1], -1): #exclude either side
        if a[i]>span_max:
            max_ind2.append(i) #index appended. Index only grows.
            span_max = a[i]
    max_ind.extend(reversed(max_ind2))
    area = 0
    #between max indexes?; total n anyways.
    for i in range(len(max_ind)-1): #between each num's, exclude last.
        ceil = min(a[max_ind[i]], a[max_ind[i+1]]) #between two indices.
        for j in range(max_ind[i]+1, max_ind[i+1]): #exclude either end. if one well, passes.
            area += ceil - a[j]
    return(area)

print(rainarea2(a_in))
