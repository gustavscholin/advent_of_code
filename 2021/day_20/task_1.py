from collections import defaultdict
from copy import deepcopy


def read_input(path: str):
    with open(path, "r") as f:
        lines = f.read().splitlines()
    algo = lines.pop(0)
    image_dict = defaultdict(int)
    for i, line in enumerate(lines[1:]):
        for j, pixel in enumerate(line):
            if pixel == "#":
                image_dict[(i, j)] = 1
    return algo, image_dict


def get_pot_pixels(image_dict):
    pot_pixels = set()
    for pixel in image_dict.keys():
        pot_pixels.add(pixel)
        for i in range(pixel[0] - 1, pixel[0] + 2):
            for j in range(pixel[1] - 1, pixel[1] + 2):
                if (i, j) != pixel:
                    pot_pixels.add((i, j))
    return pot_pixels


if __name__ == "__main__":
    algo, image_dict = read_input("2021/day_20/input.txt")
    for turn in range(2):
        if algo[0] == "#" and algo[-1] == ".":
            if turn % 2 == 1:
                image_dict.default_factory = lambda: 1
            else:
                image_dict.default_factory = lambda: 0

        pot_pixels = get_pot_pixels(image_dict)
        next_image_dict = deepcopy(image_dict)
        for pixel in pot_pixels:
            pixel_str = ""
            for i in range(pixel[0] - 1, pixel[0] + 2):
                for j in range(pixel[1] - 1, pixel[1] + 2):
                    pixel_str += str(image_dict[(i, j)])
            if algo[int(pixel_str, 2)] == "#":
                next_image_dict[pixel] = 1
            else:
                next_image_dict[pixel] = 0
        image_dict = next_image_dict
    cnt = 0
    for k in image_dict:
        if image_dict[k] == 1:
            cnt += 1
    print(cnt)
