from collections import defaultdict


def one(lines):
#     lines = """RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE""".splitlines()
    def group_adjacent_values(grid):
        def get_neighbors(pos):
            row, col = pos
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, down, left, right
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                    yield (r, c)

        def bfs(start):
            value = grid[start[0]][start[1]]
            queue = [start]
            group = set()
            while queue:
                pos = queue.pop()
                if pos not in visited:
                    visited.add(pos)
                    group.add(pos)
                    for neighbor in get_neighbors(pos):
                        if neighbor not in visited and grid[neighbor[0]][neighbor[1]] == value:
                            queue.append(neighbor)
            return group

        visited = set()
        groups = []

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited:
                    group = bfs((row, col))
                    if group:
                        groups.append(group)

        return groups

    def calculate_perimeter_and_area(group, grid):
        area = len(group)
        perimeter = 0

        for pos in group:
            row, col = pos
            neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            for neighbor in neighbors:
                if neighbor not in group and (
                        neighbor[0] < 0 or neighbor[0] >= len(grid) or
                        neighbor[1] < 0 or neighbor[1] >= len(grid[0]) or
                        grid[neighbor[0]][neighbor[1]] != grid[row][col]
                ):
                    perimeter += 1

        return area, perimeter

    groups = group_adjacent_values(lines)
    s = 0
    for group in groups:
        area, perimeter = calculate_perimeter_and_area(group, lines)
        s += area * perimeter



    return s


def two(lines):
#     lines = """AAAA
# BBCD
# BBCC
# EEEC""".splitlines()
    def group_adjacent_values(grid):
        def get_neighbors(pos):
            row, col = pos
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
                    yield (r, c)

        def bfs(start):
            value = grid[start[0]][start[1]]
            queue = [start]
            group = set()

            while queue:
                pos = queue.pop()
                if pos not in visited:
                    visited.add(pos)
                    group.add(pos)
                    for neighbor in get_neighbors(pos):
                        if neighbor not in visited and grid[neighbor[0]][neighbor[1]] == value:
                            queue.append(neighbor)
            return group

        visited = set()
        groups = []

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited:
                    group = bfs((row, col))
                    if group:
                        groups.append(group)

        return groups

    def calculate_area_and_sides(group, grid):
        area = len(group)
        edges = 0

        for pos in group:
            row, col = pos
            edge_ids = set()
            neighbors = [(row - 1, col,0), (row + 1, col,2), (row, col - 1,1), (row, col + 1,3)]
            for r, c, edge in neighbors:
                if (r,c) not in group:
                    edge_ids.add(edge)

            if len(edge_ids) == 4:
                edges += 4
            elif len(edge_ids) == 3:
                edges += 2
            elif len(edge_ids) == 2:
                a,b = list(edge_ids)
                if (a%2) != (b%2):
                    edges += 1

            for (di, dj) in [(-1,-1), (-1,1), (1,-1), (1,1)]:
                if {(row + di, col), (row, col + dj)}.issubset(group) and (row +di, col + dj) not in group:
                    edges += 1

        return area, edges

    groups = group_adjacent_values(lines)
    s = 0
    for group in groups:
        area, edges = calculate_area_and_sides(group, lines)
        print(group, area, edges)
        s += area * edges
        print(s)

    print(s)