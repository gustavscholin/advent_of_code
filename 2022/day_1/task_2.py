if __name__ == "__main__":
    input_path = "2022/day_1/input.txt"
    with open(input_path, "r") as f:
        cal_list = [
            [int(s) for s in l.split("\n")] for l in f.read().strip("\n").split("\n\n")
        ]
    print(sum(sorted([sum(l) for l in cal_list])[-3:]))
