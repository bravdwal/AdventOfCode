import re
import numpy as np


def mark_matches(boards, matches, num):
    for idx, board in enumerate(boards):
        for idx2, row in enumerate(board):
            for idx3, n in enumerate(row):
                if n == num:
                    matches[idx][idx2][idx3] = 1


def find_winning_board(boards, matches):
    for idx, match in enumerate(matches):
        np_match = np.array(match)
        for row in np_match:
            if row.sum() == len(row):
                return boards[idx], match
        for col in np_match.transpose():
            if col.sum() == len(col):
                return boards[idx], match
    return None, None


with open('files/4.txt', 'r') as f:
    lines = f.readlines()

numbers = [int(num) for num in re.findall(r'(\d+)', lines[0])]

boards = []  # contains actual values of the boards
matches = []  # contains whether each position on the board has matched (1) or not yet (0)

# setup of boards and matches
for idx in range(2, len(lines), 6):
    board = []
    match = []
    for rowi in range(5):
        row = [int(num) for num in re.findall(r'(\d+)', lines[idx + rowi])]
        m = [0 for _ in row]
        board.append(row)
        match.append(m)
    boards.append(board)
    matches.append(match)

# play bingo until all boards have won
order_of_wins = []
num_boards = len(boards)
for num in numbers:
    mark_matches(boards, matches, num)
    while (ret := find_winning_board(boards, matches)) and ret[0] is not None:
        winning_board, winning_match = ret
        if winning_board is not None:
            order_of_wins.append((winning_board, winning_match, num))
            boards.remove(winning_board)
            matches.remove(winning_match)
            if len(order_of_wins) == num_boards:
                break
    else:
        continue
    break

print(np.multiply(np.array(order_of_wins[0][0]), np.abs(np.array(order_of_wins[0][1])-1)).sum()*order_of_wins[0][2])
print(np.multiply(np.array(order_of_wins[-1][0]), np.abs(np.array(order_of_wins[-1][1])-1)).sum()*order_of_wins[-1][2])
