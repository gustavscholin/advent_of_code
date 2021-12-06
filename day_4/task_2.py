import numpy as np


def read_input(path: str):
    with open(path, "r") as f:
        return f.read().strip("\n").split("\n\n")


if __name__ == "__main__":
    bingo_input = read_input("day_4/input.txt")
    numbers = [int(i) for i in bingo_input[0].split(",")]
    boards = [[row.split() for row in board.split("\n")] for board in bingo_input[1:]]
    boards = np.array(boards).astype(int)

    winners = []
    row_col_len = boards.shape[-1]
    for called_nbr in numbers:
        boards[np.where(boards == called_nbr)] = -1
        for i, board in enumerate(boards):
            if i in winners:
                continue
            row_sum = np.sum(board, axis=1)
            col_sum = np.sum(board, axis=0)
            if -row_col_len in np.append(row_sum, col_sum):
                winners.append(i)
            if len(winners) == len(boards):
                print(called_nbr * np.sum(np.where(board == -1, 0, board)))
                break
        if len(winners) == len(boards):
            break
