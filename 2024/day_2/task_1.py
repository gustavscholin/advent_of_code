from utils.read_input import read_input

if __name__ == "__main__":
    safe_reports = 0
    for line in read_input("2024/day_2/input.txt"):
        report = [int(i) for i in line.split()]
        if (report == sorted(report, reverse=True) or report == sorted(report)) and all(
            [1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1)]
        ):
            safe_reports += 1
    print(safe_reports)
