# -*- coding: utf-8 -*-

string_in = input()

"""
- Time : O(n)
"""
def unique(s):
    sdict = dict.fromkeys(s, 0) #O(n)
    for char in s: #O(n)
        sdict[char]+=1
    if len(set(sdict.values()))!=1:
        return "Not unique."
    return "Unique."


"""
**Constraint : No more datastructures
- Time : O(n(log(n)))
"""
def unique_constraint(s):
    slist = sorted(list(s)) #O(nlog(n))
    for i in range(len(slist)-1): #O(n)
        if slist[i]==slist[i+1]:
            return "Not unique."
    return "Unique."

#print(unique(string_in))
print(unique_constraint(string_in))
