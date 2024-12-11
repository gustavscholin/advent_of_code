def get_first_empty_slot(slots, size):
    for i, slot in enumerate(slots):
        if slot[0] == "." and slot[1] >= size:
            return i
    return None


if __name__ == "__main__":
    with open("2024/day_9/input.txt", "r") as f:
        disk_map = f.read().strip()

    slots = []
    for idx, val in enumerate(disk_map):
        if idx % 2 == 0:
            slots.append((idx // 2, int(val)))
        else:
            slots.append((".", int(val)))

    i = len(slots) - 1
    while i >= 0:
        val, size = slots[i]
        if val == ".":
            i -= 1
            continue
        empty_idx = get_first_empty_slot(slots[:i], size)
        if empty_idx is None:
            i -= 1
            continue
        slots[empty_idx] = (".", slots[empty_idx][1] - size)
        slots.insert(empty_idx, slots.pop(i))
        slots.insert(i + 1, (".", size))

    checksum = 0
    i = 0
    for val, size in slots:
        if val != ".":
            checksum += sum([val * j for j in range(i, i + size)])
        i += size
    print(checksum)
