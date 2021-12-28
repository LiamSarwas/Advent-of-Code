import itertools
import math
from pathlib import Path

FILE_DIR = Path(__file__).parent

def is_won(board):
    for i in range(len(board)):
        if sum(board[i]) == -5:
            return True
        if sum([board[j][i] for j in range(len(board[0]))]) == -5:
            return True
    return False

def make_board_dict(board):
    db = {}
    for i in range(len(board)):
        for j in range(len(board[0])):
            db[board[i][j]] = (i, j)
    return db

def compute_score(board, num):
    score = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != -1:
                score += board[i][j]
    return score * num

def turns_to_win(nums, board):
    turns = 0
    db = make_board_dict(board)
    for num in nums:
        if num in db:
            i, j = db[num]
            board[i][j] = -1
        turns += 1
        if is_won(board):
            return compute_score(board, num), turns

def part_one(nums, boards):
    min_turns = len(nums) + 1
    final_score = 0
    for board in boards:
        score, turns = turns_to_win(nums, board)
        if turns < min_turns:
            min_turns = turns
            final_score = score
    return final_score

def part_two(nums, boards):
    max_turns = 0
    final_score = 0
    for board in boards:
        score, turns = turns_to_win(nums, board)
        if turns > max_turns:
            max_turns = turns
            final_score = score
    return final_score

def make_board(buffer):
    board = []
    for line in buffer:
        board.append([int(x) for x in line.split()])
    return board

if __name__ == "__main__":
    DATA = (FILE_DIR / "input" / "day4.txt").read_text().strip().split('\n')
    #DATA = (FILE_DIR / "input" / "day4test.txt").read_text().strip().split('\n')
    nums = [int(x) for x in DATA[0].split(',')]
    buffer = []
    boards = []
    for line in DATA[1:]:
        if line == '':
            if len(buffer) > 0:
                boards.append(make_board(buffer))
                buffer = []
        else:
            buffer.append(line)
    boards.append(make_board(buffer))
    print(part_one(nums, boards))
    buffer = []
    boards = []
    for line in DATA[1:]:
        if line == '':
            if len(buffer) > 0:
                boards.append(make_board(buffer))
                buffer = []
        else:
            buffer.append(line)
    boards.append(make_board(buffer))
    print(part_two(nums, boards))
