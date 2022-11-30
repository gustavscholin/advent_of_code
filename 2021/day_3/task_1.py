import numpy as np

from utils.read_input import read_input

if __name__ == "__main__":
    binaries = read_input("day_3/input.txt")
    binaries = [[int(bit) for bit in binary] for binary in binaries]
    binaries = np.array(binaries)

    gamma_bin = np.sum(binaries, axis=0) > len(binaries) / 2
    epsilon_bin = np.logical_not(gamma_bin)
    gamma_bin = gamma_bin.astype(int).astype(str)
    epsilon_bin = epsilon_bin.astype(int).astype(str)

    gamma = int("".join(gamma_bin), 2)
    epsilon = int("".join(epsilon_bin), 2)

    print(gamma * epsilon)
