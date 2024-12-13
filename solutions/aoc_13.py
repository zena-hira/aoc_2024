from sympy import symbols, Eq, solve
import re
def solve_button_presses(x_a, y_a, x_b, y_b, x_target, y_target):
    a, b = symbols('a b', integer=True, nonnegative=True)
    eq1 = Eq(x_a * a + x_b * b, x_target)
    eq2 = Eq(y_a * a + y_b * b, y_target)

    solution = solve((eq1, eq2), (a, b), dict=True)
    valid_solutions = [sol for sol in solution if sol[a] >= 0 and sol[b] >= 0]

    if valid_solutions:
        return valid_solutions[0][a], valid_solutions[0][b]
    else:
        return None


def extract_equation_systems(input_text):

    results = []

    for i in range(0, len(input_text), 3):
        button_a = input_text[i]
        button_b = input_text[i + 1]
        prize = input_text[i + 2]
        button_a_pattern = r"X\+([0-9]+), Y\+([0-9]+)"
        button_a_match = re.search(button_a_pattern, ' '.join(button_a))
        button_b_pattern = r"X\+([0-9]+), Y\+([0-9]+)"
        button_b_match = re.search(button_b_pattern, ' '.join(button_b))

        prize_pattern = r"X=([0-9]+), Y=([0-9]+)"
        prize_match = re.search(prize_pattern, ' '.join(prize))
        if button_a_match and button_b_match and prize_match:
            results.append({
                "Button A": {
                    "X_increment": int(button_a_match.group(1)),
                    "Y_increment": int(button_a_match.group(2))
                },
                "Button B": {
                    "X_increment": int(button_b_match.group(1)),
                    "Y_increment": int(button_b_match.group(2))
                },
                "Prize": {
                    "X_target": int(prize_match.group(1)),
                    "Y_target": int(prize_match.group(2))
                }
            })


    return results


def one(lines):
#     lines = """Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400
#
# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176
#
# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450
#
# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279"""

    extracted_data = extract_equation_systems(lines)

    s = 0
    for d in extracted_data:
        result = solve_button_presses(d['Button A']['X_increment'], d['Button A']['Y_increment'],
                             d['Button B']['X_increment'], d['Button B']['Y_increment'],
                             d['Prize']['X_target'], d['Prize']['Y_target'])
        if result:
            s += 3 * result[0] + result[1]

    return s
def two(lines):
    def extract_equation_systems(input_text):

        results = []

        for i in range(0, len(input_text), 3):
            button_a = input_text[i]
            button_b = input_text[i + 1]
            prize = input_text[i + 2]
            button_a_pattern = r"X\+([0-9]+), Y\+([0-9]+)"
            button_a_match = re.search(button_a_pattern, ' '.join(button_a))
            button_b_pattern = r"X\+([0-9]+), Y\+([0-9]+)"
            button_b_match = re.search(button_b_pattern, ' '.join(button_b))

            prize_pattern = r"X=([0-9]+), Y=([0-9]+)"
            prize_match = re.search(prize_pattern, ' '.join(prize))
            if button_a_match and button_b_match and prize_match:
                results.append({
                    "Button A": {
                        "X_increment": int(button_a_match.group(1)),
                        "Y_increment": int(button_a_match.group(2))
                    },
                    "Button B": {
                        "X_increment": int(button_b_match.group(1)),
                        "Y_increment": int(button_b_match.group(2))
                    },
                    "Prize": {
                        "X_target": 10000000000000 + int(prize_match.group(1)),
                        "Y_target": 10000000000000 + int(prize_match.group(2))
                    }
                })

        return results

    extracted_data = extract_equation_systems(lines)

    s = 0
    for d in extracted_data:
        result = solve_button_presses(d['Button A']['X_increment'], d['Button A']['Y_increment'],
                                      d['Button B']['X_increment'], d['Button B']['Y_increment'],
                                      d['Prize']['X_target'], d['Prize']['Y_target'])
        if result:
            s += 3 * result[0] + result[1]

    return s
