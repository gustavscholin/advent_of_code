from utils.read_input import read_input


def interpolation(x):
    if all([i == 0 for i in x]):
        return 0
    return x[0] - interpolation([x[i + 1] - x[i] for i in range(len(x) - 1)])


if __name__ == "__main__":
    readings = [
        [int(i) for i in line.split()] for line in read_input("2023/day_9/input.txt")
    ]
    print(sum([interpolation(r) for r in readings]))
