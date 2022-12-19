from functools import cmp_to_key


def read_input(path: str):
    with open(path) as f:
        return [eval(l) for l in f.read().replace("\n\n", "\n").splitlines()]


def compare(left_list, right_list):
    for left, right in zip(left_list, right_list):
        if type(left) == int and type(right) == int:
            if left < right:
                return -1
            elif left > right:
                return 1
            continue
        right = [right] if type(right) == int else right
        left = [left] if type(left) == int else left
        res = compare(left, right)
        if res is not None:
            return res
    if len(left_list) < len(right_list):
        return -1
    elif len(left_list) > len(right_list):
        return 1


if __name__ == "__main__":
    packets = read_input("2022/day_13/input.txt")
    start, end = [[2]], [[6]]
    packets.extend([start, end])
    packets.sort(key=cmp_to_key(compare))
    print((packets.index(start) + 1) * (packets.index(end) + 1))
