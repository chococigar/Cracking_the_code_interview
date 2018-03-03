# -*- coding: utf-8 -*-

"""
- Time : O(n)
- if in Java, need to use character array, and work from backwords for index consideration)
"""
s_input, n = input()
def replace_space(s):
    if n>len(s): #Edge case : need to consider this.
        return None
    return (s_input[:n].replace(" ", "%20"))

print(replace_space(s_input))
