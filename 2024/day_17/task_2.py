import re


def combo(operand, a, b, c):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c


def dv(operand, a, b, c):
    return a // 2 ** combo(operand, a, b, c)


def op(a, b, c, p):
    if p >= len(program):
        return ""
    else:
        operand = int(program[p + 1])
        match int(program[p]):
            case 0:
                return op(dv(operand, a, b, c), b, c, p + 2)
            case 1:
                return op(a, b ^ operand, c, p + 2)
            case 2:
                return op(a, combo(operand, a, b, c) % 8, c, p + 2)
            case 3:
                if a != 0:
                    return op(a, b, c, operand)
                else:
                    return op(a, b, c, p + 2)
            case 4:
                return op(a, b ^ c, c, p + 2)
            case 5:
                return str(combo(operand, a, b, c) % 8) + op(a, b, c, p + 2)
            case 6:
                return op(a, dv(operand, a, b, c), c, p + 2)
            case 7:
                return op(a, b, dv(operand, a, b, c), p + 2)


def find_ra(idx, octal):
    for i in range(8):
        for j in range(8):
            ra = j + i * 8 + int(octal + "00", 8)
            if (out := op(ra, inrb, inrc, 0)) == program[-1 - idx :]:
                if out == program:
                    return ra
                if r := find_ra(idx + 1, octal + str(i)):
                    return r


if __name__ == "__main__":
    with open("2024/day_17/input.txt", "r") as f:
        _, inrb, inrc, program = re.match(
            r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: (.+)",
            f.read(),
        ).groups()

    inra, inrb, inrc = 0, int(inrb), int(inrc)
    program = program.replace(",", "")
    octal = ""

    print(find_ra(0, octal))
