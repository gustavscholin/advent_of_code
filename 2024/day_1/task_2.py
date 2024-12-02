from utils.read_input import read_input

if __name__ == "__main__":
    l1, l2 = [], []
    for line in read_input("2024/day_1/input.txt"):
        n1, n2 = line.split("   ")
        l1.append(int(n1))
        l2.append(int(n2))

    print(sum([n * l2.count(n) for n in l1]))
