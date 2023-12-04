from utils.read_input import read_input

if __name__ == "__main__":
    cards = read_input("2023/day_4/input.txt")
    sum = 0
    for card in cards:
        winning, played = card.split(": ")[1].split(" | ")
        winning = [int(i) for i in winning.split()]
        played = [int(i) for i in played.split()]
        played_winnings = len(set(played).intersection(set(winning)))
        if played_winnings:
            sum += 2 ** (played_winnings - 1)
    print(sum)
