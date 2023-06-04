import sympy as sp

x = sp.Symbol('x')
f = sp.simplify(input())  # функция
a, b = map(int, input().split())  # отрезок которому принадлежит x
dif_f = f.diff(x)
f = sp.sqrt(1 + dif_f ** 2)  # формула подынтегральной функции для нахождения длины дуги
ans = sp.integrate(f, (x, a, b))  # интегрируем
print(round(ans, 3))
