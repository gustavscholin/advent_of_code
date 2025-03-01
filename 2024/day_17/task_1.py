import re


def combo(operand: int):
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return ra
        case 5:
            return rb
        case 6:
            return rc


def dv(operand):
    return ra // 2 ** combo(operand)


if __name__ == "__main__":
    with open("2024/day_17/input.txt", "r") as f:
        ra, rb, rc, program = re.match(
            r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)\n\nProgram: (.+)",
            f.read(),
        ).groups()
    ra, rb, rc = int(ra), int(rb), int(rc)
    program = [int(i) for i in program.split(",")]
    pointer = 0
    out = []

    while pointer < len(program):
        jumped = False
        operand = program[pointer + 1]
        match opcode := program[pointer]:
            case 0:
                ra = dv(operand)
            case 1:
                rb = rb ^ operand
            case 2:
                rb = combo(operand) % 8
            case 3:
                if ra != 0:
                    pointer = operand
                    jumped = True
            case 4:
                rb = rb ^ rc
            case 5:
                out.append(str(combo(operand) % 8))
            case 6:
                rb = dv(operand)
            case 7:
                rc = dv(operand)
        if not jumped:
            pointer += 2

    print(",".join(out))
