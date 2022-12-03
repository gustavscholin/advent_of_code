from utils.read_input import read_input

if __name__ == "__main__":
    items_list = read_input("2022/day_3/input.txt")
    priority_sum = 0
    for items in items_list:
        item = (set(items[: len(items) // 2]) & set(items[len(items) // 2 :])).pop()
        if item.isupper():
            priority_sum += ord(item) - ord("A") + 27
        else:
            priority_sum += ord(item) - ord("a") + 1
    print(priority_sum)
