# -*- coding: utf-8 -*-

"""
Given 2 strings, determine if one is a substring of another.
"""
f = open("1_9_input.txt", 'r') #also, input is automatically taken as string.
s_1 = f.readline().strip()
s_2 = f.readline().strip()


"""
Sol 1
Given 2 strings, determine if one is a substring of another.
- Time : O(n)
# No recursions allowed. (Only one call to function.)
"""
def is_rotation(s1, s2):
    if len(s1)!= len(s2):
        return False
    for i in range(len(s1)):
        if ''.join([s1[i:], s1[:i]])==s2:
            return True
    return False

"""
Sol2
if rotation, means in 2 concatenated original string there will be one.
"""
def is_rotation2(s1, s2):
    if len(s1)!= len(s2):
        return False
    s1s1 = ''.join([s1, s1])
    return is_substring(s2, s1s1)

#is substring, with O(n+m)= O(n) time complexity
def is_substring(s, b): #b : longer string
    for i in range(len(b)-len(s)+1):
        print(s, b[i:i+len(s)])
        if s==b[i:i+len(s)]:
            return True
    return False

print(is_rotation2(s_1, s_2))
