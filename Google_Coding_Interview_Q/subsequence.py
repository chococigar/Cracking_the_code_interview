# -*- coding: utf-8 -*-
#
"""
Time complexity : O(len(s) * len(d array))
Space complexity : 1+1

"""
from itertools import compress

f = open("subsequence_input.txt", 'r')
#input always valid.

s_in = f.readline().strip()[1:-1]
d_in = f.readline().strip()[2:-2].split('", "')


def subsequence(s, w): # s is longer, w is test word. #O(len(s))
    w_ind = 0
    for i in range(len(s)):
        if w_ind==len(w):
            return True
        elif s[i] == w[w_ind]:
            w_ind+=1
        else:
            pass
    else:
        return False

#print(max(list(compress(d_in, [subsequence(s_in, elem) for elem in d_in])), key=len))


"""
Time complexity : O(len(s) * len(d array))
Space complexity : 1+1

"""
#mapping.
def word2dic(w): #O(len(s))
    dict1 = dict.fromkeys(s, [])
    for i in range(len(s)): #O(S)
        dict1[s[i]].append(i)
    return dict1

def subsequence2(dic, w):
    ind = 0
    print(dic)
    for i in range(len(w)):
        if w[i] in dic:
            ind = min(filter(lambda x: x>ind, dic[w[i]])) #right ind = prev ind.
        else:
            return False
    return True

print(max(list(compress(d_in, [subsequence2(s_in, elem) for elem in d_in])), key=len))


#print(subsequence2(word2dic(s_in), d_in))
#but if S is long and dictionary is short, very bad.
