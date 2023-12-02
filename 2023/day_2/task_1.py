from utils.read_input import read_input

if __name__ == "__main__":
    games = read_input("2023/day_2/input.txt")
    limits = {"red": 12, "green": 13, "blue": 14}
    sum = 0
    for game_nbr, game in enumerate(games, 1):
        valid_game = True
        for draw in game.split(": ")[1].split("; "):
            for cubes in draw.split(", "):
                nbr, cube_color = cubes.split(" ")
                if int(nbr) > limits[cube_color]:
                    valid_game = False
                    break
            if not valid_game:
                break
        if valid_game:
            sum += game_nbr
    print(sum)
