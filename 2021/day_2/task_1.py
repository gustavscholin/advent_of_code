from utils.read_input import read_input

if __name__ == "__main__":
    instructions = read_input("2021/day_2/input.txt")
    h_pos = 0
    d_pos = 0

    for instruction in instructions:
        direction, value = instruction.split()
        value = int(value)
        if direction == "forward":
            h_pos += value
        elif direction == "down":
            d_pos += value
        elif direction == "up":
            d_pos -= value

    print(h_pos * d_pos)
