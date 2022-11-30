HEXA_DICT = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def parse_paket(bin_str: str, i: int):
    type_id = int(bin_str[i + 3 : i + 6], 2)

    if type_id == 4:
        out_bin_str = ""
        j = i + 6
        while int(bin_str[j]) != 0:
            out_bin_str += bin_str[j + 1 : j + 5]
            j += 5
        out_bin_str += bin_str[j + 1 : j + 5]
        j += 5
        return j, int(out_bin_str, 2)

    length_type_id = int(bin_str[i + 6])
    num_list = []
    if length_type_id == 0:
        sub_length = i + 22 + int(bin_str[i + 7 : i + 22], 2)
        i += 22
        while i < sub_length:
            i, num = parse_paket(bin_str, i)
            num_list.append(num)
    elif length_type_id == 1:
        nb_subs = int(bin_str[i + 7 : i + 18], 2)
        i += 18
        for _ in range(nb_subs):
            i, num = parse_paket(bin_str, i)
            num_list.append(num)

    match type_id:
        case 0:
            return i, sum(num_list)
        case 1:
            return i, prod(num_list)
        case 2:
            return i, min(num_list)
        case 3:
            return i, max(num_list)
        case 5:
            return i, int(num_list[0] > num_list[1])
        case 6:
            return i, int(num_list[0] < num_list[1])
        case 7:
            return i, int(num_list[0] == num_list[1])


def prod(l):
    res = 1
    for i in l:
        res *= i
    return res


def hexa_2_dec(hexa_str: str):
    return "".join([HEXA_DICT[s] for s in hexa_str])


if __name__ == "__main__":
    with open("day_16/input.txt", "r") as f:
        hexa_str = f.read().strip()

    bin_str = hexa_2_dec(hexa_str)
    _, res = parse_paket(bin_str, 0)
    print(res)
