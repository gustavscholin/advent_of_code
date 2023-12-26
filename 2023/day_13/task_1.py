def get_reflection_idx(lines):
    for i in range(1, len(lines)):
        if lines[i - 1] == lines[i]:
            m = i + 1
            n = i - 2
            is_reflection = True
            while n >= 0 and m < len(lines):
                if lines[n] != lines[m]:
                    is_reflection = False
                    break
                n -= 1
                m += 1
            if is_reflection:
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
