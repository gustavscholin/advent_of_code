from utils.read_input import read_input


def rotate_right(lines):
    return ["".join(l[i] for l in reversed(lines)) for i in range(len(lines[0]))]


if __name__ == "__main__":
    platform = read_input("2023/day_14/input.txt")
    states = {}
    total_cycles = 1_000_000_000
    cycles = 0
    period_found = False

    platform = rotate_right(rotate_right(platform))
    states["".join(platform)] = cycles

    while cycles < total_cycles:
        for _ in range(4):
            platform = rotate_right(platform)
            new_platform = []
            for row in platform:
                new_row = [c for c in row]
                stop_idx = -1
                for i in range(len(row)):
                    if row[i] == "#":
                        stop_idx = i
                    elif row[i] == "O":
                        stop_idx += 1
                        if i != stop_idx:
                            del new_row[i]
                            new_row.insert(stop_idx, "O")
                new_platform.append("".join(new_row))
            platform = new_platform

        cycles += 1

        if not period_found:
            if "".join(platform) in states:
                period_start = states["".join(platform)]
                period = cycles - period_start
                cycles = total_cycles - (total_cycles - period_start) % period
                period_found = True
            else:
                states["".join(platform)] = cycles

    platform = rotate_right(platform)
    print(
        sum(
            sum([i for i, c in enumerate(reversed(row), 1) if c == "O"])
            for row in platform
        )
    )
