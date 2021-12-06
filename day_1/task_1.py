from utils.read_input import read_input

if __name__ == "__main__":
    messurements = read_input("day_1/input.txt", "int")

    increases = 0
    for i in range(1, len(messurements)):
        if messurements[i] > messurements[i - 1]:
            increases += 1

    print(increases)
