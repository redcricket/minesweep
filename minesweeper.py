#!/bin/env python3

import random

class Cell():

    def __init__(self,i,j,field):
        self.i = i
        self.j = j
        self.exposed = False
        self.field = field
        self.value = self.calc_value()

    def display(self):
        if self.exposed:
            return self.value
        return '_'

    def expose(self):
        self.exposed = True

    def calc_value(self):
        i = self.i
        j = self.j
        f = self.field

        if self.field[i][j] == '*':
            return '*' 
        v=0
        try:
            if f[i-1][j-1] == '*' and i != 0 and j != 0:
                v += 1
        except:
            pass
        try:
            if f[i-1][j] == '*' and i != 0:
                v += 1
        except:
            pass
        try:
            if f[i-1][j+1] == '*' and i != 0:
                v += 1
        except:
            pass
        try:
            if f[i][j-1] == '*' and j != 0:
                v += 1
        except:
            pass
        try:
            if f[i][j+1] == '*':
                v += 1
        except:
            pass
        try:
            if f[i+1][j-1] == '*' and j != 0:
                v += 1
        except:
            pass
        try:
            if f[i+1][j] == '*':
                v += 1
        except:
            pass
        try:
            if f[i+1][j+1] == '*':
                v += 1
        except:
            pass
        return str(v)


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def main():
    size = int(input('Enter size of field: '))

    # 1/10th of cells will be mines.
    mines = (size**2)//size

    try:
        mines = int(input('Enter number of mines [default=%s]: ' % mines))
    except:
        mines = (size**2)//size

    # Make an one dimensional list of size square.
    field_1d = [' ']*(size**2)

    # Stick the mines into the list.
    for m in range(mines):
        field_1d[m] = '*'

    # Randomly place the mines.
    random.shuffle(field_1d)

    # Make a 2D list out of the 1D list.
    field = [r for r in chunks(field_1d,size)]

    # Display it.
    for row in field:
        print(row)

    for i in range(size):
        for j in range(size):
            print(field[i][j], end='|')
        print("")

    board_1d = []
    for i in range(size):
        for j in range(size):
            board_1d.append(Cell(i,j,field))

    board = [r for r in chunks(board_1d,size)]

    def display(board):
        for i in range(size):
            for j in range(size):
                print(board[i][j].display(), end='|')
            print("")

    def win(board):
        unexposed = 0
        for i in range(size):
            for j in range(size):
                if board[i][j].exposed == False:
                    unexposed += 1

        if unexposed == mines:
            print('WINNER!!!!')
            return True

        return False

    gameover = False

    while not gameover:
        display(board)
        J = int(input('Enter I: '))
        I = int(input('Enter J: '))
        c = board[I][J]
        print("I=%d J=%d c(i,j) -> (%d,%d)" % (I,J,c.i,c.j))
        c.expose()
        if c.value == '*':
           print("BOOM!")
           gameover = True
        else:
           gameover = win(board)

    display(board)


if __name__ == '__main__':
    main()
