from utils.read_input import read_input_as_matrix


def follow_beam(pos, dir):
    while (
        0 <= pos[0] < len(contraption[0])
        and 0 <= pos[1] < len(contraption)
        and (pos, dir) not in visited_tiles
    ):
        if pos == (5, 2):
            pass
        visited_tiles.add((pos, dir))
        tile = contraption[pos[1]][pos[0]]
        if tile == "/":
            dir = (-dir[1], -dir[0])
        elif tile == "\\":
            dir = (dir[1], dir[0])
        elif tile == "-" and dir[1] != 0:
            follow_beam(pos, (1, 0))
            follow_beam(pos, (-1, 0))
            return
        elif tile == "|" and dir[0] != 0:
            follow_beam(pos, (0, 1))
            follow_beam(pos, (0, -1))
            return
        pos = (pos[0] + dir[0], pos[1] + dir[1])


if __name__ == "__main__":
    contraption = read_input_as_matrix("2023/day_16/input.txt")
    visited_tiles = set()
    follow_beam((0, 0), (1, 0))
    print(len({p for p, d in visited_tiles}))
