from itertools import product

file = open('data/7.txt', 'r')
lines = file.read().splitlines()

def evaluate_expr(expr):
    res = expr[0]
    for i in range(1, len(expr), 2):
        if expr[i] == '+':
            res += expr[i+1]
            continue
        res *= expr[i+1]
    return res

# can be improved by early-skipping absurd operations
# e.g. if a +|* b is already greater than the result, skip the rest of the expression
validsum = 0
for l in lines:
    res, operands = l.split(':')
    res, operands = int(res), [int(x) for x in operands.split()]
    
    combs = product(['+', '*'], repeat=len(operands) - 1)

    for c in combs:
        expression = [operands[0]]
        for i in range(len(c)):
            expression.append(c[i])
            expression.append(operands[i+1])
        if evaluate_expr(expression) == res:
            validsum += res
            break

print(validsum)