# -*- coding: utf-8 -*-

"""
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

print(is_palindrome(s_input))
