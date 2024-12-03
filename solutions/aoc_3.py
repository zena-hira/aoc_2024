import re

def one(lines):
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, lines)
    pattern = r'\d+'
    s = 0
    for mul in matches:
        digits = list(map(int, re.findall(pattern, mul)))
        s += digits[0] * digits[1]
    return s


def two(lines):
    pattern = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"
    do = r"do\(\)"
    dont = r"don't\(\)"
    mul = r"mul\(\d+,\d+\)"
    calc = True
    matches = re.findall(pattern, lines)
    s = 0
    dig = r'\d+'

    for m in matches:
        if calc:
            if re.match(mul, m):
                digits = list(map(int, re.findall(dig, m)))
                s += digits[0] * digits[1]
        if re.match(dont, m):
            calc = False
        if re.match(do, m):
            calc = True

    return s

