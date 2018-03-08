# -*- coding: utf-8 -*-

import random

"""

"""

def quicksort(a):
    if len(a)==0:
        return []
    print(0, len(a)-1)
    pivot = a[random.randint(0, len(a)-1)]
    less = []
    equal = []
    more = []
    for elem in a:
        if elem < pivot:
            less.append(elem)
        elif elem > pivot:
            more.append(elem)
        else :
            equal.append(elem)
        #else : now it's equal.
    result = quicksort(less) + equal + quicksort(more)
    return result

def swap(a, i1, i2):
    a[i1], a[i2] = a[i2], a[i1]
    return a

def quicksort_inplace2(a, left, right):
    #print(a)
    ind = partitian(a, left, right)
    if left < ind - 1:
        quicksort_inplace2(a, left, ind-1)
    if right > ind:
        quicksort_inplace2(a, ind, right)
#    if left<right: 
#        ind = partitian(a, left, right)
#        quicksort_inplace2(a, left, ind-1)
#        quicksort_inplace2(a, ind, right)
    return(a)


def partitian(a, left, right):
    if right-left < 1:
        return
    pivot = int((left+right)/2)
    while left<=right:#?
        while a[left]<a[pivot]:
            left+=1
        while a[right]>a[pivot]:
            right-=1
        if (left<=right): #why is this conditional necessary?
            a = swap(a, left, right)
            left+=1
            right-=1
    #print ("left is %d", left)
    return left


def quicksort_inplace(a):
    return quicksort_inplace2(a, 0, len(a)-1)

arrayy = [43, 5, 3, 7, 2, 9, 6, 7, 2, 8, 1]
print(quicksort_inplace(arrayy))
