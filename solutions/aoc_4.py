def one(st):
    # st = """MMMSXXMASM
    #         MSAMXMSMSA
    #         AMXSXMAAMM
    #         MSAMASMSMX
    #         XMASAMXAMM
    #         XXAMMXXAMA
    #         SMSMSASXSS
    #         SAXAMASAAA
    #         MAMMMXMMMM
    #         MXMXAXMASX""".splitlines()
    st = [line.strip() for line in st]
    s = 0
    target = 'XMAS'

    def check_horizontal_left(r, c, target_str):
        return c - len(target_str) + 1 >= 0 and all(st[r][c - i] == target_str[i] for i in range(len(target_str)))

    def check_horizontal_right(r, c, target_str):
        return c + len(target_str) <= len(st[0]) and all(st[r][c + i] == target_str[i] for i in range(len(target_str)))

    def check_vertical_up(r, c, target_str):
        return r - len(target_str) + 1 >= 0 and all(st[r - i][c] == target_str[i] for i in range(len(target_str)))

    def check_vertical_down(r, c, target_str):
        return r + len(target_str) <= len(st) and all(st[r + i][c] == target_str[i] for i in range(len(target_str)))

    def check_diagonal_down_right(r, c, target_str):
        return r + len(target_str) <= len(st) and c + len(target_str) <= len(st[0]) and all(
            st[r + i][c + i] == target_str[i] for i in range(len(target_str)))

    def check_diagonal_up_right(r, c, target_str):
        return r - len(target_str) + 1 >= 0 and c + len(target_str) <= len(st[0]) and all(
            st[r - i][c + i] == target_str[i] for i in range(len(target_str)))

    def check_diagonal_down_left(r, c, target_str):
        return r + len(target_str) <= len(st) and c - len(target_str) + 1 >= 0 and all(
            st[r + i][c - i] == target_str[i] for i in range(len(target_str)))

    def check_diagonal_up_left(r, c, target_str):
        return r - len(target_str) + 1 >= 0 and c - len(target_str) + 1 >= 0 and all(
            st[r - i][c - i] == target_str[i] for i in range(len(target_str)))

    # Iterate through the grid and count matches in all directions
    for r in range(len(st)):
        for c in range(len(st[0])):
            if check_horizontal_left(r, c, target):
                s += 1
            if check_horizontal_right(r, c, target):
                s += 1
            if check_vertical_up(r, c, target):
                s += 1
            if check_vertical_down(r, c, target):
                s += 1
            if check_diagonal_down_right(r, c, target):
                s += 1
            if check_diagonal_up_right(r, c, target):
                s += 1
            if check_diagonal_down_left(r, c, target):
                s += 1
            if check_diagonal_up_left(r, c, target):
                s += 1
    return s

def two(st):
    # st = """.M.S......
    #         ..A..MSMS.
    #         .M.S.MAA..
    #         ..A.ASMSM.
    #         .M.S.M....
    #         ..........
    #         S.S.S.S.S.
    #         .A.A.A.A..
    #         M.M.M.M.M.
    #         ..........""".splitlines()
    st = [line.strip() for line in st]

    def check_diagonal_down_right(r, c, target_str):
        return r + 1 + len(target_str) <= len(st) and c + 1 + len(target_str) <= len(st[0]) and st[r + 1][c + 1] == target_str

    def check_diagonal_up_right(r, c, target_str):
        return r - 1 - len(target_str) + 1 >= 0 and c + 1 + len(target_str) <= len(st[0]) and st[r - 1][c + 1] == target_str

    def check_diagonal_down_left(r, c, target_str):
        return r + 1 + len(target_str) <= len(st) and c - 1 - len(target_str) + 1 >= 0 and st[r + 1][c - 1] == target_str

    def check_diagonal_up_left(r, c, target_str):
        return r - 1- len(target_str) + 1 >= 0 and c - 1 - len(target_str) + 1 >= 0 and st[r - 1][c - 1] == target_str

    s = 0
    for r in range(len(st)):
        for c in range(len(st[0])):
            if st[r][c] == 'A':
                if check_diagonal_down_right(r, c, 'S') and check_diagonal_up_left(r, c, 'M') and check_diagonal_down_left(r, c, 'M') and check_diagonal_up_right(r, c, 'S'):
                        s += 1
                elif check_diagonal_down_right(r, c, 'M') and check_diagonal_up_left(r, c,'S') and check_diagonal_down_left(r,c,'M') and check_diagonal_up_right(r, c, 'S'):
                    s += 1
                elif check_diagonal_down_right(r, c, 'M') and check_diagonal_up_left(r, c,'S') and check_diagonal_down_left(r,c,'S') and check_diagonal_up_right(r, c, 'M'):
                    s += 1
                if check_diagonal_down_right(r, c, 'S') and check_diagonal_up_left(r, c, 'M') and check_diagonal_down_left(r, c, 'S') and check_diagonal_up_right(r, c, 'M'):
                        s += 1

    return s


