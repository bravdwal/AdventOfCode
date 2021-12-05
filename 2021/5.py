import re
import numpy as np


def create_grid(lines):
    max_x = 0
    max_y = 0
    vents = []
    for line in lines:
        m = re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line)
        x1, y1, x2, y2 = [int(g) for g in m.groups()]
        vents.append(((x1, y1), (x2, y2)))

        mx = max([x1, x2])
        my = max([y1, y2])

        if mx > max_x:
            max_x = mx
        if my > max_y:
            max_y = my

    return np.zeros((max_x+1, max_y+1), dtype=np.int32), vents


def mark_vents(grid, vents, diagonal):
    grid = grid.copy()
    for vent in vents:
        (x1, y1), (x2, y2) = vent
        if x1 == x2:
            s = sorted([y1, y2])
            for idx in range(s[0], s[1]+1):
                grid[idx][x1] += 1  # counter intuitive, but grid[row_idx][col_idx]
        elif y1 == y2:
            s = sorted([x1, x2])
            for idx in range(s[0], s[1]+1):
                grid[y1][idx] += 1  # counter intuitive, but grid[row_idx][col_idx]
        elif diagonal:
            tx = 1 if x2 > x1 else -1
            ty = 1 if y2 > y1 else -1
            cx = x1
            cy = y1
            while cx != x2 and cy != y2:
                grid[cy][cx] += 1
                cx += tx
                cy += ty
            grid[cy][cx] += 1
    return grid


with open('files/5.txt', 'r') as f:
    lines = f.readlines()

grid, vents = create_grid(lines)

# 1
marked_grid = mark_vents(grid, vents, False)
print(len(np.where(marked_grid > 1)[0]))

# 2
marked_grid = mark_vents(grid, vents, True)
print(len(np.where(marked_grid > 1)[0]))
