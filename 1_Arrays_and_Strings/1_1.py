# -*- coding: utf-8 -*-

string_in = input()

"""
Sol 1
- Time : O(n)
- ASCII or Unicode String?
"""
def unique(s):
    sdict = dict.fromkeys(s, 0) #O(n)
    for char in s: #O(n)
        sdict[char]+=1
    if len(set(sdict.values()))!=1:
        return "Not unique."
    return "Unique."


"""
Sol 2
** ord() : code --> num; chr() : num-->code
- Time : O(n)
"""

def unique_constraint(s):
    slist = [False]*128 #O(nlog(n))
    for char in s: #O(n)
        if slist[ord(char)]==True:
            return "Not unique."
        else:
            slist[ord(char)]=True
    return "Unique."

"""
Sol 3
** Constraint : No more datastructures
** ord() : code --> num; chr() : num-->code
- Time : O(nlog(n))
"""

def unique_constraint2(s):
    s = sorted(s) #quicksort in-place
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            return "Not unique"
    return "Unique"


#print(unique(string_in))
print(unique_constraint2(string_in))
