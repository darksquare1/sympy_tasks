
import sympy as sp
# Определяем переменную x
x = sp.Symbol('x')
# Определяем функцию f(x)
f = sp.simplify(input())
# Находим производную функции
df = sp.diff(f, x)
# Находим корни производной
roots = sp.solve(df, x)
# Определяем тип экстремумов
if len(roots) == 0:
    print("Функция не имеет экстремумов")
else:
    for root in roots:
        if sp.diff(df, x).subs(x, root) > 0:
            print(f"Точка ({root}, {f.subs(x, root)}) - локальный минимум")
        elif sp.diff(df, x).subs(x, root) < 0:
            print(f"Точка ({root}, {f.subs(x, root)}) - локальный максимум")
        else:
            print(f"Точка ({root}, {f.subs(x, root)}) - не является экстремумом")