nums = [2, 8, 9, 1]
opers = ['+', '-', '*', '/']

def safe_eval(expr):
    try:
        return eval(expr)
    except ZeroDivisionError:
        return None

def permutations(lst):
    if len(lst) == 1:
        return [lst]
    result = []
    for i in range(len(lst)):
        rest = lst[:i] + lst[i+1:]
        for p in permutations(rest):
            result.append([lst[i]] + p)
    return result

def products(opers, repeat):
    if repeat == 0:
        return [[]]
    result = []
    for op in opers:
        for p in products(opers, repeat - 1):
            result.append([op] + p)
    return result

for perm in permutations(nums):
    a, b, c, d = perm

    for ops in products(opers, 3):
        op1, op2, op3 = ops

        expressions = [
            f'(({a} {op1} {b}) {op2} {c}) {op3} {d}',
            f'({a} {op1} ({b} {op2} {c})) {op3} {d}',
            f'{a} {op1} (({b} {op2} {c}) {op3} {d})',
            f'{a} {op1} ({b} {op2} ({c} {op3} {d}))',
            f'({a} {op1} {b}) {op2} ({c} {op3} {d})'
        ]

        for expr in expressions:
            if safe_eval(expr) == 10:
                print(expr, "= 10")