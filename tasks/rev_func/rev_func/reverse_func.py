import sympy as sp
from matplotlib import pyplot as plt
import numpy as np

f = input()
x, y = sp.symbols("x y")
a = sp.Eq(y, sp.simplify(f))
# подставим икс вместо игрик а игрик вместо икса
a = sp.Eq(a.lhs.subs(y, x), a.rhs.subs(x, y))
# выражаем y
q = sp.solve(a, y)
# это наша обратная функция
a = sp.Eq(y, *q)
# выражение для лямбдирования
y = a.rhs
# делаем функцию лямбдой чтобы преобразовать в массив нампая
lambd_expr = sp.lambdify(x, y)

points = np.linspace(-20, 20, 1000)
# получаем массив значений во всех наших точках
output = lambd_expr(points)
# рисуем график
plt.plot(points, output)
plt.show()