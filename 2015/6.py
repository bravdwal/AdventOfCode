import numpy as np
import re


class Grid:
    width: int
    height: int
    grid: list[list]

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[False for _ in range(width)] for _ in range(height)]

    def turn_on(self, bottom_left, top_right):
        for x in range(bottom_left[0], top_right[0]+1):
            for y in range(bottom_left[1], top_right[1]+1):
                self.grid[x][y] = True

    def turn_off(self, bottom_left, top_right):
        for x in range(bottom_left[0], top_right[0]+1):
            for y in range(bottom_left[1], top_right[1]+1):
                self.grid[x][y] = False

    def toggle(self, bottom_left, top_right):
        for x in range(bottom_left[0], top_right[0]+1):
            for y in range(bottom_left[1], top_right[1]+1):
                self.grid[x][y] = not self.grid[x][y]


class Grid2:
    width: int
    height: int
    grid: list[list]

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def turn_on(self, bottom_left, top_right):
        for x in range(bottom_left[0], top_right[0]+1):
            for y in range(bottom_left[1], top_right[1]+1):
                self.grid[x][y] += 1

    def turn_off(self, bottom_left, top_right):
        for x in range(bottom_left[0], top_right[0]+1):
            for y in range(bottom_left[1], top_right[1]+1):
                self.grid[x][y] = b if (b := self.grid[x][y]-1) > 0 else 0

    def toggle(self, bottom_left, top_right):
        for x in range(bottom_left[0], top_right[0]+1):
            for y in range(bottom_left[1], top_right[1]+1):
                self.grid[x][y] += 2


def follow_instructions(grid, instructions):
    for instruction in instructions:
        m = re.search(r'^(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)$', instruction)
        attr = getattr(grid, m.group(1).replace(' ', '_'))
        bottom_left, top_right = (int(m.group(2)), int(m.group(3))), (int(m.group(4)), int(m.group(5)))
        attr(bottom_left, top_right)


def day6(Grid, instructions):
    grid = Grid(1000, 1000)
    follow_instructions(grid, instructions)
    return sum(np.reshape(grid.grid, (-1,)))


with open('files/6.txt', 'r') as f:
    instructions = f.readlines()

# print('Check for ex1')
# print('-------------')
# print(day6(Grid, ['turn on 0,0 through 999,999\n']))
# print(day6(Grid, ['turn on 0,0 through 999,999\n', 'toggle 0,0 through 999,0\n']))
# print(day6(Grid, ['turn on 0,0 through 999,999\n', 'turn off 499,499 through 500,500\n']), '\n')

# print('Result of ex1')
# print('-------------')
# print(day6(Grid, instructions), '\n')

print('Check for ex2')
print('-------------')
print(day6(Grid2, ['turn on 0,0 through 0,0\n']))
print(day6(Grid2, ['toggle 0,0 through 999,999\n']))
print(day6(Grid2, ['toggle 0,0 through 999,999\n', 'turn off 0,0 through 999,999\n']), '\n')

print('Result of ex2')
print('-------------')
print(day6(Grid2, instructions), '\n')
