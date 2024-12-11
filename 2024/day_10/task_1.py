from utils.read_input import read_input_as_matrix


def find_trails(x, y):
    val = top_map[x][y]
    if val == 9:
        tops.add((x, y))
    for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= nx < len(top_map) and 0 <= ny < len(top_map):
            if top_map[nx][ny] == val + 1:
                find_trails(nx, ny)


if __name__ == "__main__":
    top_map = read_input_as_matrix("2024/day_10/input.txt", type="int")
    trail_heads = [
        (i, j)
        for i in range(len(top_map))
        for j in range(len(top_map[i]))
        if top_map[i][j] == 0
    ]
    tot_score = 0
    for tx, ty in trail_heads:
        tops = set()
        find_trails(tx, ty)
        tot_score += len(tops)
    print(tot_score)
