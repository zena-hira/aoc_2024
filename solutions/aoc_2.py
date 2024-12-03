def one(lines):
    s = 0
    for lst in lines:
        is_increasing = all(x < y for x, y in zip(lst, lst[1:]))
        is_decreasing = all(x > y for x, y in zip(lst, lst[1:]))

        # Check difference between adjacent levels
        valid_difference = all(1 <= abs(x - y) <= 3 for x, y in zip(lst, lst[1:]))

        if (is_increasing or is_decreasing) and valid_difference:
            s += 1

    return s
def two(lines):
    s = 0

    def is_safe(lst):
        # Check if a list is valid based on the rules
        is_increasing = all(x < y for x, y in zip(lst, lst[1:]))
        is_decreasing = all(x > y for x, y in zip(lst, lst[1:]))
        valid_difference = all(1 <= abs(x - y) <= 3 for x, y in zip(lst, lst[1:]))
        return (is_increasing or is_decreasing) and valid_difference

    for lst in lines:
        if is_safe(lst):
            s += 1
            continue

        for i in range(len(lst)):
            modified_levels = lst[:i] + lst[i + 1:]
            if is_safe(modified_levels):
                s += 1
                break

    return s