from utils.read_input import read_input

if __name__ == "__main__":
    l1, l2 = [], []
    for line in read_input("2024/day_1/input.txt"):
        n1, n2 = line.split("   ")
        l1.append(int(n1))
        l2.append(int(n2))
    l1.sort()
    l2.sort()
    print(sum([abs(n1 - n2) for n1, n2 in zip(l1, l2)]))
