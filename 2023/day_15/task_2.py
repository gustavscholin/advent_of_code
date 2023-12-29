import re
from collections import defaultdict


def hash_algo(seq):
    current_value = 0
    for c in seq:
        current_value = ((current_value + ord(c)) * 17) % 256
    return current_value


if __name__ == "__main__":
    with open("2023/day_15/input.txt") as f:
        sequences = f.read().replace("\n", "").split(",")

    boxes = defaultdict(list)
    seq_sum = 0
    for seq in sequences:
        label = re.split(r"=|-", seq)[0]
        box = hash_algo(label)
        box_labels = [b[0] for b in boxes[box]]

        if "=" in seq:
            focal_length = int(seq.split("=")[1])
            if label in box_labels:
                boxes[box][box_labels.index(label)] = (label, focal_length)
            else:
                boxes[box].append((label, focal_length))
        elif label in box_labels:
            del boxes[box][box_labels.index(label)]

    print(
        sum(
            [
                sum([(box + 1) * i * l[1] for i, l in enumerate(lenses, 1)])
                for box, lenses in boxes.items()
            ]
        )
    )
