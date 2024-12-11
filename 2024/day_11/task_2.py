def blink(stone, level):
    if level == max_level:
        return 1

    if cached := cache.get((stone, level)):
        return cached

    if stone == 0:
        nbr_stones = blink(1, level + 1)
    elif len(str(stone)) % 2 == 0:
        s = str(stone)
        stone_1 = blink(int(s[: len(s) // 2]), level + 1)
        stone_2 = blink(int(s[len(s) // 2 :]), level + 1)
        nbr_stones = stone_1 + stone_2
    else:
        nbr_stones = blink(stone * 2024, level + 1)

    cache[(stone, level)] = nbr_stones
    return nbr_stones


if __name__ == "__main__":
    cache = {}
    max_level = 75
    with open("2024/day_11/input.txt", "r") as f:
        print(sum([blink(int(s), 0) for s in f.read().strip().split()]))
