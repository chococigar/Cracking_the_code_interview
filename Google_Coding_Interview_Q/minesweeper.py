# -*- coding: utf-8 -*-
"""

"""
f = open("minesweeper_input.txt", 'r')
matrix_in = []
for line in f:
    #matrix_in.append([int(x) for x in line.strip().split("  ")])
    matrix_in.append(line.strip().split("  "))


game_over=0
class Minefield(object):
    #Assume bigger than 2*2; not nec.
    def __init__(self):
        self.matrix = []
        self.masked = []
        self.bombnum = []
    def setmine(self, matrix):
        self.matrix = matrix
    def setmask(self, matrix):
        self.masked = [['-' for i in range(len(self.matrix[0]))] for j in range(len(self.matrix))]
    def orig_show(self):
        for row in self.matrix:
            print(row)
    def masked_show(self):
        for row in self.masked:
            print(row)
    def init_game(self):
        self.setmask(self.matrix)
    def uncover(self, row, col):
        if self.matrix[row][col]=='9':
            #BOMB!
            print("THERE WAS A BOMB. GAME OVER!")
            global game_over
            game_over = 1
        elif self.matrix[row][col]=='0':
            self.uncover_zeros(row, col)
        else:
            self.masked[row][col] = self.matrix[row][col]
    def uncover_zeros(self, row, col):
        self.masked[row][col] = self.matrix[row][col]
        #adjacent.
        left =0
        right=0
        top=0
        bottom=0
        if col==0:
            left = 1
        if col==len(self.matrix[0]) - 1:
            right = 1
        if row==0:
            top = 1
        if row==len(self.matrix)-1:
            bottom = 1
        print(right, left, top, bottom)
        if right == 0:
            if self.masked[row][col+1]=='0':
                self.uncover_zeros(row, col+1) #uncover_zeros(self, row, col) doesn't work; global name error
                print("1")
        if left == 0:
            if self.masked[row][col-1]=='0':
                self.uncover_zeros(row, col+1)
                print("2")
        if top == 0:
            if self.masked[row-1][col]=='0':
                self.uncover_zeros(row-1, col)
                print("3")
        if bottom == 0:
            if self.masked[row+1][col]=='0':
                self.uncover_zeros(row+1, col)
        if (right==0 and top==0):
            if self.masked[row-1][col+1]=='0':
                self.uncover_zeros(row-1, col+1)
        if (left==0 and top==0):
            if self.masked[row-1][col-1] == '0':
                self.uncover_zeros(row-1, col-1)
        if (left==0 and bottom==0):
            if self.masked[row+1][col-1] == '0':
                self.uncover_zeros(row+1, col-1)
        if (right==0 and bottom==0):
            if self.masked[row+1][col+1] == '0':
                self.uncover_zeros(row+1, col+1)
    def play(self):
        global game_over
        while not game_over:
            self.masked_show()
            (row, col) = input("ENTER THE ROW(%d~%d) AND COLUMN(%d~%d) TO UNCOVER\n" %(0, len(self.matrix)-1, 0, len(self.matrix[0])-1))
            self.uncover(row, col)





mine = Minefield()
mine.setmine(matrix_in)
mine.init_game()
mine.play()
