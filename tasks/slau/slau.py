import sympy as sp

# на вход подается система из n уравнений с m неизвестными нужно найти решение системы
n, m = map(int, input().split())
symbols = sp.symbols(f'x:{m}')
equations = []
for i in range(n):
    expr = input()
    expr = sp.simplify(expr[:expr.find('=')] + str(-int(expr[expr.find('=') + 1]))) # приводим к однородной
    equations.append(expr)
print('решение системы:', sp.solve(equations, symbols))
