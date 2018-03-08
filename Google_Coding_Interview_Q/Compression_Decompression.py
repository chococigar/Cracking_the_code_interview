# -*- coding: utf-8 -*-

"""

"""
f = open("cd_input.txt", 'r')
#input always valid.

s_in = f.readline()

def cd_string(s):
    #divide into parts...don't know about this part.
    #maybe just join later.
    count = 0
    beg = s.find('[')
    if (s[0].isdigit()): #initial is digit.
        for i in range(1, len(s)):
            if s[i]=='[':
                count+=1
            elif s[i]==']':
                count-=1
            if count==0:
                end = i #] index.
                break
    current = s[beg:]*int(s[0:beg])
    #ab is another matter.

    result = ''.join(current, cd_string(s[end+1:])) #after end brack
    #br_open = [i for i, char in enumerate(s) if char=='[']
    #br_close = [i for i, char in enumerate(s) if char==']']


    #do recursion for each parts.


    #join the parts
    result = ''.join([seq])
