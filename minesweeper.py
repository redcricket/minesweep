#!/bin/env python3

import random
import time


class Cell:

    def __init__(self, i, j, field):
        self.i = i
        self.j = j
        self.exposed = False
        self.field = field
        self.size = len(field[0])
        self.value = self.calc_value(self.i, self.j)

    def display(self):
        if self.exposed:
            if self.value == '0':
                return ' '
            return self.value
        # You can get the funny charaters here:
        # http://www.fileformat.info/info/charset/UTF-16/list.htm?start=1024
        return '_'

    def expose(self, board):
        i = self.i
        j = self.j
        size = self.size
        self.exposed = True
        if int(self.value) == 0:
            if i > 0 and j > 0:
                v = int(self.calc_value(i - 1, j - 1))
                if v == 0 and not board[i - 1][j - 1].exposed:
                    board[i - 1][j - 1].expose(board)
                if v > 0 and not board[i - 1][j - 1].exposed:
                    board[i - 1][j - 1].exposed = True
            if i > 0:
                v = int(self.calc_value(i - 1, j))
                if v == 0 and not board[i - 1][j].exposed:
                    board[i - 1][j].expose(board)
                if v > 0 and not board[i - 1][j].exposed:
                    board[i - 1][j].exposed = True
            if i > 0 and j < size - 1:
                v = int(self.calc_value(i - 1, j + 1))
                if v == 0 and not board[i - 1][j + 1].exposed:
                    board[i - 1][j + 1].expose(board)
                if v > 0 and not board[i - 1][j + 1].exposed:
                    board[i - 1][j + 1].exposed = True

            if j > 0:
                v = int(self.calc_value(i, j - 1))
                if v == 0 and not board[i][j - 1].exposed:
                    board[i][j - 1].expose(board)
                if v > 0 and not board[i][j - 1].exposed:
                    board[i][j - 1].exposed = True
            if j < size - 1:
                v = int(self.calc_value(i, j + 1))
                if v == 0 and not board[i][j + 1].exposed:
                    board[i][j + 1].expose(board)
                if v > 0 and not board[i][j + 1].exposed:
                    board[i][j + 1].exposed = True

            if i < size - 1 and j > 0:
                v = int(self.calc_value(i + 1, j - 1))
                if v == 0 and not board[i + 1][j - 1].exposed:
                    board[i + 1][j - 1].expose(board)
                if v > 0 and not board[i + 1][j - 1].exposed:
                    board[i + 1][j - 1].exposed = True
            if i < size - 1:
                v = int(self.calc_value(i + 1, j))
                if v == 0 and not board[i + 1][j].exposed:
                    board[i + 1][j].expose(board)
                if v > 0 and not board[i + 1][j].exposed:
                    board[i + 1][j].exposed = True
            if i < size - 1 and j < size - 1:
                v = int(self.calc_value(i + 1, j + 1))
                if v == 0 and not board[i + 1][j + 1].exposed:
                    board[i + 1][j + 1].expose(board)
                if v > 0 and not board[i + 1][j + 1].exposed:
                    board[i + 1][j + 1].exposed = True

    def calc_value(self, i, j):
        f = self.field

        try:
            if self.field[i][j] == '*':
                return '*'
        except:
            pass
        v = 0
        try:
            if f[i - 1][j - 1] == '*' and i != 0 and j != 0:
                v += 1
        except:
            pass
        try:
            if f[i - 1][j] == '*' and i != 0:
                v += 1
        except:
            pass
        try:
            if f[i - 1][j + 1] == '*' and i != 0:
                v += 1
        except:
            pass
        try:
            if f[i][j - 1] == '*' and j != 0:
                v += 1
        except:
            pass
        try:
            if f[i][j + 1] == '*':
                v += 1
        except:
            pass
        try:
            if f[i + 1][j - 1] == '*' and j != 0:
                v += 1
        except:
            pass
        try:
            if f[i + 1][j] == '*':
                v += 1
        except:
            pass
        try:
            if f[i + 1][j + 1] == '*':
                v += 1
        except:
            pass
        return str(v)


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def expose_all(board):
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            board[i][j].exposed = True


def cheat(b):
    size = len(b[0])
    for i in range(size):
        for j in range(size):
            if b[i][j].value == '*':
                print('*', end='|')
            else:
                print(' ', end='|')
        print("")


def display(board):
    size = len(board)
    for i in range(size):
        if i == 0:
            for ii in range(size):
                if ii == 0:
                    print(" ", end=' ')
                print(ii % 10, end=' ')
            print("")
        for j in range(size):
            if j == 0:
                print("%s " % (i % 10), end='')
            print(board[i][j].display(), end='|')
            if j == size - 1:
                print(" %s" % (i % size), end='')
        print("")
    for ii in range(size):
        if ii == 0:
            print(" ", end=' ')
        print(ii % 10, end=' ')
    print("")


def win(board, mines):
    size = len(board)
    unexposed = 0
    for i in range(size):
        for j in range(size):
            if not board[i][j].exposed:
                unexposed += 1

    if unexposed == mines:
        print('WINNER!!!!')
        return True
    return False


def main():
    size = int(input('Enter size of field: '))

    # 1/10th of cells will be mines.
    mines = (size ** 2) // size

    try:
        mines = int(input('Enter number of mines [default=%s]: ' % mines))
    except:
        mines = (size ** 2) // size
        pass

    # Make an one dimensional list of size square.
    field_1d = [' '] * (size ** 2)

    # Stick the mines into the list.
    for m in range(mines):
        field_1d[m] = '*'

    # Randomly place the mines.
    random.shuffle(field_1d)

    # Make a 2D list out of the 1D list.
    field = [r for r in chunks(field_1d, size)]

    # board_1d = []
    # for i in range(size):
    #    for j in range(size):
    #        board_1d.append(Cell(i, j, field))
    # board_1d = [Cell(i, j, field) for i in range(size) for j in range(size)]
    # board = [r for r in chunks(board_1d, size)]
    board = [r for r in chunks([Cell(i, j, field) for i in range(size) for j in range(size)], size)]
    game_over = False

    while not game_over:
        display(board)
        asking = True
        i = j = 0
        while asking:
            try:
                i, j = [int(i) for i in input('Enter row,col: ').split(',')]
                if size > i >= 0 and size > j >= 0:
                    asking = False
            except Exception as ex:
                if ex.args[0] == "invalid literal for int() with base 10: 'c'":
                    cheat(board)
                pass
        c = board[i][j]
        if c.value == '*':
            print("BOOM!")
            game_over = True
            c.exposed = True
            display(board)
            time.sleep(3)
            print('')
            expose_all(board)
        else:
            c.expose(board)
            game_over = win(board, mines)

    display(board)


if __name__ == '__main__':
    main()
