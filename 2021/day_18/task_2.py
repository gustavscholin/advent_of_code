import json
import re
import math

from utils.read_input import read_input
from itertools import permutations


def explode(nbr: str) -> str:
    counter = 0
    for i, c in enumerate(nbr):
        if c == "[":
            counter += 1
        elif c == "]":
            counter -= 1
        if counter == 5:
            break
    if counter == 0:
        return nbr
    j = nbr.find("]", i)
    pair = json.loads(nbr[i : j + 1])

    pat = re.compile("\d+")

    right_sub = nbr[j + 1 :]
    right = pat.search(right_sub)
    if right:
        right_sub = (
            right_sub[: right.start()]
            + str(pair[1] + int(right.group()))
            + right_sub[right.end() :]
        )

    left_sub = nbr[:i]
    left = list(pat.finditer(left_sub))
    if left:
        left = left[-1]
        left_sub = (
            left_sub[: left.start()]
            + str(pair[0] + int(left.group()))
            + left_sub[left.end() :]
        )

    return left_sub + "0" + right_sub


def split(nbr: str) -> str:
    large = re.search(r"\d\d", nbr)
    if large:
        single = int(large.group())
        pair = (
            "[" + str(math.floor(single / 2)) + "," + str(math.ceil(single / 2)) + "]"
        )
        nbr = nbr[: large.start()] + pair + nbr[large.end() :]
    return nbr


def magnitude(nbr: str) -> str:
    while True:
        pair_match = re.search(r"\[\d+,\d+\]", nbr)
        if not pair_match:
            break
        pair = json.loads(pair_match.group())
        pair_magnitude = 3 * pair[0] + 2 * pair[1]
        nbr = nbr[: pair_match.start()] + str(pair_magnitude) + nbr[pair_match.end() :]
    return int(nbr)


def add_nbrs(nbr_1, nbr_2):
    add_nbr = "[" + nbr_1 + "," + nbr_2 + "]"
    while True:
        new_nbr = explode(add_nbr)
        if new_nbr != add_nbr:
            add_nbr = new_nbr
            continue
        new_nbr = split(add_nbr)
        if new_nbr != add_nbr:
            add_nbr = new_nbr
            continue
        break
    return add_nbr


if __name__ == "__main__":
    snail_nbrs = read_input("day_18/input.txt")

    nbr_combs = permutations(snail_nbrs, 2)

    magnitudes = [magnitude(add_nbrs(nbr_1, nbr_2)) for nbr_1, nbr_2 in nbr_combs]

    print(max(magnitudes))
