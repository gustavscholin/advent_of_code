from utils.read_input import read_input


def is_safe(report: list[int]):
    return (report == sorted(report, reverse=True) or report == sorted(report)) and all(
        [1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1)]
    )


if __name__ == "__main__":
    safe_reports = 0
    for line in read_input("2024/day_2/input.txt"):
        report = [int(i) for i in line.split()]
        if is_safe(report):
            safe_reports += 1
        else:
            for sub_report in [
                [report[i] for i in range(len(report)) if i != j]
                for j in range(len(report))
            ]:
                if is_safe(sub_report):
                    safe_reports += 1
                    break
    print(safe_reports)
