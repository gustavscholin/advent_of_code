def compare_lines(l1, l2):
    return sum([c1 != c2 for c1, c2 in zip(l1, l2)])


def get_reflection_idx(lines):
    for i in range(1, len(lines)):
        smudge_cnt = 0
        line_diff = compare_lines(lines[i - 1], lines[i])
        if line_diff in (0, 1):
            smudge_cnt += line_diff
            m = i + 1
            n = i - 2
            while n >= 0 and m < len(lines):
                smudge_cnt += compare_lines(lines[n], lines[m])
                if smudge_cnt > 1:
                    break
                n -= 1
                m += 1
            if smudge_cnt == 1:
                return i
    return 0


if __name__ == "__main__":
    with open("2023/day_13/input.txt") as f:
        patterns = f.read().strip("\n").split("\n\n")

    x = 0
    for pattern in patterns:
        rows = pattern.splitlines()
        cols = ["".join(r[i] for r in rows) for i in range(len(rows[0]))]
        x += get_reflection_idx(rows) * 100
        x += get_reflection_idx(cols)

    print(x)
