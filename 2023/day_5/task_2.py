def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return zip(a, a)


def read_input(path: str):
    with open(path, "r") as f:
        almanac = f.read().split("\n\n")
        seed_ranges = [
            range(int(x), int(x) + int(y))
            for x, y in pairwise(almanac[0].split(": ")[1].split())
        ]
        cat_maps = []
        for cat_map in almanac[1:]:
            cat_maps.append(
                [
                    [int(i) for i in line.split()]
                    for line in cat_map.strip("\n").split("\n")[1:]
                ]
            )
    return seed_ranges, cat_maps


def intersection(x: range, y: range):
    return range(max(x.start, y.start), min(x.stop, y.stop))


if __name__ == "__main__":
    seed_ranges, maps = read_input("2023/day_5/input.txt")
    for cat_map in maps:
        new_seed_ranges = []
        for conversion in cat_map:
            keep_ranges = []
            source_range = range(conversion[1], conversion[1] + conversion[2])
            dest_range = range(conversion[0], conversion[0] + conversion[2])
            for seed_range in seed_ranges:
                if inter := intersection(source_range, seed_range):
                    new_start = dest_range.start + inter.start - source_range.start
                    new_seed_ranges.append(range(new_start, new_start + len(inter)))
                    if keep_range := range(seed_range.start, inter.start):
                        keep_ranges.append(keep_range)
                    if keep_range := range(inter.stop, seed_range.stop):
                        keep_ranges.append(keep_range)
                else:
                    keep_ranges.append(seed_range)
            seed_ranges = keep_ranges
        seed_ranges += new_seed_ranges
    print(min([r.start for r in seed_ranges]))
