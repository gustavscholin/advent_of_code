import numpy as np

from utils.read_input import read_input_single_line

if __name__ == "__main__":
    crabs = np.array(read_input_single_line("day_7/input.txt", "int"))

    min_fuel = 10000000000
    for i in range(min(crabs), max(crabs) + 1):
        fuel = np.abs(crabs - i)
        fuel = np.sum([sum(range(j + 1)) for j in fuel])
        if fuel < min_fuel:
            min_fuel = fuel

    print(min_fuel)
