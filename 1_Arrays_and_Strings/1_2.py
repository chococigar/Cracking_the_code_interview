# -*- coding: utf-8 -*-

"""
- Time : O(n)

"""
f = open("1_2_input.txt", 'r')
s_1 = f.readline()
s_2 = f.readline()

dict1 = dict.fromkeys(s_1, 0)
for char in s_1:
    dict1[char]+=1
dict2 = dict.fromkeys(s_2, 0)
for char in s_2:
    dict2[char]+=1

if dict1 != dict2 :
    print("Not permutations.")
else:
    print("Permutations.")
