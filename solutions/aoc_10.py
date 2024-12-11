import re


def one(lines):
#     lines = """89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732""".splitlines()

    # lines = lines.splitlines()

    def find_zeros(lines):
        return [(line_index, match.start()) for line_index, line in enumerate(lines) for match in re.finditer('0', line)]

    def traverse(lines, y , x, paths, prev = None):
        if y < 0 or y >= len(lines) or x < 0 or x >= len(lines[0]):
            return 0
        if lines[y][x] == '.' or prev is not None and (int(prev) + 1 != int(lines[y][x])):
            return 0
        if lines[y][x] == '9':
            if (y, x) not in paths:
                paths.add((y,x))
                return 1
            else:
                return 0

        return traverse(lines, y+1 , x, paths, prev=lines[y][x]) + traverse(lines, y , x+1, paths, prev=lines[y][x]) \
            + traverse(lines, y , x-1, paths, prev=lines[y][x]) \
            + traverse(lines, y-1 , x, paths, prev=lines[y][x])


    zeros = find_zeros(lines)
    s = 0
    for zero in zeros:
        s += traverse(lines, zero[0], zero[1], set())
    return s
def two(lines):
#     lines = """89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732""".splitlines()
    def find_zeros(lines):
        return [(line_index, match.start()) for line_index, line in enumerate(lines) for match in
                re.finditer('0', line)]

    def traverse(lines, y, x, prev=None):
        if y < 0 or y >= len(lines) or x < 0 or x >= len(lines[0]):
            return 0
        if lines[y][x] == '.' or prev is not None and (int(prev) + 1 != int(lines[y][x])):
            return 0
        if lines[y][x] == '9':
            return 1

        return traverse(lines, y + 1, x, prev=lines[y][x]) + traverse(lines, y, x + 1, prev=lines[y][x]) \
            + traverse(lines, y, x - 1, prev=lines[y][x]) \
            + traverse(lines, y - 1, x, prev=lines[y][x])

    zeros = find_zeros(lines)
    s = 0
    for zero in zeros:
        s += traverse(lines, zero[0], zero[1])
    return s
