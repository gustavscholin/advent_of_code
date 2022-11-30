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


def parse_paket(bin_str: str, i: int, version_sum: int):
    version = int(bin_str[i : i + 3], 2)
    type_id = int(bin_str[i + 3 : i + 6], 2)

    if type_id == 4:
        j = i + 6
        while int(bin_str[j]) != 0:
            j += 5
        j += 5
        return j, version_sum + version

    length_type_id = int(bin_str[i + 6])
    if length_type_id == 0:
        sub_length = i + 22 + int(bin_str[i + 7 : i + 22], 2)
        i += 22
        while i < sub_length:
            i, version_sum = parse_paket(bin_str, i, version_sum)
    elif length_type_id == 1:
        nb_subs = int(bin_str[i + 7 : i + 18], 2)
        i += 18
        for _ in range(nb_subs):
            i, version_sum = parse_paket(bin_str, i, version_sum)

    return i, version_sum + version


def hexa_2_dec(hexa_str: str):
    return "".join([HEXA_DICT[s] for s in hexa_str])


if __name__ == "__main__":
    with open("day_16/input.txt", "r") as f:
        hexa_str = f.read().strip()

    bin_str = hexa_2_dec(hexa_str)
    _, version_sum = parse_paket(bin_str, 0, 0)
    print(version_sum)
