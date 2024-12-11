from itertools import product

from utils.read_input import read_input

if __name__ == "__main__":
    total_result = 0
    products = {}
    for line in read_input("2024/day_7/input.txt"):
        value_str, nums_str = line.split(": ")
        value = int(value_str)
        nums = [int(i) for i in nums_str.split()]

        rep = len(nums) - 1
        if not products.get(rep):
            products[rep] = list(product(["+", "*", "||"], repeat=rep))
        prod = products.get(rep)

        for ops in prod:
            eq_value = nums[0]
            for op, num in zip(ops, nums[1:]):
                if op == "||":
                    eq_value = int(f"{eq_value}{num}")
                else:
                    eq_value = eval(f"{eq_value}{op}{num}")
                if eq_value > value:
                    break
            if eq_value == value:
                total_result += value
                break
    print(total_result)
