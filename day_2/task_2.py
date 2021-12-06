from utils.read_input import read_input

if __name__ == "__main__":
    instructions = read_input("day_2/input.txt")
    h_pos = 0
    d_pos = 0
    aim = 0

    for instruction in instructions:
        direction, value = instruction.split()
        value = int(value)
        if direction == "forward":
            h_pos += value
            d_pos += aim * value
        elif direction == "down":
            aim += value
        elif direction == "up":
            aim -= value

    print(h_pos * d_pos)
