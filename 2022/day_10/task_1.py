from utils.read_input import read_input

if __name__ == "__main__":
    program = read_input("2022/day_10/input.txt")
    X = 1
    cycles = [X]

    for command in program:
        cycles.append(X)
        if "addx" in command:
            X += int(command.split()[1])
            cycles.append(X)
        if len(cycles) > 220:
            break

    print(sum([i * cycles[i - 1] for i in (20, 60, 100, 140, 180, 220)]))
