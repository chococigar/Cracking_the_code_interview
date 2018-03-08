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
