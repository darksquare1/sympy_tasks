import sympy as sp

x = sp.Symbol('x')
f = sp.simplify(input())
df = sp.diff(f, x)
roots = sp.solve(df, x)
flag = False
for root in roots: # используется вторая производная
    if sp.diff(df, x).subs(x, root) > 0:
        print(f"({root}, {f.subs(x, root)}) - min")
        flag = True
    elif sp.diff(df, x).subs(x, root) < 0:
        print(f"({root}, {f.subs(x, root)}) - max")
        flag = True
if not (flag):
    print("No extremums")
