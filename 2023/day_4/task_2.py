from utils.read_input import read_input

if __name__ == "__main__":
    cards = read_input("2023/day_4/input.txt")
    copies = {i: 1 for i in range(1, len(cards) + 1)}
    for card_nbr, card in enumerate(cards, 1):
        winning, played = card.split(": ")[1].split(" | ")
        winning = [int(i) for i in winning.split()]
        played = [int(i) for i in played.split()]
        played_winnings = len(set(played).intersection(set(winning)))
        for i in range(1, played_winnings + 1):
            copies[card_nbr + i] += copies[card_nbr]
    print(sum(copies.values()))
