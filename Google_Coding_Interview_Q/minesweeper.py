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
    #Assume bigger than 3*3; not nec.
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
        if (0<col and col<len(self.matrix) )
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
