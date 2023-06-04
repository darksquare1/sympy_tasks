import sympy as sp

x0 = float(input()) #размеры холста
y0 = float(input())
g = 9.8
x = sp.Symbol("x")

p = sp.Float(1000)

print(g*sp.integrate(p*y0*x, (x, 0, x0)))  #используем формулу и выводим
