import re
from utils.read_input import read_input

if __name__ == "__main__":
    times, records = [
        [int(i) for i in re.findall(r"\d+", line)]
        for line in read_input("2023/day_6/input.txt")
    ]
    product = 1
    for time, record in zip(times, records):
        record_beats = 0
        for ms in range(1, time):
            if ms * (time - ms) > record:
                record_beats += 1
        product *= record_beats
    print(product)
