from utils.read_input import read_input

if __name__ == "__main__":
    dig_plan = read_input("2023/day_18/input.txt")
    area = 0
    nb_edge_points = 0
    p1 = (0, 0)
    for edge in dig_plan:
        dir, length = edge.split()[:2]
        length = int(length)

        if dir == "R":
            p2 = (p1[0] + length, p1[1])
        elif dir == "L":
            p2 = (p1[0] - length, p1[1])
        elif dir == "U":
            p2 = (p1[0], p1[1] + length)
        elif dir == "D":
            p2 = (p1[0], p1[1] - length)

        area += 0.5 * (p1[0] * p2[1] - p1[1] * p2[0])
        nb_edge_points += length
        p1 = p2

    # Modified Pick's theorem, i + b = A + b/2 + 1
    print(int(abs(area) + 0.5 * nb_edge_points + 1))
