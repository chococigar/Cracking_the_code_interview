# -*- coding: utf-8 -*-

"""
- Time : O(n^2)
- Outer layer to inside.
- cf : this implementation was confusing. Should have started with sheer example.
"""
s_input = input()

def rotate(matrix):
    n = len(matrix)
    for layer in range(int(n/2)+1): #layer index.
        for i in range(layer, n-layer-1):#index
            temp = matrix[layer][i]
            matrix[layer][i] = matrix[n-i-1][layer] #col to row
            matrix[n-i-1][layer] = matrix[n-layer-1][n-i-1] #row to col
            matrix[n-layer-1][n-i-1] = matrix[i][n-layer-1]
            matrix[i][n-layer-1] = temp
    return(matrix)

print(rotate(s_input))
