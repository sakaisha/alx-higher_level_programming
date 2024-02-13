#!/usr/bin/python3
from sys import argv

l = len(argv)
if l != 2:
    print("Usage: nqueens N")
    exit(1)
if not argv[1].isdigit():
    print("N must be a number")
    exit(1)
elif int(argv[1]) < 4:
    print("N must be at least 4")
    exit(1)


class Board:
    def __init__(self, size=0, array=0, next_arr=None):
        self.size = size
        self.array = array
        self.next_arr = None

    def set_queen(self, queen, array):
        """locate Queen on Board at empty cell"""
        for y in range(self.size):
            for x in range(self.size):
                if array[y][x] == 0:
                    queen.pos_x = x
                    queen.pos_y = y
                    array[y][x] == 2
                    return array
        queen.pos_x = -1

    def next_queen(self, array):
        """move the Queen to next empty cell on board"""
        for y in range(self.size):
            for x in range(self.size):
                if array[y][x] == 0:
                    array[y][x] = 1
                    return array


class Status:
    def __init__(self, size, stat_arr=[]):
        self.stat_arr = stat_arr
        self.size = size

    def reset_arr(self):
        """reset the arr to arr of 0"""
        l = len(self.stat_arr)
        while l > 1:
            self.stat_arr.pop()
            l -= 1

    def return_comb(self):
        """create a combination of Queen location"""
        comb = []
        for y in range(self.size):
            for x in range(self.size):
                if self.stat_arr[-1][y][x] == 2:
                    comb += [[y, x]]
        return comb

    def check_2(self):
        """return the status of board when queen is
        first located. Fill the all cell until queen
        location"""
        ret_arr = [[0 for x in range(self.size)] for y in range(self.size)]
        for x in range(self.size - 1):
            ret_arr[0][x] = 1
            if self.stat_arr[1][0][x] == 2:
                return ret_arr
        return False


class Queen:
    def __init__(self, size=0, pos_x=0, pos_y=0):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size = size

    def move_queen(self, arr):
        """move the queen follow queen rules"""
        array = [sub_arr[:] for sub_arr in arr]
        for i in range(self.size):
            array[self.pos_y][i] = 1
            array[i][self.pos_x] = 1
            if self.pos_y + i < self.size and self.pos_x + i < self.size:
                array[self.pos_y + i][self.pos_x + i] = 1
            if self.pos_y - i >= 0 and self.pos_x - i >= 0:
                array[self.pos_y - i][self.pos_x - i] = 1
            if self.pos_y + i < self.size and self.pos_x - i >= 0:
                array[self.pos_y + i][self.pos_x - i] = 1
            if self.pos_y - i >= 0 and self.pos_x + i < self.size:
                array[self.pos_y - i][self.pos_x + i] = 1
        array[self.pos_y][self.pos_x] = 2
        return array


def run(size):
    """hand moving for queen to empty cell and go back to previous case
    when no more empty cell"""
    arr = [[0 for x in range(size)] for y in range(size)]
    board = Board(size, arr)
    status = Status(size, [arr])
    queen = Queen(size)
    i = 1
    while True:
        arr = board.set_queen(queen, arr)
        if queen.pos_x != -1:
            arr = queen.move_queen(arr)
            status.stat_arr.append(arr)
            i += 1
            if i == size + 1:
                print(status.return_comb())
        elif queen.pos_x == -1:
            """ go back to previouse status when
            no more cell for Queen moving
            """
            if len(status.stat_arr) > 2:
                status.stat_arr.pop()
                arr = status.stat_arr[-1]
                arr = board.next_queen(arr)
                i -= 1
            elif len(status.stat_arr) == 2:
                """go to first situation """
                if status.check_2():
                    arr = status.check_2()
                    status.reset_arr()
                    i = 1
                else:
                    exit()
run(int(argv[1]))
