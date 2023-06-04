import sympy as sp
from matplotlib import pyplot as plt
import numpy as np
 
f = input()
x, y = sp.symbols("x y")
a = sp.Eq(y, sp.simplify(f))
a = sp.Eq(a.lhs.subs(y, x), a.rhs.subs(x, y)) # подставляем икс вместо игрика а игрик вместо икса
q = sp.solve(a, y) # выражаем y
l = [sp.Eq(y, i).rhs for i in q] # Обратная функция
print(*l)
m = np.linspace(-10, 10, 1000)

for i in l: # "лямбдируем функциии и строим график
  y = i
  lambd_expr = sp.lambdify(x, y)
  output = lambd_expr(m)
  plt.plot(m, output)
plt.show()
