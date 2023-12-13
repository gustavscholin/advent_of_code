import re
from collections import Counter
from dataclasses import dataclass
from itertools import product

from utils.read_input import read_input


@dataclass
class Hand:
    hand: str
    strongest_hand: str
    bid: int


cards = {
    "A": "d",
    "K": "c",
    "Q": "b",
    "T": "a",
    "9": "9",
    "8": "8",
    "7": "7",
    "6": "6",
    "5": "5",
    "4": "4",
    "3": "3",
    "2": "2",
    "J": "1",
}


def get_strongest(hand):
    j_idxs = [i for i, j in enumerate(hand) if j == "J"]
    if not j_idxs:
        return hand
    hands = []
    for replacements in product("".join("AKQT98765432"), repeat=len(j_idxs)):
        new_hand = hand
        for idx, replacement in zip(j_idxs, replacements):
            new_hand = new_hand[:idx] + replacement + new_hand[idx + 1 :]
        hands.append(new_hand)
    return max(hands, key=lambda x: get_type(x, x))


def get_type(hand, strongest_hand):
    counts = Counter(strongest_hand)
    val_counts = sorted(counts.values(), reverse=True)
    if val_counts[0] == 5:
        type_rank = "7"
    elif val_counts[0] == 4:
        type_rank = "6"
    elif val_counts[0] == 3 and val_counts[1] == 2:
        type_rank = "5"
    elif val_counts[0] == 3:
        type_rank = "4"
    elif val_counts[0] == 2 and val_counts[1] == 2:
        type_rank = "3"
    elif val_counts[0] == 2:
        type_rank = "2"
    else:
        type_rank = "1"
    return type_rank + "".join([cards[c] for c in hand])


if __name__ == "__main__":
    hands = [
        Hand(
            hand=line.split()[0],
            strongest_hand=get_strongest(line.split()[0]),
            bid=int(line.split()[1]),
        )
        for line in read_input("2023/day_7/input.txt")
    ]
    hands.sort(key=lambda x: get_type(x.hand, x.strongest_hand))
    print(sum([hand.bid * i for i, hand in enumerate(hands, 1)]))
