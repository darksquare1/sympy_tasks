import sympy as sp

x = sp.Symbol('x')
f = sp.simplify(input())
df = sp.diff(f, x)
roots = sp.solve(df, x)
ans = []

for root in roots:
    if sp.diff(df, x).subs(x, root) > 0:
        ans.append(f"Точка ({root}, {f.subs(x, root)}) - локальный минимум")
    elif sp.diff(df, x).subs(x, root) < 0:
        ans.append(f"Точка ({root}, {f.subs(x, root)}) - локальный максимум")
if ans:
    [print(i) for i in ans]
else:
    print("Функция не имеет экстремумов")
