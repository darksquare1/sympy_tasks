import sympy as sp

x = sp.Symbol('x')
f = sp.simplify(input()) # наша функция
n = int(input()) # до какого члена разбить ряд
a = int(input()) # точка в которой ищем приближенное значение
# найдем ряд тейлора функции f(x) в точке 0
taylor_series = sp.series(f, x, 0, n=n).removeO()
print(taylor_series)
# найдем приближенное значение
taylor_series = taylor_series.subs(x, a)
print(taylor_series.evalf().round(3))
