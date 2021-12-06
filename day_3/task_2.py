import numpy as np

from copy import deepcopy
from utils.read_input import read_input

if __name__ == "__main__":
    binaries = read_input("day_3/input.txt")

    oxygen_binaries = deepcopy(binaries)
    for i in range(len(binaries[0])):
        oxygen_binaries_np = np.array([[int(bit) for bit in binary] for binary in oxygen_binaries])
        most_common = np.sum(oxygen_binaries_np, axis=0) >= len(oxygen_binaries_np) / 2
        oxygen_binaries = [binary for binary in oxygen_binaries if int(binary[i]) == bool(most_common[i])]
        if len(oxygen_binaries) == 1:
            break

    co2scrub_binaries = deepcopy(binaries)
    for i in range(len(binaries[0])):
        co2scrub_binaries_np = np.array([[int(bit) for bit in binary] for binary in co2scrub_binaries])
        least_common = np.sum(co2scrub_binaries_np, axis=0) < len(co2scrub_binaries_np) / 2
        co2scrub_binaries = [binary for binary in co2scrub_binaries if int(binary[i]) == bool(least_common[i])]
        if len(co2scrub_binaries) == 1:
            break

    print(int(oxygen_binaries[0], 2) * int(co2scrub_binaries[0], 2))
