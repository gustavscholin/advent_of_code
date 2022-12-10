from utils.read_input import read_input


def get_pixel(pixel):
    pixel_str = "#" if abs((pixel % 40) - cycles[pixel]) < 2 else "."
    if (pixel + 1) % 40 == 0:
        pixel_str += "\n"
    return pixel_str


if __name__ == "__main__":
    program = read_input("2022/day_10/input.txt")
    X = 1
    cycles = [X]
    out_str = "#"

    for command in program:
        cycles.append(X)
        out_str += get_pixel(len(cycles) - 1)
        if "addx" in command:
            X += int(command.split()[1])
            cycles.append(X)
            out_str += get_pixel(len(cycles) - 1)
        if len(cycles) == 240:
            break

    print(out_str)
