from utils.read_input import read_input

if __name__ == "__main__":
    messurements = read_input("day_1/input.txt", "int")

    increases = 0
    for i in range(len(messurements) - 3):
        if sum(messurements[i : i + 3]) < sum(messurements[i + 1 : i + 4]):
            increases += 1

    print(increases)
