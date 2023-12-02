from utils.read_input import read_input

if __name__ == "__main__":
    games = read_input("2023/day_2/input.txt")
    sum = 0
    for game in games:
        min_cubes = {"red": 0, "green": 0, "blue": 0}
        for draw in game.split(": ")[1].split("; "):
            for cubes in draw.split(", "):
                nbr, cube_color = cubes.split(" ")
                if int(nbr) > min_cubes[cube_color]:
                    min_cubes[cube_color] = int(nbr)
        sum += min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
    print(sum)
