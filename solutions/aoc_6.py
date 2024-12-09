def one(map):



    def find_guard(map):
        for y in range(len(map)):
            for x in range(len(map[0])):
                if map[y][x] == '^':
                    return y, x


    def face(f):
        if f == 'n':
            return 'r'
        elif f == 's':
            return 'l'
        elif f == 'l':
            return 'n'
        else:
            return 's'
    def move(map, x, y):
        f = 'n'
        c = set()
        while True:
            if f == 'n':
                if y-1 < 0:
                    return c
                elif map[y-1][x] == "#":
                    f = face(f)
                else:
                    y -= 1
                    c.add((x,y))
            elif f == 's':
                if y+1 >= len(map):
                    return c
                elif map[y+1][x] == "#":
                    f = face(f)
                else:
                    y += 1
                    c.add((x,y))
            elif f == 'r':

                if x+1 >= len(map[0]):
                    return c
                elif map[y][x+1] == "#":
                    f = face(f)
                else:
                    x += 1
                    c.add((x,y))
            elif f == 'l':
                if x-1 < 0:
                    return c
                elif map[y][x-1] == "#":
                    f = face(f)
                else:
                    x -= 1
                    c.add((x,y))

    x, y = find_guard(map)
    return len(move(map, y, x))


def two(map):
#     map = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...""".splitlines()
    def find_guard(map):
        for y in range(len(map)):
            for x in range(len(map[0])):
                if map[y][x] == '^':
                    return y, x


    def face(f):
        if f == 'n':
            return 'r'
        elif f == 's':
            return 'l'
        elif f == 'l':
            return 'n'
        else:
            return 's'
    def move(map, x, y):
        f = 'n'
        c = set()
        while True:
            if f == 'n':
                if y-1 < 0:
                    return c
                elif map[y-1][x] == "#":
                    f = face(f)
                else:
                    y -= 1
                    c.add((x,y))
            elif f == 's':
                if y+1 >= len(map):
                    return c
                elif map[y+1][x] == "#":
                    f = face(f)
                else:
                    y += 1
                    c.add((x,y))
            elif f == 'r':

                if x+1 >= len(map[0]):
                    return c
                elif map[y][x+1] == "#":
                    f = face(f)
                else:
                    x += 1
                    c.add((x,y))
            elif f == 'l':
                if x-1 < 0:
                    return c
                elif map[y][x-1] == "#":
                    f = face(f)
                else:
                    x -= 1
                    c.add((x,y))

    def move_2(map, x, y):
        f = 'n'
        c = set()
        while True:
            if f == 'n':
                if y-1 < 0:
                    return False
                elif map[y-1][x] == "#":
                    f = face(f)
                else:
                    y -= 1
                    if (x,y, f) not in c:
                        c.add((x,y, f))
                    else:
                        return True
            elif f == 's':
                if y+1 >= len(map):
                    return False
                elif map[y+1][x] == "#":
                    f = face(f)
                else:
                    y += 1
                    if (x, y, f) not in c:
                        c.add((x, y, f))
                    else:
                        return True
            elif f == 'r':

                if x+1 >= len(map[0]):
                    return False
                elif map[y][x+1] == "#":
                    f = face(f)
                else:
                    x += 1
                    if (x, y, f) not in c:
                        c.add((x, y, f))
                    else:
                        return True
            elif f == 'l':
                if x-1 < 0:
                    return False
                elif map[y][x-1] == "#":
                    f = face(f)
                else:
                    x -= 1
                    if (x, y, f) not in c:
                        c.add((x, y, f))
                    else:
                        return True

    loops = 0
    x, y = find_guard(map)
    c = move(map, y, x)
    for pos in c:
        if pos == (x, y):
            continue
        x_o, y_o = pos
        # Deep copy the map with each row as a list of characters
        copy_map = [list(row) for row in map]

        # Modify the specific position
        copy_map[y_o][x_o] = copy_map[y_o][x_o].replace('.', '#')

        # Convert rows back to strings for the next operation
        copy_map = [''.join(row) for row in copy_map]

        if move_2(copy_map, y, x):
            loops += 1

    return loops
