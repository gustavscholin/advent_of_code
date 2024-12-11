if __name__ == "__main__":
    with open("2024/day_11/input.txt", "r") as f:
        stones = [int(s) for s in f.read().strip().split()]

    for _ in range(25):
        new_stones = []
        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif len(str(stone)) % 2 == 0:
                s = str(stone)
                new_stones.append(int(s[: len(s) // 2]))
                new_stones.append(int(s[len(s) // 2 :]))
            else:
                new_stones.append(stone * 2024)
        stones = new_stones
    print(len(stones))
