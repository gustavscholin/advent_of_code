if __name__ == "__main__":
    with open("2024/day_9/input.txt", "r") as f:
        disk_map = f.read().strip()

    expanded_map = []
    for idx, val in enumerate(disk_map):
        if idx % 2 == 0:
            expanded_map += [idx // 2 for _ in range(int(val))]
        else:
            expanded_map += ["." for _ in range(int(val))]

    empty_indices = [i for i, val in enumerate(expanded_map) if val == "."]
    vals = [(i, val) for i, val in enumerate(expanded_map) if val != "."]

    for i, val in reversed(vals):
        empty_idx = expanded_map.index(".")
        expanded_map[empty_idx] = val
        expanded_map[i] = "."
        if all(rem_val == "." for rem_val in expanded_map[empty_idx + 1 :]):
            break

    print(sum([i * val for i, val in enumerate(expanded_map) if val != "."]))
