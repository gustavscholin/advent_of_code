def read_input(path: str):
    with open(path, "r") as f:
        return f.read().strip()


if __name__ == "__main__":
    stream = read_input("2022/day_6/input.txt")
    for i in range(4, len(stream)):
        seq = stream[i - 4 : i]
        if len(set(seq)) == len(seq):
            break
    print(i)
