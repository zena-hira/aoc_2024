import itertools


def one(lines):
#     lines = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............""".splitlines()

    h = {}
    y_max = len(lines)-1
    x_max = len(lines[0])-1
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x].isdigit() or lines[y][x].isalpha():
                h.setdefault(lines[y][x], set()).add((y,x))

    def find_distance(loc1, loc2):
        return (loc1[0] - loc2[0], loc1[1] - loc2[1])

    def calc_antidote(loc2, d):
        if loc2[0] + d[0] <= y_max and loc2[0] + d[0] >= 0 and loc2[1] + d[1] <= x_max and loc2[1] + d[1] >= 0:
            antidotes.add((loc2[0] + d[0], loc2[1] + d[1]))



    antidotes = set()
    for k, v in h.items():
        pairs = list(itertools.combinations(v, 2))
        for loc1, loc2 in pairs:
            d = find_distance(loc1, loc2)
            calc_antidote(loc1, d)
            d = find_distance(loc2, loc1)

            calc_antidote(loc2, d)

    return len(antidotes)



def two(lines):
#     lines = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............""".splitlines()

    h = {}
    y_max = len(lines) - 1
    x_max = len(lines[0]) - 1
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x].isdigit() or lines[y][x].isalpha():
                h.setdefault(lines[y][x], set()).add((y, x))

    def find_distance(loc1, loc2):
        return (loc1[0] - loc2[0], loc1[1] - loc2[1])

    def calc_antidote(loc2, d):
        bound1 = loc2[0]
        bound2 = loc2[1]
        while y_max >= bound1 + d[0] >= 0 and x_max >= bound2 + d[1] >= 0:
            antidotes.add((bound1 + d[0], bound2 + d[1]))
            bound1 += d[0]
            bound2 += d[1]

    antidotes = set()
    for k, v in h.items():
        pairs = list(itertools.combinations(v, 2))
        for loc1, loc2 in pairs:
            d = find_distance(loc1, loc2)
            calc_antidote(loc1, d)
            d = find_distance(loc2, loc1)
            calc_antidote(loc2, d)
            antidotes.add(tuple(loc1))
            antidotes.add(tuple(loc2))

    return len(antidotes)


