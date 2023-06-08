#import sympy as sp
n, m = map(int, input().split())
#symbols = sp.symbols(f'x:{m}')
equations = []
for i in range(n):
    expr = input()
    #expr = sp.simplify(expr[:expr.find('=')] + '-' + str(int(expr[expr.find('=') + 1:])))
    #equations.append(expr)
#print('system solution:', sp.solve(equations, symbols) if sp.solve(equations, symbols) else "No solution")
print('hello')# --