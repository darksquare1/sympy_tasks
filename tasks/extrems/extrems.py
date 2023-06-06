import sympy as sp

x = sp.Symbol('x')
f = sp.simplify(input())
df = sp.diff(f, x)
roots = sp.solve(df, x)
flag = False
for root in roots:
    if sp.diff(df, x).subs(x, root) > 0:
        print(f"Точка ({root}, {f.subs(x, root)}) - минимум")
        flag = True
    elif sp.diff(df, x).subs(x, root) < 0:
        print(f"Точка ({root}, {f.subs(x, root)}) - максимум")
        flag = True
if not (flag):
    print("Функция не имеет экстремумов")
