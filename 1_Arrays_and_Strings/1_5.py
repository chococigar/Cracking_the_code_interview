# -*- coding: utf-8 -*-

"""
Given a string, determine if it is a palindrome.
- Time : O(n)
"""
f = open("1_5_input.txt", 'r')
n = int(f.readline())
def one_edit(s1, s2):
    if s1==s2:
        return True
    for i in range(len(s1)):
        if s1[:i] + s2[i] + s1[i:] == s2: #insertion
            return True
        elif s1[:i] + s1[i+1:] == s2: #deletion
            return True
        elif s1[:i] + s2[i] + s1[i+1:] == s2: #replacement
            return True
    return False

#need to strip the last newline, python syntax.
for i in range(n):
    s_1, s_2 = f.readline().strip().split(", ")
    print(one_edit(s_1, s_2))
