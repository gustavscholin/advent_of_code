from utils.read_input import read_input

if __name__ == "__main__":
    rows = read_input("2023/day_14/input.txt")
    cols = ["".join(r[i] for r in rows) for i in range(len(rows[0]))]
    total_load = 0
    for col in cols:
        stop_idx = -1
        for i in range(len(col)):
            if col[i] == "#":
                stop_idx = i
            elif col[i] == "O":
                stop_idx += 1
                total_load += len(col) - stop_idx
    print(total_load)
