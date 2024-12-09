import numpy as np
import itertools


def one(rules, order):
#     rules =  """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13""".splitlines()
#
#     order = """75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47""".splitlines()

    # rules = [line.strip() for line in rules]
    order = [line[0].split(',') for line in order]
    h = {}

    for r in rules:
        b, a = r[0].split('|')
        if b in h.keys():
            h[b].append(a)
        else:
            h[b] = [a]

    r = []
    for l in order:

        flag = True
        for idx in range(len(l)):
            if not flag:
                break
            if l[idx] in h.keys():
                for n in h[l[idx]]:
                    if n not in l:
                        continue
                    else:
                        index = l.index(n)
                        if idx < index:
                            continue
                        else:
                            flag = False
                            break
        if flag:
            r.append(l)
    s = 0
    for el in r:
        s += int(el[len(el)//2])
    return s



def is_valid(sequence, h):
    """
    Check if a sequence satisfies the rules in the dependency graph `h`.
    """
    for idx, elem in enumerate(sequence):
        if elem in h:
            for dependent in h[elem]:
                if dependent in sequence[:idx]:
                    return False
    return True


def find_valid_permutation(order, h):
    """
    Use backtracking to find the first valid permutation of the order that satisfies the rules in `h`.
    """
    n = len(order)
    used = [False] * n
    result = []

    def backtrack(path):
        if len(path) == n:
            result.append(path[:])
            return True

        for i in range(n):
            if not used[i]:
                path.append(order[i])
                if is_valid(path, h):
                    used[i] = True
                    if backtrack(path):
                        return True
                    used[i] = False
                path.pop()
        return False

    backtrack([])
    return result[0] if result else None
def two(rules, order):
#     rules =  """47|53
# 97|13
# 97|61
# 97|47
# 75|29
# 61|13
# 75|53
# 29|13
# 97|29
# 53|29
# 61|53
# 97|53
# 61|29
# 47|13
# 75|47
# 97|75
# 47|61
# 75|61
# 47|29
# 75|13
# 53|13"""
#
#     order = """75,47,61,53,29
# 97,61,53,29,13
# 75,29,13
# 75,97,47,61,53
# 61,13,29
# 97,13,75,29,47"""
#
#

    def is_correct(sequence, h):
        for idx, elem in enumerate(sequence):
            if elem in h:
                for dependent in h[elem]:
                    if dependent in sequence:
                        if idx > sequence.index(dependent):
                            return False, sequence[:idx + 1]
        return True, None

    rules = [r[0].split('|') for r in rules]
    order = [line[0].split(',') for line in order]

    h = {}
    for b, a in rules:
        if b in h:
            h[b].append(a)
        else:
            h[b] = [a]

    r = []
    for l in order:
        val, pr = is_correct(l, h)

        if not val:
            todo = list(l)
            out = []
            while todo:
                for i in range(len(todo)):
                    is_ok = True
                    for j in range(len(todo)):
                        if todo[j] in h and todo[i] in h[todo[j]]:
                            is_ok = False
                            break
                    if is_ok:
                        out.append(todo[i])
                        todo = todo[0:i] + todo[i+1:]
                        break

            r.append(out)

    s = sum(int(el[len(el) // 2]) for el in r)
    return s

