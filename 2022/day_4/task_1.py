from utils.read_input import read_input

if __name__ == "__main__":
    assignment_pairs = read_input("2022/day_4/input.txt")
    contained = 0
    for pair in assignment_pairs:
        assignments = (tuple(int(s) for s in a.split("-")) for a in pair.split(","))
        set_1, set_2 = (set(range(a[0], a[1] + 1)) for a in assignments)
        if set_1.issubset(set_2) or set_2.issubset(set_1):
            contained += 1
    print(contained)
