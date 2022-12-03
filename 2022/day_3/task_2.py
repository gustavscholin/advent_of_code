from utils.read_input import read_input


def chunker(seq, size):
    return (seq[pos : pos + size] for pos in range(0, len(seq), size))


if __name__ == "__main__":
    items_list = read_input("2022/day_3/input.txt")
    priority_sum = 0
    for item_1, item_2, item_3 in chunker(items_list, 3):
        badge_item = (set(item_1) & set(item_2) & set(item_3)).pop()

        if badge_item.isupper():
            priority_sum += ord(badge_item) - ord("A") + 27
        else:
            priority_sum += ord(badge_item) - ord("a") + 1
    print(priority_sum)
