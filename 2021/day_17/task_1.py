import re


def read_input(path: str):
    with open(path, "r") as f:
        return [int(i) for i in re.findall(r"-?\d+", f.read())]


if __name__ == "__main__":
    target = read_input("day_17/input.txt")

    print(sum(range(abs(target[2]))))
