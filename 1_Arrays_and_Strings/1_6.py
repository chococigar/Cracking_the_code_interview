# -*- coding: utf-8 -*-

"""
Sol 1 : Bad
String compression, without losing original string.
- Time : O(n + m^2) due to string concat quadratic
"""
s_input = input()
def compress(s):
    c = s[0] #current char
    val = 0 #current num
    newstr = ""
    for i in range(len(s_input)):
        if s[i]==c:
            val+=1
        elif i<len(s_input)-1: #for next to come. but if last string, dif story.
            newstr += c + str(val)
            val = 1
            c = s[i]
        else:
            newstr += s[i] + "1"
    if len(newstr)>=len(s):
        return s
    return newstr

"""
Sol 2 : Considers string concatration time.
String compression, without losing original string.
- Time : O(n)
"""
def compress2(s):
    c = s[0] #current char
    val = 0 #current num
    newstr = ""
    for i in range(len(s_input)):
        if s[i]==c:
            val+=1
        elif i<len(s_input)-1: #for next to come. but if last string, dif story.
            newstr = ''.join(c, str(val)) # O(n)
            val = 1
            c = s[i]
        else:
            newstr = ''.join(s[i], "1")
    if len(newstr)>=len(s):
        return s
    return newstr

print(compress(s_input))
