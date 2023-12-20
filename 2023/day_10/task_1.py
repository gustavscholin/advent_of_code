import numpy as np

from utils.read_input import read_input_as_matrix

north = np.array([-1, 0])
south = np.array([1, 0])
east = np.array([0, 1])
west = np.array([0, -1])


def get_start_pipe(idx):
    connecting_west = pipes[*(idx + west)] in ("-", "F", "L")
    connecting_east = pipes[*(idx + east)] in ("-", "7", "J")
    connecting_north = pipes[*(idx + north)] in ("|", "7", "F")
    connecting_south = pipes[*(idx + south)] in ("|", "J", "L")
    if connecting_north and connecting_south:
        return "|"
    elif connecting_west and connecting_east:
        return "-"
    elif connecting_north and connecting_east:
        return "L"
    elif connecting_west and connecting_north:
        return "J"
    elif connecting_west and connecting_south:
        return "7"
    elif connecting_east and connecting_south:
        return "F"


def get_next_pipe(cur_idx, cur_pipe, prev_idx):
    if cur_pipe == "|":
        return (
            cur_idx + north if np.all(prev_idx == cur_idx + south) else cur_idx + south
        )
    elif cur_pipe == "-":
        return cur_idx + east if np.all(prev_idx == cur_idx + west) else cur_idx + west
    elif cur_pipe == "L":
        return (
            cur_idx + east if np.all(prev_idx == cur_idx + north) else cur_idx + north
        )
    elif cur_pipe == "J":
        return (
            cur_idx + west if np.all(prev_idx == cur_idx + north) else cur_idx + north
        )
    elif cur_pipe == "7":
        return (
            cur_idx + west if np.all(prev_idx == cur_idx + south) else cur_idx + south
        )
    elif cur_pipe == "F":
        return (
            cur_idx + east if np.all(prev_idx == cur_idx + south) else cur_idx + south
        )


if __name__ == "__main__":
    pipes = np.array(read_input_as_matrix("2023/day_10/input.txt"))
    idx = np.argwhere(pipes == "S")[0]
    pipe = get_start_pipe(idx)
    loop = [(idx, pipe)]
    while pipe != "S":
        idx = get_next_pipe(idx, pipe, None if pipes[*idx] == "S" else loop[-2][0])
        pipe = pipes[*idx]
        loop.append((idx, pipe))
    print(int((len(loop) - 1) / 2))
