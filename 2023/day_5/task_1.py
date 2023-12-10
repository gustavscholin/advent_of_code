def read_input(path):
    with open(path, "r") as f:
        almanac = f.read().split("\n\n")
        seeds = [int(i) for i in almanac[0].split(": ")[1].split()]
        cat_maps = []
        for cat_map in almanac[1:]:
            cat_maps.append(
                [
                    [int(i) for i in line.split()]
                    for line in cat_map.strip("\n").split("\n")[1:]
                ]
            )
    return seeds, cat_maps


if __name__ == "__main__":
    seeds, maps = read_input("2023/day_5/input.txt")
    locations = []
    for seed in seeds:
        for cat_map in maps:
            for conversion in cat_map:
                if conversion[1] <= seed < conversion[1] + conversion[2]:
                    seed = conversion[0] + seed - conversion[1]
                    break
        locations.append(seed)
    print(min(locations))
