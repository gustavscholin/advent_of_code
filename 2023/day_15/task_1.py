if __name__ == "__main__":
    with open("2023/day_15/input.txt") as f:
        sequences = f.read().replace("\n", "").split(",")

    seq_sum = 0
    for seq in sequences:
        current_value = 0
        for c in seq:
            current_value = ((current_value + ord(c)) * 17) % 256
        seq_sum += current_value

    print(seq_sum)
