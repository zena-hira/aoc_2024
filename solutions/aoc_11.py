def one(lines):
    # lines = "125 17".splitlines()
    lines = [list(map(int, line.strip().replace(',', '').split())) for line in lines][0]
    h = {}

    def transform(num):
        if num == 0:
            return 1
        elif len(str(num)) % 2 == 0:
            splitter = len(str(num)) // 2
            return int(str(num)[:splitter]), int(str(num)[splitter:])

        else:
            return 2024 * num

    def first_pass(lines):
        for num in lines:
            val = transform(num)
            if type(val) is int:
                if val in h.keys():
                    h[val] += 1
                else:
                    h[val] = 1
            else:
                if val[0] in h.keys():
                    h[val[0]] += 1
                else:
                    h[val[0]] = 1
                if val[1] in h.keys():
                    h[val[1]] += 1
                else:
                    h[val[1]] = 1


    first_pass(lines)

    def run(h):
        for it in range(0, 24):
            d = {}
            for num,v in h.items():
                for i in range(0, v):
                    val = transform(num)
                    if type(val) is int:
                        if val in d.keys():
                            d[val] += 1
                        else:
                            d[val] = 1
                    else:
                        if val[0] in d.keys():
                            d[val[0]] += 1
                        else:
                            d[val[0]] = 1
                        if val[1] in d.keys():
                            d[val[1]] += 1
                        else:
                            d[val[1]] = 1
            h = dict(d)
        return d

    d = run(h)
    return sum(v for v in d.values())


def two(lines):
    # lines = "125 17".splitlines()
    lines = [list(map(int, line.strip().replace(',', '').split())) for line in lines][0]
    h = {}

    def transform(num):
        if num == 0:
            return 1
        elif len(str(num)) % 2 == 0:
            splitter = len(str(num)) // 2
            return int(str(num)[:splitter]), int(str(num)[splitter:])

        else:
            return 2024 * num

    def first_pass(lines):
        for num in lines:
            val = transform(num)
            if type(val) is int:
                if val in h.keys():
                    h[val] += 1
                else:
                    h[val] = 1
            else:
                if val[0] in h.keys():
                    h[val[0]] += 1
                else:
                    h[val[0]] = 1
                if val[1] in h.keys():
                    h[val[1]] += 1
                else:
                    h[val[1]] = 1

    first_pass(lines)

    def run(h):
        for it in range(0, 74):
            d = {}
            for num, v in h.items():
                val = transform(num)
                if type(val) is int:
                    if val in d.keys():
                        d[val] += v
                    else:
                        d[val] = v
                else:
                    if val[0] in d.keys():
                        d[val[0]] += v
                    else:
                        d[val[0]] = v
                    if val[1] in d.keys():
                        d[val[1]] += v
                    else:
                        d[val[1]] = v
            h = dict(d)
        return d

    d = run(h)
    return sum(v for v in d.values())
