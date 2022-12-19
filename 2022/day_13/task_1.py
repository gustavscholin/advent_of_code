def read_input(path: str):
    with open(path) as f:
        return [
            tuple(eval(s) for s in pair.splitlines()) for pair in f.read().split("\n\n")
        ]


def compare(left_list, right_list):
    for left, right in zip(left_list, right_list):
        if type(left) == int and type(right) == int:
            if left < right:
                return True
            elif left > right:
                return False
            continue
        right = [right] if type(right) == int else right
        left = [left] if type(left) == int else left
        res = compare(left, right)
        if res is not None:
            return res
    if len(left_list) < len(right_list):
        return True
    elif len(left_list) > len(right_list):
        return False


if __name__ == "__main__":
    pairs = read_input("2022/day_13/input.txt")
    correct_pairs = []
    for i, (left, right) in enumerate(pairs):
        res = compare(left, right)
        if res:
            correct_pairs.append(i + 1)
    print(sum(correct_pairs))
