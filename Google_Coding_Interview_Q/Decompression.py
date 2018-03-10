# -*- coding: utf-8 -*-

"""

"""
f = open("decompression_input.txt", 'r')
#input always valid.

#at beginning, until number ends or letter ends.

def string_one(s):
    if not s[0].isdigit():
        for i in range(len(s)):
            if s[i].isdigit() or (s[i]=='[' or ']'):
                s = ''.join(['1[', s[0:i], ']', s[i:] ]) # making it into 1's.
    return(s)


def decomp(text, start=0, num=1):
    #edgecase possible, assume all text in bracket.
    if len(text)==0:
        return ''
    result = text[start:]*num +


def decompress(s, text, times): #by default, should be number.
    #recursion, join, or multiply.
    #s = string_one(s)
    for letter in decomp(text):
        print(letter)


for i in range(times):
    i = start
    while i < len(text) and text[i] != ']':
        if text[i].islower():
            yield text[i]
        else:
            sub_times = 0
            while text[i].isdigit():
                sub_times = sub_times * 10 + int(text[i])
                i+=1
            i+=1
            for item in decomp(text):
                if isinstance(item, basestring):
                    yield item
                else:
                    i = item
            i +=1
if start > 0:
    yield i


for i in range(2):
    s_1 = f.readline().strip()
    print(decompress(s_1))
