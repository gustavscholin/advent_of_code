from itertools import product

from utils.read_input import read_input

if __name__ == "__main__":
    total_result = 0
    for line in read_input("2024/day_7/input.txt"):
        value_str, nums_str = line.split(": ")
        value = int(value_str)
        nums = [int(i) for i in nums_str.split()]
        for ops in product("+*", repeat=len(nums) - 1):
            eq_value = nums[0]
            for op, num in zip(ops, nums[1:]):
                eq_value = eval(f"{eq_value}{op}{num}")
            if eq_value == value:
                total_result += value
                break

    print(total_result)
