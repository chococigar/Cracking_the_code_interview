# -*- coding: utf-8 -*-

"""
Sol 1
Given a string, determine if it is a palindrome.
- Time : O(n)
- Maximum one odd character.
"""
s_input = input().replace(" ", "")

def is_palindrome(s):
    sdict = dict.fromkeys(s, 0)
    for char in s:
        sdict[char] +=1
    value = 0
    for elem in sdict.values():
        value += (elem%2)
    return value<=1


"""
Sol 2
#instead of use a int, try to use boolean variales.
#Benefit : no redundancy.
- Time : O(n)
"""

def is_palindrome2(s):
    sdict = dict.fromkeys(s, 0)
    for char in s:
        sdict[char] +=1
    odd_found = False
    for elem in sdict.values(): #Odd more than 2 times?
        if (elem%2==1):
            if odd_found:
                return False
            else:
                odd_found=True
    return True


"""
Sol 3
#instead of use a int, try to use boolean variales.
- Time : O(n)
If using java, easy bit manipulation for only collecting odd / even information is possible.
"""


print(is_palindrome2(s_input))
