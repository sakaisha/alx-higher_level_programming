#!/usr/bin/python3
from sys import argv

# Check if the correct number of arguments is provided
l = len(argv)
if l != 2:
    print("Usage: nqueens N")
    exit(1)
# Check if the argument is a number
if not argv[1].isdigit():
    print("N must be a number")
    exit(1)
# Check if the number is at least 4
elif int(argv[1]) < 4:
    print("N must be at least 4")
    exit(1)


class Board:
    def __init__(self, size=0, array=0, next_arr=None):
        self.size = size
        self.array = array
        self.next_arr = None

    def set_queen(self, queen, array):
        """Locate Queen on the Board at an empty cell."""
        for y in range(self.size):
            for x in range(self.size):
                if array[y][x] == 0:
                    queen.pos_x = x
                    queen.pos_y = y
                    array[y][x] == 2  # Typo: should be assignment, not comparison
                    return array
        queen.pos_x = -1

    def next_queen(self, array):
        """Move the Queen to the next empty cell on the board."""
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
        """Reset the array to an array of 0s."""
        l = len(self.stat_arr)
        while l > 1:
            self.stat_arr.pop()
            l -= 1

    def return_comb(self):
        """Create a combination of Queen locations."""
        comb = []
        for y in range(self.size):
            for x in range(self.size):
                if self.stat_arr[-1][y][x] == 2:
                    comb += [[y, x]]
        return comb

    def check_2(self):
        """Return the status of the board when the queen is first located. 
        Fill all cells until the queen's location."""
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
        """Move the queen following queen rules."""
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
    """Handle moving the queen to empty cells and go back to the previous case
    when no more empty cells are available."""
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
            """ Go back to the previous status when
            no more cells are available for the Queen to move."""
            if len(status.stat_arr) > 2:
                status.stat_arr.pop()
                arr = status.stat_arr[-1]
                arr = board.next_queen(arr)
                i -= 1
            elif len(status.stat_arr) == 2:
                """Go to the first situation."""
                if status.check_2():
                    arr = status.check_2()
                    status.reset_arr()
                    i = 1
                else:
                    exit()
run(int(argv[1]))
