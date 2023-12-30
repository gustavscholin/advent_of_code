from utils.read_input import read_input_as_matrix


def follow_beam(pos, dir, visited_tiles):
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
            visited_tiles = follow_beam(pos, (1, 0), visited_tiles)
            visited_tiles = follow_beam(pos, (-1, 0), visited_tiles)
            return visited_tiles
        elif tile == "|" and dir[0] != 0:
            visited_tiles = follow_beam(pos, (0, 1), visited_tiles)
            visited_tiles = follow_beam(pos, (0, -1), visited_tiles)
            return visited_tiles
        pos = (pos[0] + dir[0], pos[1] + dir[1])
    return visited_tiles


def energized_tiles(start_pos, start_dir):
    return len({p for p, _ in follow_beam(start_pos, start_dir, set())})


if __name__ == "__main__":
    contraption = read_input_as_matrix("2023/day_16/input.txt")

    all_energized_tiles = []
    for i in range(len(contraption[0])):
        all_energized_tiles.append(energized_tiles((i, 0), (0, 1)))
        all_energized_tiles.append(energized_tiles((i, len(contraption) - 1), (0, -1)))
    for i in range(len(contraption)):
        all_energized_tiles.append(energized_tiles((0, i), (1, 0)))
        all_energized_tiles.append(
            energized_tiles((len(contraption[0]) - 1, i), (-1, 0))
        )

    print(max(all_energized_tiles))
