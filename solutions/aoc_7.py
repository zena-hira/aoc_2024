from itertools import permutations


def one(lines):
    lines= """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".splitlines()

    n = []
    for line in lines:
        tmp = line.split(':')
        l = [int(tmp[0])]
        for el in tmp[1].split():
            l.append(int(el))
        n.append(l)

    def func(res, l):
        if (res != 0 and len(l) == 0) or (res == 0 and len(l) != 0):
            return False
        if res == 0 and len(l) == 0:
            return True
        if res - l[-1] >= 0 and func(res - l[-1], l[:-1]):
            return True
        if res % l[-1] == 0 and func(res // l[-1], l[:-1]):
            return True


        return False

    def call_f(n):
        s = 0
        for l in n:
            if func(l[0], l[1:]):
                s += l[0]

        return s
    return call_f(n)


def two(lines):
#     lines = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20
# """.splitlines()

    n = []
    for line in lines:
        tmp = line.split(':')
        l = [int(tmp[0])]
        for el in tmp[1].split():
            l.append(int(el))
        n.append(l)

    def undo_concat(x,y):
        sx = str(x)
        sy = str(y)
        if str(x).endswith(str(y)) and len(sx) > len(sy):
            return int(sx[0:len(sx) - len(sy)])
        return None

    def func(res, l):
        if (res != 0 and len(l) == 0) or (res == 0 and len(l) != 0):
            return False
        if res == 0 and len(l) == 0:
            return True
        if res - l[-1] >= 0 and func(res - l[-1], l[:-1]):
            return True
        if res % l[-1] == 0 and func(res // l[-1], l[:-1]):
            return True
        k = undo_concat(res, l[-1])
        if len(l) > 1 and k is not None and func(k, l[:-1]):
            return True

        return False

    def call_f(n):
        s = 0
        for l in n:
            if func(l[0], l[1:]):
                s += l[0]

        return s

    return call_f(n)